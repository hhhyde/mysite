# coding:UTF8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mysite.jd.models import User
from jingdong import JD
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger('django.request')
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
    display_post = 10
    try:
        display_post = User.objects.get(ip=ip).display_post
    except ObjectDoesNotExist:
        logger.warn("can't found config records by accessing user ip:%s, return default value 10" % ip)
    jd.refresh(item, display_post)
    return render_to_response('jingdong.xml', mimetype="application/xml")

def __get_ip(req):
    if req.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = req.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = req.META['REMOTE_ADDR']
    return ip
    
if __name__ == '__main__':
    print User.objects.get(ip='127.0.0.1').display_post
