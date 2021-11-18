from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.DayList.as_view(), name='day_list'),
    path('days/', views.DayList.as_view(), name='day_list'),
    path('days/<int:pk>', views.DayDetail.as_view(), name='day_detail')
]