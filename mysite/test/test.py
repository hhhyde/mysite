#encoding:UTF-8
import os
import sys
import csv

sys.path.append('e://eclipse/mysite') #项目路径
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings' #项目名的settings 放进django设置模块

from mysite.books.models import Book, Publisher, Author
b = Book.objects.get(id = 4)
print b
print b.publisher.url

print b.authors.all()

p = Publisher.objects.get(name = '人民文学出版社')
print p.book_set.all()

p1 = p.book_set.filter(title__icontains = '观音')#icontains是忽略大小写的 contains是比较大小写的
print p1

a = Author.objects.get(first_name = '大卫')
print a.book_set.all()

print (str)(Book.me_objects.title_count('中')) + '本符合条件的书'

L = (1, 2, 3, 4, 5)
def aa(self, self1):
    return self * self1
L1 = (2, 3, 4, 5, 6)
print tuple(map(aa, L, L1))#一个对应一个放入aa里面并返回一个list，然后被转成tuple

print Book.objects.all()
print Book.me_objects.querybook()
print Book.me_objects.querybook(2)
print Book.me_objects.querybook()
print Author.objects.all()
print Publisher.objects.all()
print Author.objects.all().model._meta.verbose_name
print Author.objects.all().filter(pk = 3).get()

a = ['1', '2', '3', '4']
for aa in a:
    print aa

def linefeed(self):
    return '\n' + self

print map(linefeed, a)


#s = open(r'C:\Users\ke\Desktop\22.txt', 'rb').read()

#print unicode(s, 'gbk')

a = []
b = ("1", "AADE editors' journal", "AADE Ed J", "0160-6999", "", "AADE Ed J", "7708172")
#a.append(b)
#print a
for i in b:
    a.append(i)
print a

ff = open('E:/12.xls', 'w')
aa = csv.writer(ff, dialect = 'excel')
aa.writerow(['jj', 'ss'])
ff.close()
