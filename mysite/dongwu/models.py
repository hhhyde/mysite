#coding:utf8
from django.db import models

# Create your models here.
class Dongwu(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    details = models.CharField(max_length=2000)

if __name__=='__main__':
    import sys
    print sys.path