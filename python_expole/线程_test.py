# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/10/26 10:00
#文件 :线程_test.py

import threading,queue,time,urllib

from urllib import request

baseUrl ='http://www.pythontab.com/html/pythonjichu/'

urlQueue = queue.Queue()

for i in range(2,10):
    url = baseUrl + str(i) + '.html'
    urlQueue.put(url)

def fetchUrl(urlQueue):
    while True:
        try:
            url = urlQueue.get_nowait()
            i=urlQueue.qsize()
        except Exception as e:
            break
        print('Current Thread Name %s, Url:%s'%(threading.current_thread().name,url))

        try:
            response = urllib.request.urlopen(url)
            responseCode = response.getcode()
        except Exception as e:
            continue

        if responseCode==200:
            time.sleep(1)
if __name__=="__main__":
    startTime = time.time()
    threads =[]
    threadNum =int(input("请输入你想要线程数>>>"))
    for i in range(0,threadNum):
        t = threading.Thread(target=fetchUrl,args=(urlQueue,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    endTime = time.time()
    print('Done, Time cost:%s'%(endTime -startTime))

