# coding:utf-8
# @Author:shuibugou


from django.urls import path, re_path
from IOweb import views

urlpatterns = [
    path('member/<member_id>/', views.IO_members, name='member'),
    path('test/', views.test, name='test'),
    path('love/', views.love, name='love'),

]