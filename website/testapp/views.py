# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import tushare as ts
 
def index(request):
    return HttpResponse(u"欢迎光临DataMole！")
	
def dahua(request):
    dahua = ts.get_realtime_quotes('002236')
    return HttpResponse(dahua.iloc[0,3])
