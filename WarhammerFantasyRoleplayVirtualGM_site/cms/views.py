from django.shortcuts import render
from math import ceil

from cms.models import News
from cms.serializers import NewsSerializer
from rest_framework import permissions, viewsets

# Create your views here.

import logging
logger = logging.getLogger(__name__)

def index(request, page=0):
    data = {}
    number_of_news_on_page = 9.0
    news = News.objects.filter(is_deleted=False).order_by('-datetime_update')
    data['news'] = news[page:page+number_of_news_on_page]
    data['page_numbers'] = []
    for p in range(ceil(len(news) / number_of_news_on_page)):
        print(p)
        data['page_numbers'].append({"page_number": int(p+1), "page_start" : int(p * number_of_news_on_page) })
    
    return render(request, 'cms_main.html', data)

def newsDetail(request, pk):
    data = {}
    
    data['news'] = News.objects.filter(pk=pk, is_deleted=False).order_by('datetime_update')
    
    
    return render(request, 'cms_details.html', data)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.filter(is_deleted=False).order_by('datetime_update')
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticated]