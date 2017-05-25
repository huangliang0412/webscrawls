# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return 

        # response = urllib.urlopen(url)  # the html is downloaded in the local
        req = Request(url)
        response = urlopen(req)
        if response.getcode() != 200:
            return None
        # print (response.read())
        return response.read()

if __name__ == "__main__":
    # url ="www.umei.cc/p/gaoqing/gangtai/15483_3.htm"
    url = "http://www.baidu.com"
    print("hello")
    s = HtmlDownloader()
    print(s.download(url))
