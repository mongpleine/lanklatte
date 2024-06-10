from django.conf import settings
from django.db import models
from django.utils import timezone

class Item(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField(verbose_name="제목", max_length=200)
    content = models.TextField(verbose_name="내용")
    created_date = models.DateTimeField(
        verbose_name="작성일", default=timezone.now)

    def __str__(self):
        return self.title