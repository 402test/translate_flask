import re
import requests
import json
class SanLiuLing(object):
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }

    def run(self,value):
        url = 'http://fanyi.so.com/index/search?query=%s&eng=%s&ignore_trans=0'
        if re.search('[A-Za-z]',value):
            value = str(value).replace(' ','+')
            url = url%(value,'1')
        else:
            url = url%(value,'0')
        res = requests.post(url,headers = self.headers)
        r_dict = json.loads(res.text)
        return r_dict['data']['fanyi']
        #ddd = re.findall('"fanyi":"(.*?)"}',res.text)[0]
        #print(ddd)


if __name__ == '__main__':
    sll = SanLiuLing()
    print(sll.run("我流血过多而死。"))