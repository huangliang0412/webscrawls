# -*_ coding: utf-8 -*-
import html_parser, html_downloader
    #, html_outputer
from redis_slave_connect import conn
import asyncio
from multiprocessing import Pool
import time
from threading import Thread
class SpiderMain(object):
    def __init__(self):
        #self.urls = html_manager.UrlManager()    #url管理器
        self.downloader = html_downloader.HtmlDownloader()  #url网页下载器
        self.parser = html_parser.HtmlParser()           #url解析器
        #self.outputer = html_outputer.HtmlOutputer()          #url网页输出器
    '''
    def set_rooturl(self, root_url):
        print(root_url)
        root_url1 = root_url
        print(conn.lpush('task_queue', root_url1))
        #print(conn.rpop('task_queue'))
    '''
    #@asyncio.coroutine
    async def craw(self):
        _, page_url = conn.brpop('task_queue')
        print(page_url)
        html_cont = self.downloader.download(page_url)  #下载网页数据
        print(html_cont)
        self.parser.parse(html_cont, page_url) #解析数据，获取新的url和图片



def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

if __name__ == "__main__":
    #p = Pool(2)
    #for i in range(3):
    #root_url = input('Please input url:')
    obj_spider = SpiderMain()

    new_loop = asyncio.new_event_loop()
    t = Thread(target=start_loop, args=(new_loop,))
    #t.setDaemon(True)
    t.start()
    try:
        while True:
            asyncio.run_coroutine_threadsafe(obj_spider.craw(), new_loop)
    except Exception as e:
        print('crawl error')
        new_loop.stop()