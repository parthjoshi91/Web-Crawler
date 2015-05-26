__author__ = 'parthdhj'
import requests
from bs4 import BeautifulSoup
import time
from sys import exit
import MySQLdb
t= time.time()
start_t=t
t+=600
def webcrawler(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('h1'):
            href=link.a
            if href!= None:
                if time.time()<t:
                    get_single_post_data(str(href.get('href')))
                else:
                    #print(time.time()-start_t)
                    exit(0)
    for link in soup.findAll('li',{'class':'collapsable channel submenu'}):
        href=link.a
        #new_link= "http://mashable.com" + href.get('href')
        #if time.time()<t:
            #new_link_post_data(new_link)
        #else:
            #print(time.time()-start_t)
            #exit(0)
        d_tag = link.get('data-tags')
        s=d_tag.split(',')
        if href.text == 'Social Media':
                pass
        else:
            for l in s:
                new_l="http://mashable.com/" + l
                #print(new_l)
                if time.time()<t:
                     new_link_post_data(new_l)
                else:
                    #print(time.time()-start_t)
                    exit(0)





def get_single_post_data(url):
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
            #print('not included')
        else:
            d=(url_link, title, description, image)
            sql="INSERT INTO t_data (Url,Title,Description,Image) VALUES (%s, %s, %s, %s)"
            try:
                cursor.execute(sql, d)
                if time.time()<t:
                    db.commit()
                    #print("ok")
                else:
                    #print(time.time()-start_t)
                    exit(0)
            except:
                db.rollback()




def new_link_post_data(url):
    #print(url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('h1'):
            href=link.a
            if href!= None:
                if time.time()<t:
                    get_single_post_data(str(href.get('href')))
                else:
                    #print(time.time()-start_t)
                    exit(0)





webcrawler('http://mashable.com')
print(time.time()-start_t)
