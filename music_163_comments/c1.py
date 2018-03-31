import urllib.request
import urllib.parse
import json
import base64
from crypto.Cipher import AES
import codecs
import re
import multiprocessing as mp

url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_27548281?csrf_token='

headers = {
    'Referer':
    'http://music.163.com/song?id=27548281',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}


# rid是视频的标志，offset是控制视频翻页的标志
def get_ParamsFirst(rid, offset):
    params_first = '{"rid":"' + rid + '","offset":"' + offset + '","total":"false","limit":"20","csrf_token":""}'
    return params_first


params_second = "010001"
params_third = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
params_forth = "0CoJUm6Qyw8W8jud"

# params需要第一个参数和第四个参数
# encSecKey需要第二个和第三个参数，还需要一个随机的16个字符组成的字符串


def aesEncrypt(text, key):
    # 偏移量
    iv = '0102030405060708'
    # 文本
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, 2, iv)
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext


def get_params(text, rid, offset):
    # 第一个参数
    params = aesEncrypt(get_ParamsFirst(rid, offset),
                        params_forth).decode('utf-8')
    params = aesEncrypt(params, text)
    return params


def rsaEncrypt(pubKey, text, modulus):
    '''进行rsa加密'''
    text = text[::-1]
    rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16)**int(
        pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


def get_encSEcKey(text):
    pubKey = params_second
    moudulus = params_third
    encSecKey = rsaEncrypt(pubKey, text, moudulus)
    return encSecKey


def main():
    rid = re.findall('comments/(.*?)\?', url)[0]
    offset = 0
    while True:
        text = "A" * 16
        params = get_params(text, rid, str(offset))
        encSEcKey = get_encSEcKey(text)
        formdata = {"params": params, "encSecKey": encSEcKey}

        temp_data = json.loads(
            urllib.request.urlopen(
                urllib.request.Request(
                    url=url,
                    data=urllib.parse.urlencode(formdata).encode("utf-8"),
                    headers=headers)).read().decode("utf-8"))["comments"]
        length = len(temp_data)
        for eve_data in temp_data:
            print(eve_data)
        if length == 20:
            offset = offset + 20
        else:
            break


if __name__ == '__main__':
    # pool = mp.Pool()
    # offset = []
    # pool.map(main, offset)
    main()