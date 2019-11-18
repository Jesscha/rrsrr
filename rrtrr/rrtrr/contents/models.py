from django.db import models

from taggit.managers import TaggableManager
from tagging.fields import TagField
# Create your models here.


class Post(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()
    image = models.FileField(null=True, blank=True, upload_to='contents')
    tag = TagField()


    class Meta:
        verbose_name = '포스'
        verbose_name_plural = '포스트'
        ordering = ['title', ]

    def __str__(self):
        return self.title
