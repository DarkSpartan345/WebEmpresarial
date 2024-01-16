from django.shortcuts import render, get_object_or_404
from .models import Page

def pages(request,page_id,page_title):
    page=get_object_or_404(Page,id=page_id)
    return render(request,"pages/sample.html",{"page":page})
