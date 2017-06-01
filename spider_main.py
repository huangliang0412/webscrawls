# -*_ coding: utf-8 -*-
import html_parser, html_downloader, html_outputer
from proxyip_pool import ProxyIpPoll
from redis_connect import conn
import asyncio, os
from multiprocessing import Pool
import time
from threading import Thread
class SpiderMain(object):
    def __init__(self):
        #self.urls = html_manager.UrlManager()    #url管理器
        self.downloader = html_downloader.HtmlDownloader()  #url网页下载器
        self.parser = html_parser.HtmlParser()           #url解析器
        self.outputer = html_outputer.HtmlOutputer()          #url网页输出器

    def set_rooturl(self, root_url):
        print(root_url)
        root_url1 = root_url
        print(conn.lpush('task_queue', root_url1))
        #print(conn.rpop('task_queue'))

    #@asyncio.coroutine
    async def craw(self):
        page_url = conn.brpop('task_queue')
        print(page_url)
        #self.urls.add_new_url(root_url)            #将url入口地址放入url管理器中
        #conn.lpush('task_url', root_url)
        #print(conn.rpop('task_url'))
        #while self.urls.has_new_url():      #如果有新的url地址，程序会一直运行下去
        #while conn.llen('task_url') > 0 :
        #while True:
        #try:
        #new_url = self.urls.get_new_url()    #获取一个新的url
        html_cont = self.downloader.download(page_url)  #下载网页数据
        print(html_cont)
        #time.sleep(10)
        self.parser.parse(html_cont, page_url) #解析数据，获取新的url和图片
        #self.urls.add_new_urls(new_urls)  #将新的url放入到url管理器中
        self.outputer.download_pic()   #下载图片

            #except:
                #print("craw failed")

    def main(self, root_url):
        asyncio.ensure_future(self.craw(root_url))

        loop = asyncio.get_event_loop()
        try:
            loop.run_forever()
        except KeyboardInterrupt as e:
            asyncio.gather(*asyncio.Task.all_tasks().cancel())
            loop.stop()
            loop.run_forever()
        finally:
            loop.close()

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def child_process():
    proxy_ippool = ProxyIpPoll()
    proxy_ippool.get_available_proxyipool()
    while True:
        time.sleep(15*60)  # 每15分钟更新一次
        proxy_ippool.updata_proxyippool()

if __name__ == "__main__":
    #p = Pool(2)
    #for i in range(3):
    pid = os.fork()
    if pid == 0:        #新开一个子线程，专门管理IP代理池
        child_process()
    else:
        root_url = 'http://fuli.asia/luyilu/2016/0703/2146.html'               #入口URL
        obj_spider = SpiderMain()
        obj_spider.set_rooturl(root_url)

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