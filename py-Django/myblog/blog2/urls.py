from django.urls import path, include

from . import views

import sys
sys.path.append('../')
sys.path.append('../../')

urlpatterns = [
    path('index/', views.index),
]