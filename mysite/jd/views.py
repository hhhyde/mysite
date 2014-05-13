# coding:UTF8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mysite.jd.models import User
from jingdong import JD

def save(request):
    user = User()
    user.ip = __get_ip(request)
    if request.GET.has_key('display_post'):
        display_post = request.GET['display_post']
        user.display_post = display_post
    user.save()
    return HttpResponse(user.ip)

def getRelByItem(request, item):
    jd = JD()
    ip = __get_ip(request)
    jd.refresh(item, User.objects.get(ip=ip).display_post)
    return render_to_response('jingdong.xml', mimetype="application/xml")

def __get_ip(req):
    if req.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = req.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = req.META['REMOTE_ADDR']
    return ip
    
if __name__ == '__main__':
    print User.objects.get(ip='127.0.0.1').display_post
