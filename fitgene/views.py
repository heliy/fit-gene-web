# encoding:utf-8

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from fitgene.models import Chr_len,Gene
from fitgene.utils import action_context
from django.shortcuts import render

def index(request):
    return render(request,'fitgene/index.html',{})

def action(request):
    chr_no = request.GET['chr_no']
    loc = request.GET['loc']
    display = request.GET['display']
    context = action_context(chr_no,loc,display)
    return render(request,'fitgene/action.html',context)
    
    
