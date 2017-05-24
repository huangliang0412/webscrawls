#!/usr/bin/env python3
import requests
import random
'''
#r = requests.get('http://www.baidu.com')
proxies = {
    "http": "94.228.207.233:8085",
    #"https": "94.228.207.233:8085",
}
r = requests.get('http://www.baidu.com', proxies = proxies)
print(r.status_code)
print(r.headers)
#r.encoding = 'utf-8'


response = requests.get('http://')
print(response.status_code)
print(response.elapsed.microseconds)
#print(response.text)
proxy = set()
for ip in response.text.split():
    #print(ip)
    proxy.add(ip)

print(len(proxy))
'''
class ProxyIpPoll(object):
    def __init__(self):
        self.available_proxyips = set()
        self.all_proxyips = set()

    def get_new_proxyips(self):
        #try:
        response = requests.get('http://api.xicidaili.com/free2016.txt')
        for ip in response.text.split():
            self.all_proxyips.add(ip)

        print(len(self.all_proxyips))
        #except:
            #print('require ip error')

    def check_ip_available(self):
        test_url = 'http://www.baidu.com'
        timeout = 5
        print(len(self.all_proxyips))
        for ip in self.all_proxyips:
            try:
                proxies = {
                    'https': ip,
                }
                response = requests.get(test_url, proxies = proxies, timeout = 5)
                print(response.elapsed.microseconds)
                self.available_proxyips.add(ip)
                print('%s is available' % ip)

            except:
                print('%s is not available' % ip)

    def get_available_proxyipool(self):
        self.get_new_proxyips()
        self.check_ip_available()

    def get_random_proxyip(self):
        return random.choice(self.available_proxyips)

if __name__ == '__main__':
    ippool = ProxyIpPoll()
    ippool.get_available_proxyipool()
    #ippool.get_new_proxyips()








