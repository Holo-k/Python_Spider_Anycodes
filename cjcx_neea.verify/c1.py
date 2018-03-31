from urllib import request
from urllib import parse


def get_headers(verify=""):
    headers = {
        'Accept':
        'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
        'Accept-Encoding':
        'gzip, deflate',
        'Accept-Language':
        'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
        'Connection':
        'Keep-Alive',
        'Cookie':
        f'Hm_lpvt_dc1d69ab90346d48ee02f18510292577=1522127206; {verify}; Hm_lvt_dc1d69ab90346d48ee02f18510292577=1522126702; language=1; UM_distinctid=16265d247404d7-0c45c70a646eae-7047503f-144000-16265d24741cf6; esessionid=28EBFE9A7EDAE5DE25F1C0867059B19C; BIGipServersearchtest.neea.edu.cn_search.neea.cn_pool=1889585162.37407.0000; td_cookie=18446744072693736824',
        'Host':
        'search.neea.edu.cn',
        'Referer':
        'http://search.neea.edu.cn/QueryMarkUpAction.do?act=doQueryCond&sid=280&pram=results&ksnf=2Ba049ynilaf8I9J7JxJnIu&sf=11&bkjb=1&zkzh=&name=%E5%93%81%E7%89%8C&sfzh=547864102545698741',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    }
    return headers


def get_verify_image():
    url = 'http://search.neea.edu.cn/Imgs.do?act=verify&t=0.7178557184878571'
    response = request.urlopen(request.Request(url, headers=get_headers()))
    with open('v_img.png', mode='wb') as file:
        file.write(response.read())
    return response.headers['Set-Cookie']


def query_score(verify_cookies):
    verify = input('please input verify code: ')
    url = 'http://search.neea.edu.cn/QueryMarkUpAction.do?act=doQueryResults'
    data = {
        'pram':
        'results',
        'ksxm':
        '280',
        'nexturl':
        '/QueryMarkUpAction.do?act=doQueryCond&sid=280&pram=results&ksnf=2Ba049ynilaf8I9J7JxJnIu&sf=11&bkjb=1&zkzh=&name=品牌&sfzh=458952014699874502',
        'ksnf':
        '2Ba049ynilaf8I9J7JxJnIu',
        'sf':
        '11',
        'bkjb':
        '1',
        'zkzh':
        '',
        'name':
        '品牌',
        'sfzh':
        '458952014699874502',
        'verify':
        verify,
    }

    data = parse.urlencode(data).encode('utf-8')
    response = request.urlopen(
        request.Request(url, headers=get_headers(verify_cookies), data=data))
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    verify_cookies = get_verify_image()
    query_score(verify_cookies)