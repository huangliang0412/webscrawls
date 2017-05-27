# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
from redis_connect import conn
#import urllib.parse
from urllib.parse import urljoin
class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', target="_blank", href=re.compile("^2146.+html$"))
        # links = soup.find_all('a')
        print(links)
        for link in links:
            new_url = link['href']
            print(new_url)
            rooturl = 'http://fuli.asia/luyilu/2016/0703/2146.html'
            #new_full_url = "http://www.umei.cc" + new_url
            new_full_url = urljoin(rooturl, new_url) #join two urls
            new_urls.add(new_full_url)
            conn.lpush('task_url', new_full_url)
            print(new_full_url)
            #return new_urls

    def _get_new_pics(self, page_url, soup):
        new_pics = set()
        pics = soup.find_all('img', alt="推女郎李丽莎VIP无圣光")
        for pic in pics:
            #img = pic.find('img')
            picture = pic['src']
            #print(picture)
            print(picture)
            conn.lpush('pic_url', picture)
            #new_pics.add(picture)
            #return new_pics

    def parse(self, html_cont):
        #print(html_cont)
        page_url = conn.rpop('task_url')
        print('page_url',page_url)
        #if page_url is None or html_cont is None:
        if  html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gbk')
        print(soup)
        self._get_new_urls(page_url, soup)
        self._get_new_pics(page_url, soup)
        #HtmlParser.url_redis.lpush('task_url', new_urls)
        #HtmlParser.url_redis.lpush('pic_url', new_pics)
        #return new_urls, new_pics

    
