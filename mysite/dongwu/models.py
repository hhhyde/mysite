# coding:utf8
from django.db import models
import json

# Create your models here.
class Dongwu(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    details = models.CharField(max_length=2000)
    
    def __unicode__(self):
        return self.title

class DongwuEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Dongwu):
            return '[title:%s, details:%s, url:%s]'%(obj.title,obj.details,obj.url)
        return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    import sys
    print sys.path
