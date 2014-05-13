# coding:UTF-8
from django.db import models

__default_display__ = 10

class User(models.Model):
    ip = models.CharField(max_length=15, primary_key=True)
    display_post = models.IntegerField(max_length=3, default=__default_display__)

    def __unicode__(self):
        return self.ip

def get_user_display_post(ip):
    try:
        user = User.objects.get(ip=ip)
        display_post = user.display_post
    except User.DoesNotExist:
        display_post = __default_display__
        print 'not record about ip:%s in table jd_user' % ip
    return display_post


if __name__ == '__main__':
    user = User()
    user.ip = '127.0.0.1'
    user.display_post = 3
    user.save()
