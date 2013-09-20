# coding:UTF8
'''
Created on 2013-9-21

@author: Matthew
'''
class JD(object):
    def __init__(self):
        pass
    def getId(self, url):
        return url.split('/')[-1][:-5]

    def getUrl(self, url):
        id = self.getId(url)
        '''
            默认按点击数来排序
        '''
        return 'http://club.jd.com/bbs/%s-3-1-4.html' % id
    
    def getCont(self, url):
        orilnk = self.getUrl(url)
        import urllib2
        return urllib2.urlopen(orilnk).read().decode('gbk', 'ignore').encode('utf8')
    
    def makeUrlByItem(self, item):
        return 'http://item.jd.com/%s.html' % item
    
    def getRelationItem(self, item):
        url=self.makeUrlByItem(item)
        cont = self.getCont(url)
        import re
        p = re.compile(r'http://club.jd.com/bbsDetail/.*_1.html')
        # 一共有60个，但是后面20个是热门排行，先不管
        return p.findall(cont)[:40]
    
if __name__ == '__main__':
    # print
    jd = JD()
#    a = jd.getRelationLnk('http://item.jd.com/404379.html')[:10]
#    print a
#    for temp in a:
#        print temp
    print jd.getRelationItem(1008557703)