from django.urls import path
from app2.views import *
app_name='some2'

urlpatterns=[
    path('second/',second,name='second'),
    path('h2/',h2,name='h2'),
]