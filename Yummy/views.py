#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User
import json
import hashlib



#注册
def regist(request):
    flag = 0
    fail_reson = 0
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        try:
            User.objects.create(user_name= received_json_data['user_name'],
                                password=hashlib.sha1(received_json_data['password']).hexdigest(),
                                tel=received_json_data['tel'],
                                addr=received_json_data['addr'],
                                name= received_json_data['name'],
                                QQ= received_json_data['QQ'],
                                wechat= received_json_data['wechat'])
            flag = 1
        except:
            fail_reson = 1
    if flag == 0:
        response_data = json.dumps({'flag':flag, 'fail_reson':fail_reson})
        return HttpResponse(response_data)
    else:# 自动登陆
        return login(request)
#登陆
def login(req):
    if req.method == 'POST':
        received_json_data = json.loads(req.body)

        #获取表单用户密码
        username = received_json_data['user_name']
        password = hashlib.sha1(received_json_data['password']).hexdigest()
        #获取的表单数据与数据库进行比较
        user = User.objects.filter(user_name__exact = username,password__exact = password)
        if user:
            #比较成功，跳转index
            response = HttpResponseRedirect('/index/')
            #将username写入浏览器cookie,失效时间为3600
            response.set_cookie('username',username,3600*24)
            user_id = User.objects.get(user_name=username).values('user_id').first() # 查询user_name的id
            tel = User.objects.get(user_name=username).values('tel').first()
            addr = User.objects.get(user_name=username).values('addr').first()
            name = User.objects.get(user_name=username).values('name').first()
            QQ = User.objects.get(user_name=username).values('QQ').first()
            wechat = User.objects.get(user_name=username).values('wechat').first()
            response.set_cookie('user_id',user_id,3600*24)
            response.set_cookie('tel',tel,3600*24)
            response.set_cookie('addr',addr,3600*24)
            response.set_cookie('name',name,3600*24)
            response.set_cookie('QQ', QQ,3600*24)
            response.set_cookie('wechat', wechat,3600*24)
            return response
        else:
            #比较失败，还在login
            response_data = json.dumps({'flag':0, 'fail_reson':1})
            return HttpResponse(response_data)
#登陆成功跳转网页
def index(req):
    username = req.COOKIES.get('username','')
    user_id = req.COOKIES.get('user_id','')
    tel = req.COOKIES.get('tel','')
    addr = req.COOKIES.get('addr','')
    name = req.COOKIES.get('name','')
    QQ = req.COOKIES.get('QQ','')
    wechat = req.COOKIES.get('wechat','')
    return render_to_response('index.html' ,{'username':username,'user_id':user_id,'tel':tel,'addr':addr,'name':name,'QQ':QQ,'wechat':wechat})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response