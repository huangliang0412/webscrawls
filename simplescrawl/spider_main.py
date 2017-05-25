# -*_ coding: utf-8 -*-
import html_manager, html_parser, html_downloader, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = html_manager.UrlManager()    #url管理器
        self.downloader = html_downloader.HtmlDownloader()  #url网页下载器
        self.parser = html_parser.HtmlParser()           #url解析器
        self.outputer = html_outputer.HtmlOutputer()          #url网页输出器

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)            #将url入口地址放入url管理器中
        while self.urls.has_new_url():      #如果有新的url地址，程序会一直运行下去
            try:
                new_url = self.urls.get_new_url()    #获取一个新的url
                print("craw %d : %s" %(count, new_url))
                html_cont = self.downloader.download(new_url)  #下载网页数据
                new_urls, new_pics = self.parser.parse(new_url, html_cont) #解析数据，获取新的url和图片
                #print(new_urls)
                #print(new_pics)
                self.urls.add_new_urls(new_urls)  #将新的url放入到url管理器中
                self.outputer.collect_pic(new_pics)   #收集新的图片
                self.outputer.download_pic()
                count += 1

            except:
                print("craw failed")

if __name__ == "__main__":
    root_url = "http://www.umei.cc/p/gaoqing/gangtai/15483.htm"               #入口URL
    #root_url = input('Please input url:')
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
