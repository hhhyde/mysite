#coding:utf8

import urllib2
from bs4 import BeautifulSoup

def getpagelist(url):
    context = urllib2.urlopen(url).read()
    soup = BeautifulSoup(context)
    ul=soup.find('ul',class_='pagelist')
    lastpage=0
    for li in  ul.children:
        if '末页' == li.string:
            #Assert li.a['href'] = 84-30.html,这里只要30
            lastpage=li.a['href'][3:5]
    for i in xrange(1,31):
        get_podcast_by_url('http://dongwu.21cbr.com/84-%s.html'%i)

def get_podcast_by_url(url):
    context = urllib2.urlopen(url).read()
    soup = BeautifulSoup(context)
    div= soup.find('div', id='mainContent_dongwu_mid_left_list')
    #拿到这个div底下ul的所有的a标签
    for a in div.ul.find_all('a'):
        print a

def get_details(url):
    context = urllib2.urlopen(url).read()
    soup = BeautifulSoup(context)
    print soup.find(id='mainContent_dongwu_mid_left_top_title',).string
    print soup.find(id='mainContent_dongwu_mid_left_top_info').contents

if __name__=='__main__':
    #get_podcast_by_url('http://dongwu.21cbr.com/84-1.html')
    #getpagelist('http://dongwu.21cbr.com/84-1.html')
    get_details('http://www.21cbr.com/html/multimedia/audio/201101/24-7952.html')
    
    
    
    
    #<a href="http://www.21cbr.com/html/multimedia/audio/201312/03-16192.html" target="_blank">冬吴相对论第408期:《“出格”的李书福》</a>