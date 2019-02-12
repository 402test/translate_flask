import requests
import json
import time
class MeiyouDao(object):
    '''
    有道翻译  接受带翻译内容  返回结果
    '''
    def __init__(self):
        self.url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        self.data = {"i": "你好",
                "from":"AUTO",
                "to":"AUTO",
                "smartresult":"dict",
                "client":"fanyideskweb",
                "salt":"1540373170893",
                "sign":"a5d9b838efd03c9b383dc1dccb742038",
                "doctype":"json",
                "version":"2.1",
                "keyfrom":"fanyi.web",
                "action":"FY_BY_REALTIME",
                "typoResult":"false"
            }
    def run(self,key):
        '''
        :param key:  待翻译内容
        :return: 翻译后的结果
        '''
        self.data['i'] = key
        for i in range(3):
            try:
                res = requests.post(self.url,data=self.data,headers = self.headers)
                if res.status_code == 200:
                    break
            except Exception as e:
                print('发生错误',e)
                time.sleep(1)
                continue
        text = res.content.decode('utf-8')
        r_dict = json.loads(text)
        result = r_dict['translateResult'][0][0]["tgt"]
        return result
if __name__ == '__main__':
    yy = MeiyouDao()
    print(yy.run('大家好，我是渣渣辉'))




# # 请输入你要翻译的内容
# key = input("请输入要翻译的内容:")
# # post方法要求data为字典格式
# data = {"i": key,
#         "from":"AUTO",
#         "to":"AUTO",
#         "smartresult":"dict",
#         "client":"fanyideskweb",
#         "salt":"1540373170893",
#         "sign":"a5d9b838efd03c9b383dc1dccb742038",
#         "doctype":"json",
#         "version":"2.1",
#         "keyfrom":"fanyi.web",
#         "action":"FY_BY_REALTIME",
#         "typoResult":"false"
#     }
#
# # 发请求,获取响应
# # url为POST的地址,抓包工具抓到的,此处去掉 _o
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
# headers = {"User-Agent":"Mozilla/5.0"}
# # 此处data为form表单数据
# res = requests.post(url,data=data,headers=headers)
# res.encoding = "utf-8"
# html = res.text
# # 把json格式字符串转换为Python中字典
# r_dict = json.loads(html)
# result = r_dict['translateResult'][0][0]["tgt"]
# print(result)

