from turtle import title
from django.db import models

class Cashbook(models.Model):
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField('data published')
    content = models.TextField()

    def __str__(self):
        return self.title
