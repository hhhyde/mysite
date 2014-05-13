# coding:UTF8
'''
Created on 2013-9-21

@author: Chris
'''
class JD(object):
    '''
        
    '''
    def __init__(self):
        pass
    def __getId(self, url):
        '''
                        拿到Item.
        '''
        return url.split('/')[-1][:-5]

    def __getUrl(self, url):
        id = self.__getId(url)
        '''
                        默认按点击数来排序，
        这里1-1-4的意义如下：
        1：取第1页的链接，同理3是第三页
        1：按回复数排序，0是时间，2是点击数
        4：晒单贴标签，0是网友讨论贴，1是讨论贴，2是问答贴，3是圈子贴
        '''
        return 'http://club.jd.com/bbs/%s-1-1-4.html' % id
    
    def __getCont(self, url):
        orilnk = self.__getUrl(url)
        import urllib2
        return urllib2.urlopen(orilnk).read().decode('gbk', 'ignore').encode('utf8')
    
    def __makeUrlByItem(self, item):
        return 'http://item.jd.com/%s.html' % item
    
    def __getRelationItem(self, item, topNum=40):
        '''
            topNum默认是40，因为京东上面一个页面就显示有60个晒单帖链接，
                            按照html排序1-40是当前页面显示的40个，后面20个是热度排行(
                            某一个商品的所有晒单链接页面都会显示)，所以去掉
        '''
        url = self.__makeUrlByItem(item)
        cont = self.__getCont(url)
        import re
        p = re.compile(r'http://club.jd.com/bbsDetail/.*_1.html')
        # 一共有60个，但是后面20个是热门排行，先不管
        return p.findall(cont)[:topNum]
    
    def __generateXml(self, urls):
        print urls
        import xml.dom.minidom, os
        impl = xml.dom.minidom.getDOMImplementation()
        dom = impl.createDocument(None, 'tasks', None)
        root = dom.documentElement
        for url in urls:
            employee = dom.createElement('task')
            employee.setAttribute('href', url)
            root.appendChild(employee)
        pass
        xmlpath = os.path.join(os.path.dirname(__file__), '../templates/jingdong.xml').replace('\\', '/')
        f = open(xmlpath, 'w')
        dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
        f.close() 
    
    def refresh(self, item, display_post):
        print item
        self.__generateXml(self.__getRelationItem(item)[:display_post])
    
if __name__ == '__main__':
    jd = JD()
    print jd.refresh(841637)
#    xml=open('../templates/jingdong.xml')
#    print xml.read()
