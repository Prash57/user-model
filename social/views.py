from django.shortcuts import render

# Create your views here.


def soc_home(request):
    return render(request, 'social/home.html')
