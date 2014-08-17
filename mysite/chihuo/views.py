# coding:utf8
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from mysite.chihuo import chihuo
import logging
from django.shortcuts import render_to_response

log = logging.getLogger('django.request')
def query(request):
    try:
        store_name = request.GET['store']
        if store_name is not None:
            return query_pocily(store_name)
    except MultiValueDictKeyError:
        return HttpResponse('无记录')
    
def query_pocily(store_name):
    pocilys = chihuo.query_pocily(store_name)
    return render_to_response('chihuo/query_pocily.html',{'store_name':store_name,'pocilys':pocilys})

if __name__ == '__main__':
    print query_pocily('秀玉')
    log.debug(123)
