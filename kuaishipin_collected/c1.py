from urllib import request
import multiprocessing as mp
import json
from os import path
import ssl

ssl._create_default_https_context = ssl._create_unverified_context  #ssl关闭验证

def get_page_content(channel_id, page_index):
    url = f'http://pc.k.360kan.com/pc/list?n=10&p={page_index}&f=json&ajax=1&channel_id={str(channel_id)}&dl='
    response = request.urlopen(url).read().decode('utf-8')
    return json.loads(response)['data']['res']


def parse_detail(eve_data):
    title = eve_data['t']
    uid = eve_data['exData']['code']
    return (title, uid)


def save_file(title, uid):
    if not path.exists(f'{title}.mp4'):
        video_url = f'http://pc.k.360kan.com/pc/play?id={uid}&f=json'
        json_data = request.urlopen(video_url).read().decode('utf-8')
        download_url = json.loads(json_data)['data']['url']
        with open(
                f'./kuaishipin_collected/video/{title}.mp4',
                mode='wb') as file:
            file.write(request.urlopen(download_url).read())


def main(channel_id):
    page_index = 0
    while True:
        json_data = get_page_content(channel_id, page_index)
        for eve_data in json_data:
            (title, uid) = parse_detail(eve_data)
            save_file(title, uid)
            break
        if len(json_data) < 10:
        page_index += 1


if __name__ == '__main__':
    channel_list = [0, 109, 2, 13, 3, 8, 18, 19, 1, 7, 11, 12]
    pool = mp.Pool(processes=2)
    pool.map(main, channel_list)
