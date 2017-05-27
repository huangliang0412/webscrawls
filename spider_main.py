# -*_ coding: utf-8 -*-
import html_parser, html_downloader
    #, html_outputer
from redis_connect import conn
import asyncio
from multiprocessing import Pool
class SpiderMain(object):
    def __init__(self):
        #self.urls = html_manager.UrlManager()    #url管理器
        self.downloader = html_downloader.HtmlDownloader()  #url网页下载器
        self.parser = html_parser.HtmlParser()           #url解析器
        #self.outputer = html_outputer.HtmlOutputer()          #url网页输出器

    #@asyncio.coroutine
    async def craw(self, root_url):
        count = 1
        #self.urls.add_new_url(root_url)            #将url入口地址放入url管理器中
        conn.lpush('task_url', root_url)
        #print(conn.rpop('task_url'))
        #while self.urls.has_new_url():      #如果有新的url地址，程序会一直运行下去
        while conn.llen('task_url') > 0 :
            #try:
                #new_url = self.urls.get_new_url()    #获取一个新的url
                html_cont = await self.downloader.download()  #下载网页数据
                self.parser.parse(html_cont) #解析数据，获取新的url和图片
                #self.urls.add_new_urls(new_urls)  #将新的url放入到url管理器中
                #self.outputer.download_pic()   #下载图片
                count += 1

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


if __name__ == "__main__":
    p = Pool(2)
    #for i in range(3):
    root_url = "http://fuli.asia/luyilu/2016/0703/2146.html"               #入口URL
    #root_url = input('Please input url:')
    obj_spider = SpiderMain()
    obj_spider.main(root_url)
