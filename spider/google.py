# encoding: utf-8
__author__ = 'ChengweiHuang'
__date__ = '2019/1/31 9:58'
import execjs
import re
import requests
class Google_tran(object):
    def __init__(self):

        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }

    def get_tk(self,value):
        with open("../js/to_tk.js") as f:
            jsData = f.read()
            self.tk = execjs.compile(jsData).call("TL", value)

    def run(self,value):
        self.get_tk(value)
        url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=%s&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=gt&pc=1&otf=2&ssel=0&tsel=3&kc=3&tk=%s&q=%s'

        if re.search('[A-Za-z]',value):
            url = url%('zh-CN',self.tk,value)
        else:
            url = url%('en-CN',self.tk,value)
        res = requests.get(url,headers = self.headers)
        return re.findall('\[\[\["(.*?)"',res.text)[0]


if __name__ == '__main__':
    goo = Google_tran()
    print(goo.run('i am tony'))