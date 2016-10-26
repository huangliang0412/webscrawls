# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
#import urllib.parse
#from urllib.parse import urljoin
class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href = re.compile(r'^/p/gaoqing.+\.htm$'))
        #links = soup.find_all('a')
        #print(links)
        for link in links:
            new_url = link['href']
            print(new_url)
            new_full_url = "http://www.umei.cc" + new_url
            #new_full_url = urljoin("www.umei.cc", new_url) #join two urls
            new_urls.add(new_full_url)
            #print(new_full_url) 
        return new_urls

    def _get_new_pics(self, page_url, soup):
        new_pics = set()
        pics = soup.find_all('div', class_="ImageBody")
        for pic in pics:
            img = pic.find('img')
            picture = img.get('src')
            print(picture)
            new_pics.add(picture)

        return new_pics

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
        #print(soup)
        new_urls = self._get_new_urls(page_url, soup)
        new_pics = self._get_new_pics(page_url, soup)
        return new_urls, new_pics

    
