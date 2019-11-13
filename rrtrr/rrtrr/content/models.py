from django.db import models

from core.models import TimeStampModel

class Contents(TimeStampModel):
    title = models.CharField(max_length=200, verbose_name = '제목')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')
    like_count = models.PositiveIntegerField(default=0)

# Create your models here.
