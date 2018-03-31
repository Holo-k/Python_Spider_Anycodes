from selenium import webdriver
from urllib import request
from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument("--headless")

client = webdriver.Chrome()
# chrome_options=options
client.get('https://www.bilibili.com/read/cv257121')
input("Please press enter to continue.")
temp_cookie = ""
print(client.get_cookies())
for eve_cookie in client.get_cookies():
        temp_cookie = temp_cookie + eve_cookie["name"] + "=" + eve_cookie["value"] + "; "

print(temp_cookie)