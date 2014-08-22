# coding:utf8
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from mysite.chihuo import chihuo
import logging
from django.shortcuts import render_to_response
from mysite.chihuo.models import Store, Pocily

log = logging.getLogger('django.request')
def query(request):
    try:
        store_name = request.GET['store']
        if store_name is not None:
            return query_pocily(store_name)
    except MultiValueDictKeyError:
        return HttpResponse('无记录')
    
def query_pocily(store_name):
    try:
        pocilys = chihuo.query_pocily(store_name)
    except Store.DoesNotExist:
        return '无此记录'
    return render_to_response('chihuo/query_pocily.html',{'store_name':store_name,'pocilys':pocilys})

def add_store_show(request):
    store_name = request.GET['store_name']
    return render_to_response('chihuo/add_store.html',{'store_name':store_name})

def add_store_submit(request):
    store_name = request.GET['store_name']
    detail = request.GET['detail']
    store=Store()
    pocily=Pocily()
    store.name=store_name
    pocily.detail=detail
    pocily.by_who='System'
    pocily.update_date='2014-08-23'
    pocily.valid=False
    pocily.save()
    store.save()
    store.pocilys.add(pocily)
    return HttpResponse('OK!')

if __name__ == '__main__':
    print query_pocily('秀玉')
    log.debug(123)

