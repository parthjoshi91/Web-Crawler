__author__ = 'parthdhj'
import requests
from bs4 import BeautifulSoup
import time
from sys import exit
import MySQLdb
t= time.time()
start_t=t
t+=600
base_url="http://mashable.com"
def webcrawler(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    head=soup.head
    url_link=""
    title=""
    image=""
    description=""
    for l in head.findAll('link'):
        rel=l.get('rel')
        #print(rel)
        if rel==['canonical']:
            url_link=l.get('href')
            #print(url_link)
    if url_link=='':
        return
    for link in head.findAll('meta'):
        prop=link.get('property')
        nam=link.get('name')
        #print(prop)
        if prop == 'og:title':
            title=link.get('content')
            #print(title)
        if prop =='og:description':
            description=link.get('content')
            #print(description)
        if nam =='sailthru.image.thumb':
            image=link.get('content')
            #print(image)
    db = MySQLdb.connect("ec2-52-10-122-11.us-west-2.compute.amazonaws.com", "root", "", "test")
    cursor = db.cursor()
    query="SELECT * FROM t_data WHERE Url = '%s'"%(url_link)
    cursor.execute(query)
    n=cursor.rowcount
    if (n>0):
        pass
        db.close()
        print('not included')
    else:
        d=(url_link, title, description, image)
        sql="INSERT INTO t_data (Url,Title,Description,Image) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, d)
            if time.time()<t:
                db.commit()
                db.close()
                print("ok")
            else:
                print(time.time()-start_t)
                db.close()
                exit(0)
        except:
            db.rollback()
            db.close()
            print('rollback')
        body=soup.find("div",{"id":"body"})
        if body!=None:
            for link in body.findAll('a'):
                href=str(link.get('href'))
                if href!= None:
                    if href!='':
                        if href[0:19]=='http://mashable.com':
                            print('present')
                            if time.time()<t:
                                print(href)
                                webcrawler(href)
                            else:
                                print(time.time()-start_t)
                                exit(0)
                        if href[0]=='/':
                            l=base_url+href
                            if time.time()<t:
                                print(l)
                                webcrawler(l)
                            else:
                                print(time.time()-start_t)
                                exit(0)



webcrawler(base_url)
(time.time()-start_t)
