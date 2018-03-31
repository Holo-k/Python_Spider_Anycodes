from urllib import request
from socket import timeout
import socket
import os
from lxml import etree
import multiprocessing as mp

list_data = [
    'etools', 'eimage', 'emedia', 'egame', 'edata', 'ecom', 'etrade',
    'enetwork'
]
host = 'http://www.5a5x.com/'
os.chdir('./5a5x')
for eve_list_data in list_data:
    if not os.path.exists(eve_list_data):
        os.mkdir(eve_list_data)
    source_url = f'http://www.5a5x.com/wode_source/{eve_list_data}/'
    page_total = int(
        etree.HTML(request.urlopen(source_url).read().decode('gbk')).xpath(
            '//*[@id="pages"]/b[2]/text()')[0].replace('/', ''))
    for eve_content_page in range(1, page_total + 1):
        url = f'{source_url}{str(eve_content_page)}.html'
        page_source = request.urlopen(url).read().decode('gbk')
        content_list = etree.HTML(page_source).xpath(
            '//dl[@class="down_list"]/dt[1]/a/@href')
        for eve_content in content_list:
            content_url = host + eve_content
            content_page_source = request.urlopen(content_url).read().decode(
                'gbk')
            title = etree.HTML(content_page_source).xpath(
                '//*[@id="content"]/table/caption/span/text()')[0]
            download_url = etree.HTML(content_page_source).xpath(
                '//div[@id="down_address"]/a/@href')[0]
            file_url = host + download_url
            file_url = host + etree.HTML(
                request.urlopen(file_url).read().decode('gbk')).xpath(
                    '//a/@href')[0]
            with open(f'{eve_list_data}/{title}.zip', mode='wb') as file:
                file.write(request.urlopen(file_url).read())
