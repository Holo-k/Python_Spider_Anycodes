from urllib import request
from urllib import parse
import re
import time
import json


def get_forum_list():
    url = 'https://tieba.baidu.com/'
    response = request.urlopen(request.Request(
        url, headers=headers)).read().decode()
    forum_list = re.findall('"forum_name":"([\s\S]*?)"', response)
    return forum_list


def get_forum_detail(title):
    url = f'https://tieba.baidu.com/f?kw={parse.quote(title)}'
    response = request.urlopen(request.Request(
        url, headers=headers)).read().decode()
    tbs = re.search('\'tbs\': "([\s\S]*?)"', response, flags=re.M).group(1)
    return tbs


def check_in(kw, tbs):
    print(tbs)
    data = {'ie': 'utf-8', 'kw': kw, 'tbs': tbs}
    # data = bytes(parse.urlencode(data), encoding='UTF-8')
    data = parse.urlencode(data).encode('utf-8')
    print(data)
    url = 'https://tieba.baidu.com/sign/add'
    response = request.urlopen(
        request.Request(url, data=data, headers=headers,
                        method='POST')).read().decode('UTF-8')
    print(json.loads(response))


def main():
    time.sleep(2)
    forum_list = get_forum_list()
    for forum in forum_list:
        time.sleep(2)
        tbs = get_forum_detail(
            forum.encode('latin-1').decode("unicode_escape"))
        check_in(forum, tbs)


if __name__ == '__main__':
    headers = {
        'Cookie':
        'showCardBeforeSign=1; TIEBAUID=52dc7439a737f107bb48a990; TIEBA_USERTYPE=ef91730aa1095d6b122774bb; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1521966820,1521968633,1521968997,1521969089; STOKEN=db481014aa009adfb015252c79cf402c3080a184a3e1558f4aeedc6b4cdcfb30; td_cookie=18446744072533583864; rpln_guide=1; bdshare_firstime=1519382054304; wise_device=0; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1521969089; BAIDUID=F592898E306DD569FAB0D7AC9BC13779:FG=1; BIDUPSID=F592898E306DD569FAB0D7AC9BC13779; PSTM=1519044896; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=XFacW8tYllweHJidmROVC1wdDBxLUw5eXJHaHE3U2VUTUNoeVczaVloZGZNc1phQVFBQUFBJCQAAAAAAAAAAAEAAADAFFZJVGlhbmtpX0MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF-lnlpfpZ5ac; H_PS_PSSID=1462_21087_18560_20883_26023; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6',
        'Cookie':
        'wise_device=0; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1521981315; showCardBeforeSign=1; TIEBAUID=52dc7439a737f107bb48a990; TIEBA_USERTYPE=ef91730aa1095d6b122774bb; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1521968997,1521969089,1521969315,1521978872; STOKEN=db481014aa009adfb015252c79cf402c3080a184a3e1558f4aeedc6b4cdcfb30; td_cookie=18446744072547843409; rpln_guide=1; bdshare_firstime=1519382054304; H_PS_PSSID=1462_21087_18560_20883_26023; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6; BAIDUID=F592898E306DD569FAB0D7AC9BC13779:FG=1; BIDUPSID=F592898E306DD569FAB0D7AC9BC13779; PSTM=1519044896; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=XFacW8tYllweHJidmROVC1wdDBxLUw5eXJHaHE3U2VUTUNoeVczaVloZGZNc1phQVFBQUFBJCQAAAAAAAAAAAEAAADAFFZJVGlhbmtpX0MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF-lnlpfpZ5ac',
        'Host':
        'tieba.baidu.com'
    }
    main()
