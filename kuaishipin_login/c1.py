from urllib import request, parse
import re
import hashlib


def get_token(account):
    url = f'https://login.360.cn/?func=jQuery18306112322012802309_1521989893363&src=pcw_svideo&from=pcw_svideo&charset=utf-8&requestScema=https&o=sso&m=getToken&userName={account}&_=1521989920587'
    response = request.urlopen(request.Request(
        url, headers=headers)).read().decode()
    return re.search('"token":"(.*?)"', response).group(1)


def password_encrypted(password):
    m = hashlib.md5()
    m.update(password)
    return m.hexdigest()


def login(account, password):
    token = get_token(account)
    data = {
        'account': account,
        'callback': 'QiUserJsonp989893391',
        'captcha': 'HYKWX',
        'captchaApp': 'i360',
        'captFlag': '1',
        'charset': 'utf-8',
        'from': 'pcw_svideo',
        'func': 'QiUserJsonp989893391',
        'isKeepAlive': '0',
        'lm': '0',
        'm': 'login',
        'o': 'sso',
        'password': password_encrypted(password.encode('UTF-8')),
        'proxy': 'http%3A%2F%2Fk.360kan.com%2Fpsp_jump.html',
        'requestScema': 'https',
        'rtype': 'data',
        'smDeviceId': '',
        'src': 'pcw_svideo',
        'token': token,
    }
    data = parse.urlencode(data).encode('UTF-8')
    login_url = 'https://login.360.cn/'
    response = request.urlopen(
        request.Request(login_url, data=data, headers=headers,
                        method='POST')).read().decode('utf-8')
    print(response)


def main():
    account = input('Enter your account: ')
    password = input('Enter your password: ')
    login(account, password)


if __name__ == '__main__':
    headers = {
        'Accept':
        'application/javascript, */*; q=0.8',
        'Accept-Encoding':
        'gzip, deflate, br',
        'Accept-Language':
        'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
        'Connection':
        'Keep-Alive',
        'Cookie':
        '__guid=91251416.3221989064145265700.1519366967313.424; __huid=11mSNI8yIOkgk0rYEpgbIZCTCfRY5m7UfJQnzQoCqJORQ=; quCryptCode=D6TqMQxFspmbcRQUW6CG6adk6kreQJy4EnyhVYpTCDuZ3SdLwDXbrB%252BPTjv%252FFKL%252BM%252BzCLmEIoNs%253D; quCapStyle=2',
        'Host':
        'login.360.cn',
        'Referer':
        'http://k.360kan.com/',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    }
    main()
