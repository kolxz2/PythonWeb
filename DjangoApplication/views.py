from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'DjangoApplication/index.html', {"title": "Head from index"})

def about(request):
    return render(request, 'DjangoApplication/about.html')