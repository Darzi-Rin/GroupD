from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
app_name='diary'
URLPatterns=[
    path('',views.IndexView.as_view(),name='index'),
]