from django.contrib import admin
from django.urls import path, include
from timetravel import views

app_name ='time_travel'

urlpatterns = [
    path('', views.predict, name='predict_page'),
    # path('', views.predit, name='predict_page'),
    # path('', views.predit, name='predict_page'),
]