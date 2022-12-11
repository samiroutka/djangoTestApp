from django.db import models

class newsModel(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField(max_length=500)
  preview = models.ImageField(blank=True, upload_to='news/previews')

  class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'
    
