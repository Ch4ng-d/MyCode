import json

# 假设你的 JSON 数据保存在 json_data 变量中
json_data = '''  
{  
   #抓包抓到的账号
}  
'''

# 解析 JSON 数据
data = json.loads(json_data)

# 初始化一个数组以存储提取的数字
name_numbers = []

# 提取 'name' 字段的数字并加入到数组中
change_un_sign_list = data.get("data", {}).get("changeUnSignList", [])
for item in change_un_sign_list:
    name = item.get("name")
    if name is not None:  # 确保 name 不为 None
        name_numbers.append(int(name))  # 将 name 转换为整数并加入数组

# 输出结果
print(name_numbers)