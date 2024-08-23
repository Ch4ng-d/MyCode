import requests

# 设置POST和GET参数
post_data = {"id": "wllmNB"}
get_data = {"json": '{"x":"wllm"}'}

# 发送请求到目标网址
response = requests.post("http://node4.anna.nssctf.cn:28055/", data=post_data, params=get_data)

# 打印响应内容
print(response.text)