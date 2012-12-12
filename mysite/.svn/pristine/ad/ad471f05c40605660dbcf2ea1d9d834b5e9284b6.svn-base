#encoding:UTF-8
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    url = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['url']#默认按照name的升序排列

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField(blank = False)
    last_accessed = models.DateField()
    def __unicode__(self):
        return u'%s.%s' % (self.first_name, self.last_name)

class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains = keyword).count()

    def querybook(self, num = 0):
        if num != 0:
            return super(BookManager, self).all()[num]
        return super(BookManager, self).all()

class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    objects = models.Manager()
    me_objects = BookManager()

    def __unicode__(self):
        return self.title
