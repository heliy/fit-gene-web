# encoding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from fitgene.models import Chr_len,Gene

# 
def index(request):
    return HttpResponse("Input")
    
