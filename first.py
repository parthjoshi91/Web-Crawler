import requests
from bs4 import BeautifulSoup
import time
import os
from pyvirtualdisplay import Display
from selenium import webdriver
import MySQLdb
def trade_spider():
        url = 'http://mashable.com'
        display = Display(visible=0, size=(1024, 768))
        display.start()
        driver = webdriver.Firefox()
        driver.get(url)
        t= time.time()
        t+=600
        while time.time()<t:
            print (t)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        soup = BeautifulSoup(data)
        for link in soup.findAll('h1'):
            href=link.a
            if href!= None:
                       get_single_post_data(str(href.get('href')))
        driver.close()
        display.stop()


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
            #print(prop)
            if prop == 'og:title':
                title=link.get('content')
                #print(title)
            if prop =='og:description':
                description=link.get('content')
                #print(description)
            if prop =='og:image':
                image=link.get('content')
                #print(image)
        db = MySQLdb.connect("ec2-52-10-122-11.us-west-2.compute.amazonaws.com", "root", "", "test")
        cursor = db.cursor()
        d=(url_link, title, description, image)
        sql="INSERT INTO t_data (Url,Title,Description,Image) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, d)
            db.commit()
            print("ok")
        except:
            db.rollback()




trade_spider()




