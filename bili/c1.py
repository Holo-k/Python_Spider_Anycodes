from urllib import request, parse

headers = {
    'Accept':
    '',
    'Accept-Encoding':
    'gzip, deflate, br',
    'Accept-Language':
    'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
    'Connection':
    'Keep-Alive',
    'Cookie':
    'DedeUserID__ckMd5=6ae64df51460133d; _dfcaptcha=6b58e83c06b2b62e266b081c93e88c1f; finger=ee9500f4; fts=1519032468; pos=57; sid=izoezz1k; buvid3=5704C3E7-CDD7-49A6-9E2A-F94B983AB64E48507infoc; UM_distinctid=161ad6400eaa1-03025c04525936-7047503f-144000-161ad6400eb7c; DedeUserID=4204460; pgv_pvi=7945914368; rpdid=iowilliowwdosoloqlppw; purl_token=bilibili_1522068431; bili_jct=d3273ae0f0778ddee04a757ed5b2accc; LIVE_BUVID__ckMd5=2b67f87f7a77acea; SESSDATA=170ea3cc%2C1522569477%2Ce41d387d; LIVE_BUVID=356823340b088c1a71355e702401adb6',
    'Host':
    'interface.bilibili.com',
    'Origin':
    'https://www.bilibili.com',
    'Referer':
    'https://static.hdslb.com/play.swf?cid=34552110&aid=21063735&pre_ad=',
    'User-Agent':
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'
}

v_url = 'https://cn-hbcd2-cu-v-01.acgvideo.com/vg8/e/f2/34552110-1-64.flv?expires=1522078200&platform=pc&ssig=WelfwnThjrm0uLcVWppRFw&oi=989667853&nfa=gowYgs5wsUTMXpHkPMpUUA==&dynamic=1&hfa=2022430171&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI='

print(request.urlopen(request.Request(v_url, headers=headers)).read())
