# encoding:UTF8
'''
<吃货>加进后台管理
'''
from django.contrib import admin
from mysite.chihuo.models import Store, Pocily

admin.site.register(Store)
admin.site.register(Pocily)
