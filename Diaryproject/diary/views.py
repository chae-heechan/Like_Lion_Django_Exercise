from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *

def home(request):
    stories = Story.objects.all()
    paginator = Paginator(stories, 2)
    page_number = int(request.GET.get('page', 1))
    card1 = paginator.get_page((page_number*3)-2)
    card2 = paginator.get_page((page_number*3)-1)
    card3 = paginator.get_page(page_number*3)
    return render(request, 'home.html', {"story1": card1, "story2" : card2, "story3" : card3})

def detail(request, id):
    story = get_object_or_404(Story, pk=id)
    return render(request, 'detail.html', {'story':story})