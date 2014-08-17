# encoding:utf-8
from django.http import HttpResponse
import logging
from mysite.chihuo import chihuo
from django.shortcuts import render_to_response
from CommonBus.WeChat import WeChat
from django.utils.datastructures import MultiValueDictKeyError
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
        return HttpResponse(wx.send(request,query_pocily(wx.content)), content_type="application/xml")
    elif request.method == 'GET':
        print 'get'
        return HttpResponse(wx.checkSign(request))
 
def query_pocily(store_name):
    resp = '<%s>优惠信息如下:\n' % store_name
    pocilys = chihuo.query_pocily(store_name)
    i = 0
    for p in pocilys:
        i= i+1
        resp = resp + '%s.%s\n' % (i, p.detail)
    return resp