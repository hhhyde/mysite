# encoding:utf-8
from django.http import HttpResponse
import logging
from django.shortcuts import render_to_response
from CommonBus.WeChat import WeChat
from django.utils.datastructures import MultiValueDictKeyError

def wx(request):
    print '/wx Enter'
    wx = WeChat()
    if request.method == 'POST':
        print 'post'
        return HttpResponse(wx.getMsg(request), content_type="application/xml")
    elif request.method == 'GET':
        print 'get'
        return HttpResponse(wx.checkSign(request))
