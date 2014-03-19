from django.db import models

class User(models.Model):
    ip = models.CharField(max_length = 15,primary_key=True)
    display_post = models.IntegerField(max_length = 3,default=10)

    def __unicode__(self):
        return self.ip

