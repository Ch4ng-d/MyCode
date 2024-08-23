import requests
from bs4 import BeautifulSoup
import re
import time

# 设置目标网址
url = "http://127.0.0.1:60927/"

#建立session会话
session = requests.Session()

# 发起GET请求以获取页面内容
data = {
    'player': 's',  # 使用用户输入的玩家名字
    'direct': "弟子明白"
}
post_response = session.post(url, data=data)


for i in range(5):
    html_content = post_response.text
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取状态中的文本内容
    status_tag = soup.find(id='status')
    status_text = status_tag.text.strip()


    # 用正则表达式提取数字部分
    numbers = re.findall(r'\d+', status_text)

    # 定义数字与方向的映射
    direction_map = {
        '1': '北方',
        '2': '东北方',
        '3': '东方',
        '4': '东南方',
        '5': '南方',
        '6': '西南方',
        '7': '西方',
        '8': '西北方'
        # 根据需要添加更多映射
    }

    # 创建一个描述所有方向和数量的字符串
    response_message = []
    if(len(numbers)==2):
        for number in numbers:
            if number in direction_map:
                direction = direction_map[number]
                response_message.append(f"{direction}一个")
        # 将方向组合成一个字符串，使用逗号连接
        final_message = "，".join(response_message)
        if final_message == "":
            final_message = "没有可说的方位"
    else:
        for number in numbers:
            if number in direction_map:
                direction = direction_map[number]
                response_message.append(f"{direction}")
        final_message="，".join(response_message)

    # 打印最终消息
    print(f"消息内容: {final_message}")

    # 设置POST请求的参数
    data = {
        'player': 's',  # 使用用户输入的玩家名字
        'direct': final_message
    }

    # 发送POST请求
    post_response = session.post(url, data=data)
    print(f"已发送给服务器: {data}，响应状态码: {post_response.status_code}")
    if 'moectf' in post_response.text:
        print(post_response.text)

    # 点击延迟，避免请求频繁
    time.sleep(1)  # 添加延迟，防止请求过于频繁
