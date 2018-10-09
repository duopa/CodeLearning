from django.urls import path, include

from . import views

import sys
sys.path.append('../')
sys.path.append('../../')

urlpatterns = [
    path('index/', views.index),
    path('article/<int:article_id>/', views.article_page ,name='article_page'),
    path('edit/', views.edit_page,name='edit_page'),
    path('edit/action/', views.edit_action,name='edit_action'),
    path('hello/', views.hello),
]