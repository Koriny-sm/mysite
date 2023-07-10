from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
  return HttpResponse("안녕하세요. 환영합니다. 현재 polls index에 위치합니다.")