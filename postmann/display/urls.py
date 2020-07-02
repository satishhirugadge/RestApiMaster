from django.urls import path
from . import views

urlpatterns=[
    path('display/', views.login, name='display'),

]