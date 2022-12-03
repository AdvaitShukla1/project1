from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,r'C:\Users\Advait Shukla\project1\app1\templates\app1\home.html')
def about(request):
    return HttpResponse('<h1>Blog About</h1>')