from django.db import models


class Advertisement(models.Model):
    '''
    Модель объявления.
    '''
    title = models.CharField(max_length=255)
    ad_id = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.title
