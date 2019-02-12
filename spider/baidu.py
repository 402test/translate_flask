import requests
import time
import execjs
import re
import json
class BaiDu(object):
    '''
    百度翻译
    '''
    def __init__(self):
        '''
        headers  请求头
        url  翻译链接
        url_en_ch 返回 语言类型
        '''
        self.headers = {
        'Accept': '* / *',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'BAIDUID=4050F58FA9F9461C0A9CCF3E2A544924:SL=0:NR=10:FG=1;',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        self.url_baidu='http://fanyi.baidu.com'  #  主页
        self.url = 'https://fanyi.baidu.com/v2transapi' #  翻译接口
        self.url_en_ch = 'https://fanyi.baidu.com/langdetect' # 判断类型
        self.data = {
            'from':'zh',
            'to':'en',
            'query':'你好',
            'simple_means_flag': '3',
            'transtype':'realtime',
            'sign': '7604.327301',
        }
    def get_token(self):
        sess = requests.session()
        #   获取  cookie  和  token 的时候     一定要时候session()   不然得到的cookie  和    token 不匹配
        #  使用session   维持访问状态    然后先访问页面  得到cookie   再带着 访问状态(估计是服务器储存的session)   去获取 token

        req_get = sess.get(url=self.url_baidu, headers=self.headers)
        cookie_match = re.findall(r'BAIDUID=[A-Z0-9:=]+;', req_get.headers['Set-Cookie'])
        cookie = cookie_match[0]
        self.headers['Cookie'] = cookie

        req_get =  sess.get(url=self.url_baidu, headers=self.headers)
        token_match = re.findall(r'token: \'([0-9a-z]{32})\',', req_get.text)
        token = token_match[0]
        self.data['token'] = token

    def get_sign(self,value):
        with open("../js/sign.js") as f:
            jsData = f.read()
            sign = execjs.compile(jsData).call("e",value )
        self.data['sign'] = sign

    def run(self,query):
        res = requests.post(self.url_en_ch, headers=self.headers, data={'query': query})
        r_dict = json.loads(res.content.decode('utf-8'))
        self.data['from']=r_dict['lan']
        if r_dict['lan'] != 'zh':
            self.data['to'] = 'zh'       #  英    -- 中
        self.data['query'] = query
        self.get_sign(query)
        #self.data['token'] = 'a0cb75ad0dedd1bee94b138ec44c4648'
        #self.headers['Cookie']  ='BAIDUID=4050F58FA9F9461C0A9CCF3E2A544924:SL=0:NR=10:FG=1;'
        res_trans = requests.post(self.url,headers = self.headers,data= self.data)
        text = res_trans.content.decode('utf-8')
        r_dict = json.loads(text)
        return  r_dict['trans_result']['data'][0]['dst']

if __name__ =='__main__':
    bai = BaiDu()
    #  配置参数
    bai.get_token()
    #  使用
    print(bai.run('刘德华'))

