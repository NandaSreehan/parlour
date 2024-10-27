from django.db import models


class clist(models.Model):
    name=models.CharField(max_length=30)
    number=models.IntegerField()