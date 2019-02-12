from spider import *
from flask import Flask, render_template, request
from threading import Thread
import json
app = Flask(__name__)
dic = {}
def main(value):
    '''
    多线程访问4个翻译界面 返回结果
    :param value:
    :return:
    '''
    L = ['baidu', 'google', 'sll', 'youdao']
    L_Thread = []
    for i in L:
        t = Thread(target=translate_fun,args=(value,i))
        t.start()
        L_Thread.append(t)
    for j in L_Thread:
        j.join()

def translate_fun(value,name):
    global dic
    if name == 'baidu':
        example = baidu.BaiDu()
        example.get_token()
        dic['baidu']= example.run(value)
    if name == 'google':
        example = google.Google_tran()
        dic ['google']= example.run(value)
    if name =='sll':
        example = sll.SanLiuLing()
        dic ['sll']= example.run(value)
    if name == 'youdao':
        example = youdao.MeiyouDao()
        dic ['youdao']=example.run(value)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/translate')
def translate_view():

    value = request.args.get('data')
    main(value)

    json_value = json.dumps(dic)
    print(json_value)
    return json_value

if __name__ == "__main__":
    app.run(debug=True)
