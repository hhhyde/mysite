# encoding:utf-8
from django.http import HttpResponse
import logging
from mysite.chihuo import chihuo
from django.shortcuts import render_to_response
from CommonBus.WeChat import WeChat
from django.utils.datastructures import MultiValueDictKeyError
from mysite.chihuo.models import Store
'''
        修改设置默认编码为utf8,因为python的默认编码是ascii,而上面设置的encoding是utf8,不然编码不一样报错
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def wx(request):
    print '/wx Enter'
    wx = WeChat(request)
    if request.method == 'POST':
        print 'post'
        print wx.content
        # store_name = wx.getMsg(request)
        return HttpResponse(wx.send(request, query_pocily(wx.content)), content_type="application/xml")
    elif request.method == 'GET':
        print 'get'
        return HttpResponse(wx.checkSign(request))
'''
这里返回现实给用户看得信息，不用考虑weixin返回数据格式
'''
def query_pocily(store_name):
    try:
        pocilys = chihuo.query_pocily(store_name)
        resp = '<%s>优惠信息如下:\n' % store_name
        i = 0
        for p in pocilys:
            i = i + 1
            resp = resp + '%s.%s\n' % (i, p.detail)
        return resp
    except Store.DoesNotExist:
        return '<%s>的优惠信息还没有被收集，如果您愿意帮忙的话，请点<a href="http://kejt.cn/chihuo/add_store_show?store_name=%s">这里</a>' % (store_name, store_name)
