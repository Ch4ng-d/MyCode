import requests
post_data = {"password":"s155964671a"}
get_data = {"name":"s214587387a"}

response = requests.post("http://node5.anna.nssctf.cn:22442/",data=post_data,params=get_data)

print(response.text)