# coding:UTF-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from mysite.dongwu.models import Dongwu, DongwuEncoder
import logging
import json

log = logging.getLogger('django.request')
def get(request, num):
    # 传进来时str类型，不能比较大小，只能看有没有值
    if len(num) == 0:
        num = 15
    num = int(num)  # 这里强转没事，因为进来的只能是数字
    if num > 50:
        num = 50
    aa = {'a':1, 'b':2}
    return HttpResponse(json.dumps(Dongwu().__class__.objects.all()[1], cls=DongwuEncoder))
    
