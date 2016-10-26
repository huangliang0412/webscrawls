# -*- coding: utf-8 -*-
from urllib import request
#import urllib.request
#from urllib import parse


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return 

        req = request.Request(url)  # the html is downloaded in the local
        #req = Request(url)
        #携带浏览器的头部，防止网站反爬
        req.add_header("User-Agent","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0")
        response = request.urlopen(req)
        if response.getcode() != 200:
            return None
        #print (response.read())
        return response.read()
