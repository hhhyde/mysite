# coding:utf8
from django.db import models
import json
'''
促销策略对象
'''
class Pocily(models.Model):
    '''
        促销策略
    '''
    detail = models.CharField(max_length=255)
    '''
        哪个用户更新的这个
    '''
    by_who = models.CharField(max_length=50)
    '''
        更新时间
    '''
    update_date = models.DateField()
    
    def __unicode__(self):
        return self.detail

'''
商家信息
'''
class Store(models.Model):
    '''
        店名
    '''
    name = models.CharField(max_length=255)
    '''
        关联上促销策略
    '''
    pocilys = models.ManyToManyField(Pocily)
    
    def __unicode__(self):
        return self.name

class PocilyEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

if __name__ == '__main__':
    print 123
