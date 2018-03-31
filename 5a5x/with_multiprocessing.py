from urllib import request
from socket import timeout
import socket
import os
from lxml import etree
import multiprocessing as mp


def parse_index(source_url, eve_list_data):
    if not os.path.exists(eve_list_data):
        os.mkdir(eve_list_data)
    page_total = int(
        etree.HTML(request.urlopen(source_url).read().decode('gbk')).xpath(
            '//*[@id="pages"]/b[2]/text()')[0].replace('/', ''))
    return page_total


def parse_content_list(source_url, page_index):
    url = f'{source_url}{str(page_index)}.html'
    page_source = request.urlopen(url).read().decode('gbk')
    content_list = etree.HTML(page_source).xpath(
        '//dl[@class="down_list"]/dt[1]/a/@href')
    for page_href in content_list:
        yield page_href


def parse_detail(eve_content):
    host = 'http://www.5a5x.com/'
    content_url = host + eve_content
    content_page_source = request.urlopen(content_url).read().decode('gbk')
    title = etree.HTML(content_page_source).xpath(
        '//*[@id="content"]/table/caption/span/text()')[0]
    download_url = etree.HTML(content_page_source).xpath(
        '//div[@id="down_address"]/a/@href')[0]
    file_url = host + download_url
    file_url = host + etree.HTML(
        request.urlopen(file_url).read().decode('gbk')).xpath('//a/@href')[0]
    return title, file_url


def save_file(eve_list_data, title, file_url):
    with open(f'{eve_list_data}/{title}.zip', mode='wb') as file:
        file.write(request.urlopen(file_url).read())


def main(eve_list_data):
    os.chdir('./5a5x')
    source_url = f'http://www.5a5x.com/wode_source/{eve_list_data}/'
    page_total = parse_index(source_url, eve_list_data)
    for page_index in range(1, page_total + 1):
        eve_content = parse_content_list(source_url, page_index)
        for item in eve_content:
            title, file_url = parse_detail(item)
            save_file(eve_list_data, title, file_url)


if __name__ == '__main__':
    list_data = [
        'etools', 'eimage', 'emedia', 'egame', 'edata', 'ecom', 'etrade',
        'enetwork'
    ]
    pool = mp.Pool()
    pool.map(main, list_data)
