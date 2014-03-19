#coding:UTF8
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from mysite.jd.models import User

def save(request):
    user=User()
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip=request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip=request.META['REMOTE_ADDR']
    user.ip=ip
    if request.GET.has_key('display_post'):
        display_post=request.GET['display_post']
        user.display_post=display_post
    user.save()
    return HttpResponse(ip)

def getRelByItem(request, item):
    jd = JD()
    lnk = jd.refresh(item)
    return render_to_response('jingdong.xml', mimetype="application/xml")