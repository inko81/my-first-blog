from django.db import models

# Create your models here.

class Kintai(models.Model):
    employee_no = models.IntegerField('社員No.')
    name = models.CharField('名前',max_length=255)
    start = models.TimeField('就業開始時刻')
    end = models.TimeField('就業終了時刻')
    
    def __str__(self):
        return self.name
