from django.shortcuts import render, redirect
from .models import Day
from django.http import JsonResponse
from rest_framework import generics
from .serializers import DaySerializer
# Create your views here.


class DayList(generics.ListCreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class DayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer