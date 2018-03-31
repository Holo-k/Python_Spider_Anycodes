from urllib import request

url = 'http://m10.music.126.net/20180328225222/f5548a716fe9bdbb72d34999ba6ea662/ymusic/542f/a73a/67c1/06bb55823239e27bd6880f3bbb713670.mp3'
response = request.urlopen(url)
with open('4.mp3', mode='wb') as file:
    file.write(response.read())