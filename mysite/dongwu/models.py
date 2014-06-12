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
        return obj.__dict__

if __name__ == '__main__':
    import sys
    print sys.path
