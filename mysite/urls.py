# encoding:utf-8
from django.conf.urls import patterns, include, url
from mysite.views import (hello, welcome, error, current_datetime, search,
books_by_publisher, author_detail, author_list_plaintext,
my_image, unruly_passengers_csv, hello_pdf, hello_cStringIO, login, index, modifyBookName, test_cookie, showascii, wx, ltc, reminder, jqgrid, dw)
from mysite.jd import views as jd_views
from mysite.dongwu import views as dw_views
from mysite.books.views import about_pages
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
admin.autodiscover()

from django.conf.urls import *
# from django.views.generic import list_detail
# from django.views.generic.simple import direct_to_template
from mysite.books.models import Publisher, Book
# from mysite.feeds.latestEntries import LatestEntries#, LatestEntriesByCategory

def getbooks():
    return Book.objects.all()

publisher_info = {
                'queryset':Publisher.objects.all(),
                'template_name':'publisher_list_page.html',
                'template_object_name':'publisher',  # 默认是object_list,在模板中，通用视图会在template_object_name变量后面加上_list的方式创建变量名
                'extra_context':{'book_list':getbooks},  # Book.objects.all()只会调用一次,所以只能通过回调(callback)来代替一个变量,一种是在上面定义一个方法,这里调用,或者Book.objects.all这么写,不加括号代表是一个函数的引用
                }
book_info = {
                'queryset':Book.objects.order_by('-publication_date'),
#                'template_name':'book_list.html', #如果不写这句,它会默认在books文件夹底下去找模板
                'extra_context':{'description':'按出版日期排序'}
                }
# feeds = {
#         'latest':LatestEntries,
# #         'categories':LatestEntriesByCategorys
#         }

info_dict = {
           'queryset':Book.objects.all(),
           'date_field':'publication_date',
           }

sitemaps = {
          'flatpages':FlatPageSitemap,
          'book':GenericSitemap(info_dict, priority=0.6),
          }

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^/*admin/', include(admin.site.urls)),  # 多个/都可以访问admin页面
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^s/$', search),
#     (r'^about/$', direct_to_template, {'template':'about.html'}),
    (r'^about/(\w+)$', about_pages),
#     (r'^publishers/$', list_detail.object_list, publisher_info),
#     (r'^books/$', list_detail.object_list, book_info),
    (r'^books/(\w+)$', books_by_publisher),
    (r'^authors/(?P<author_id>\d+)/$', author_detail),
    (r'^ap$', author_list_plaintext),
    (r'^aa$', my_image),
    (r'^unruly$', unruly_passengers_csv),
    (r'^hello$', hello_pdf),
    (r'^hello_cStringIO$', hello_cStringIO),
#   (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict':feeds}),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps':sitemaps}),
    (r'^sitemap-(?P<section>.+).xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps':sitemaps}),
    (r'^login$', login),
    (r'^index$', index),
    (r'^book/(?P<id>.*)/(?P<title>.*)$', modifyBookName),
    (r'^test_cookie$', test_cookie),
    (r'^ascii$', showascii),
    (r'^ltc$', ltc),
    (r'^jqgrid$', jqgrid),
    (r'^ltc/(?P<reminder>.*)$', reminder),

    # 默认欢迎页
     url('^$', welcome),
    # 没有/s用.代替
#     url('^.*/$', error),没作用了被 根目录下的404.html 取代了(只能在DEBUG设置为False时可用)
)
# 主要加上微信(wx)相关的url配置
urlpatterns += patterns('',
    (r'^wx$', wx),
    (r'^wx/1$', hello),
)
# 主要加上京东(jd)相关的url配置
urlpatterns += patterns('',
    (r'^jd/save$', jd_views.save),
    (r'^jd/getRelByItem/(?P<item>.*)$', jd_views.getRelByItem),
)
# 主要加上冬吴的相关的url配置
urlpatterns += patterns('',
    (r'^dw/(?P<num>\d{0,})$', dw_views.get),
)
