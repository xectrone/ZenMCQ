from django.shortcuts import render
from django.template.loader import get_template


def home_view(request):
    template = get_template('base.html') 
    return render(request, 'website/home.html')
