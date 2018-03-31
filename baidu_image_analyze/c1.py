import requests
import json
import re


def upload_image():
    url = 'http://image.baidu.com/pcdutu/a_upload?fr=html5&target=pcSearchImage&needJson=true'
    files = {'file': open('./baidu_image_analyze/p2.jpg', mode='rb')}
    response = requests.post(url, files=files, headers=headers)
    jsonData = json.loads(response.text)
    return (jsonData['url'], jsonData['querySign'])


def analyze_image(image_url, querySign):
    headers = {
        'Host':
        'image.baidu.com',
        'Referer':
        'http://image.baidu.com/pcdutu?queryImageUrl=http%3A%2F%2Fe.hiphotos.baidu.com%2Fimage%2F%2570%2569%2563%2Fitem%2F2cf5e0fe9925bc311074769752df8db1cb137097.jpg&querySign=3874869466%2C3028513813&fm=index&uptype=upload_pc&result=result_camera&vs=7088ddf240c72188f8c81051bd20117f3703744d',
        'Upgrade-Insecure-Requests':
        '1',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    url = f'http://image.baidu.com/pcdutu?queryImageUrl={image_url}&querySign={querySign}&fm=home&uptype=upload_pc&result=result_camera'
    response = requests.get(url, headers=headers)
    return response.text


def print_Image_info(result):
    guessWord = re.findall("'guessWord': '(.*?)'", result)[0]
    term_data = re.findall(
        '"name":"(.*?)","baike":{"url":"(.*?)","abstract":"(.*?)","', result)
    if guessWord:
        print("您上传的图片可能是：", guessWord)
        print("除此之外，他还可能是：")
    else:
        print("您上传的图片最可能是：")
    for eve in term_data:
        print("名称：", eve[0], "\t描述：", eve[2], "\t百科地址：", eve[1])


if __name__ == '__main__':
    headers = {
        'Accept':
        '*/*',
        'Accept-Encoding':
        'gzip, deflate',
        'Accept-Language':
        'en-US,en;q=0.9',
        'Connection':
        'keep-alive',
        'Content-Length':
        '632938',
        'Cookie':
        'BAIDUID=40B2BFA5456C9988880903C687DC2138:FG=1; FP_UID=9d9a394a5b105d1d8c0c041d33b18622; BIDUPSID=40B2BFA5456C9988880903C687DC2138; PSTM=1520848573; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=null; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; td_cookie=18446744072684119308; shituhistory=%7B%220%22%3A%22http%3A%2F%2Fh.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F50da81cb39dbb6fddd9090290524ab18962b37f1.jpg%22%7D; sttbHint=sttbHintShow; Hm_lvt_9a586c8b1ad06e7e39bc0e9338305573=1522117590; tip_show_limit=3; Hm_lpvt_9a586c8b1ad06e7e39bc0e9338305573=1522117607',
        'Host':
        'image.baidu.com',
        'Origin':
        'http://image.baidu.com',
        'Referer':
        'http://image.baidu.com/',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'X-Requested-With':
        'XMLHttpRequest'
    }
    (image_url, querySign) = upload_image()
    result = analyze_image(image_url, querySign)
    print_Image_info(result)
