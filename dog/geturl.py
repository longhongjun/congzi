# -*-coding=utf-8-*-
import urllib
import re
import hashlib
import redis

from simhash import Simhash

url = 'http://boluojishi.com'
r = redis.Redis(host='pub-redis-14830.us-east-1-2.1.ec2.garantiadata.com', port=14830, password='ydf123456', db=0)

def get_html(url):
    hashurl = hashlib.md5(url).hexdigest()
    if r.get(hashurl):
        return None
    html = urllib.urlopen(url)
    if 'text' in html.headers.type:
        data = html.read()
        hashdata = Simhash(data).value
        r.set(hashurl,hashdata)
        return data
    else:
        pass


def pipeiurl(data):
     urlall = re.findall(r'http://[\w|\.|/]+(?=\")',data)
     b = set(urlall)
     return b

def starturl(url):
    data = get_html(url)
    if data:
        urls = pipeiurl(data)
        if len(urls):
            for url in urls:
                if 'boluojishi' in url:
                    starturl(url)
        else:
            print 'no url'




if __name__ == '__main__':
    #starturl(url)
    #dir(r)
    #get_html('http://www.baidu.com')
    print r.dbsize()
    r.flushall()


    
    #print (Simhash('How are you? I am fine. Thanks.').value - Simhash('How are u? I am fine.     Thanks.').value)
    #a = Simhash('aabbc').distance(Simhash('aabba'))
    #print a
