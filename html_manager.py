# -*- coding: utf-8 -*-
'''
使用redis sadd结构直接去重，url管理器将不再需要
'''
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls: 
            self.new_urls.add(url)
        

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return 
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0     #当url列表长度不为0， 说明有新的url列表

    def get_new_url(self):           #在新的url列表中弹出一个url，并放入已有的url列表
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
