from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

class newsView(View):
  def get(self, request):
    news = list(newsModel.objects.all())[::-1]
    return render(request, 'news/templates/index.html', {
      'news': news
    })

  def post(self, request):
    data = dict(request.POST)
    if (len(request.FILES.dict()) > 0):
      file = request.FILES['preview']
      newsModel.objects.create(
        title = data['title'][0],
        description = data['description'][0],
        preview = file
      )
    else:
      newsModel.objects.create(
        title = data['title'][0],
        description = data['description'][0],
      )

    allObjects = list(newsModel.objects.all())
    list_of_previews = []
    for element in allObjects:
      list_of_previews.append(str(element['preview']))
    print(list_of_previews)

    return HttpResponse('OK')
