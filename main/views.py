from django.shortcuts import render
from .models import News, ImageNews
from .serializers import NewsListSerializer, NewsItemSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class NewsListApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    pagination_class = PageNumberPagination


class NewsItemApiView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsItemSerializer
    lookup_field = 'id'

