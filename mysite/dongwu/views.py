# coding:UTF-8

from django.http import HttpResponse
from mysite.dongwu.models import Dongwu, DongwuEncoder
import logging
import json

log = logging.getLogger('django.request')
def get(request, num):
    callback = request.GET['dw']
    # 传进来时str类型，不能比较大小，只能看有没有值
    if len(num) == 0:
        num = 15
    num = int(num)  # 这里强转没事，因为进来的只能是数字
    if num > 50:
        num = 50
    dws = Dongwu().__class__.objects.all()[:num]
    ori = [dw for dw in dws]
    return HttpResponse('%s(%s)' % (callback, json.dumps(ori, cls=DongwuEncoder)))
    
if __name__ == '__main__':
    get(3)
