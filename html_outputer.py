# -*- coding: utf-8 -*-
from urllib import request
import re
import os
#from urllib.request import urlopen
#from urllib.request import Request

class HtmlOutputer(object):
    def __init__(self):
        self.picture = set()

    def collect_pic(self, pic):
        for img in pic:
            if img not in self.picture:
                self.picture.add(img)

    def download_pic(self):
        #pic_id = 0
        #file_load = '/home/huanglinag/PICTURE/youyou'
        #os.mkdir('/home/huangliang/PICTURE/youyou')
        for url_pic in self.picture:
            r = re.sub('^http.+img','', url_pic)
            filename = re.sub('/', '-', r)
            f = open('/home/huangliang/PICTURE/youyou/'+filename, 'wb')
            req =request.Request(url_pic)
            response = request.urlopen(req)
            #buf = response.read()
            f.write(response.read())
            
