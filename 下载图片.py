import os
import requests
import re
s=''
name=0
def get_web(url, fname):
    r = requests.get(url)                             # 返回url请求的数据
    data = r.content
    with  open(fname, 'wb') as fobj:                  # 将数据存储在指定位置
        fobj.write(data)
    return fname
f1=open('0.txt','r+')
a=f1.readline()
s=s+a
b=re.findall(r"com(.+?)png",s)
#print(b)
for c in b :
    url='http://file-1.book118.com'+c+'png'
    name=name+1
    a=''
    a=str(name)+'.png'
    try:
        get_web(url,a)
        print("ok")
    except:
        print("no")
        pass
#print(s)
f1.close()


