from django.contrib import admin
from .models import *

class newsAdmin(admin.ModelAdmin):
  list_display = ['title']

admin.site.register(newsModel, newsAdmin)
