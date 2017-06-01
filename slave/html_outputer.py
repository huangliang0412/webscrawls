# -*- coding: utf-8 -*-
from redis_connect import conn
from urllib import request
import re
import os
import aiofiles, aiohttp

class HtmlOutputer(object):
    #def __init__(self):
    #    self.picture = set()
    '''
    def collect_pic(self, pic):
        for img in pic:
            if img not in self.picture:
                self.picture.add(img)
    '''
    #async def save_file(self):


    def download_pic(self):
        #pic_id = 0
        file_load = '/Users/HLA/PICTURE/youyou'
        if os.path.exists(file_load) is None:
            os.mkdirs('/Users/HLA/PICTURE/')
        #for url_pic in self.picture:
        while conn.llen('pic_url') > 0 :
            url_pic = conn.rpop('pic_url')
            #str(url_pic, encoding= 'utf-8')
            url_pic = url_pic.decode('utf-8')
            #print(type(s))

            async with aiohttp.request('GET', url_pic) as resp:
                content = await resp.text()
            print('uil_pic', url_pic)
            r = re.sub('^http.+img/','', url_pic)
            print(r)
            filename = re.sub('/', '-', r)

            #f = open('../lilisha/'+filename, 'wb')
            #req =request.Request(url_pic)
            #response = request.urlopen(req)

            #buf = response.read()
            f.write(response.read())
            
