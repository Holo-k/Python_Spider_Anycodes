import urllib.request
import urllib.parse
import re
import json
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    "Cookie":
    'showCardBeforeSign=1; TIEBAUID=52dc7439a737f107bb48a990; TIEBA_USERTYPE=ef91730aa1095d6b122774bb; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1521966820,1521968633,1521968997,1521969089; STOKEN=db481014aa009adfb015252c79cf402c3080a184a3e1558f4aeedc6b4cdcfb30; td_cookie=18446744072533583864; rpln_guide=1; bdshare_firstime=1519382054304; wise_device=0; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1521969089; BAIDUID=F592898E306DD569FAB0D7AC9BC13779:FG=1; BIDUPSID=F592898E306DD569FAB0D7AC9BC13779; PSTM=1519044896; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=XFacW8tYllweHJidmROVC1wdDBxLUw5eXJHaHE3U2VUTUNoeVczaVloZGZNc1phQVFBQUFBJCQAAAAAAAAAAAEAAADAFFZJVGlhbmtpX0MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF-lnlpfpZ5ac; H_PS_PSSID=1462_21087_18560_20883_26023; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6',
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167Safari/537.36"
}


def SignAdd(kw, tbs_data):
    url = "https://tieba.baidu.com/sign/add"

    post_data = {
        "ie": "utf-8",
        "kw": kw,
        "tbs": tbs_data,
    }
    print(kw)
    print(tbs_data)

    data = urllib.parse.urlencode(post_data).encode("utf-8")
    post_req = urllib.request.Request(url=url, data=data, headers=headers)
    try:
        return (kw,
                json.loads(
                    urllib.request.urlopen(post_req).read().decode("utf-8"))[
                        "data"]["errmsg"])
    except:
        return (kw, "faild")


forum_list = re.findall('"forum_id":(.*?),"forum_name":"(.*?)"',
                        urllib.request.urlopen(
                            urllib.request.Request(
                                url="https://tieba.baidu.com/index.html",
                                headers=headers)).read().decode())

for eve_forum in forum_list:
    kw = eve_forum[1].encode('latin-1').decode("unicode_escape")
    forum_url = "https://tieba.baidu.com/f?kw=" + urllib.parse.quote(kw)
    time.sleep(3)
    tbs_data = re.findall('\'tbs\': "(.*?)" ',urllib.request.urlopen(urllib.request.Request(url=forum_url,headers=headers)).read().decode("utf-8"))[0]
    
    print(" - ".join(SignAdd(kw,tbs_data)))
