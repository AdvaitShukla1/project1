from django.shortcuts import render
from django.http import HttpResponse
posts=[{'Author':'Advait Shukla',
        'Title':'Blog Post 1',
        'Content':'First post content',
        'date_posted':'January 01,2022'},
       {'Author':'Advait Shukla',
        'Title':'Blog Post 2',
        'Content':'Second post content',
        'date_posted':'January 10,2022'}]
# Create your views here.
def home(request):
    context={
        'posts':posts
    }
    return render(request,r'app1\home.html',context)
def about(request):
    return render(request,r'app1\about.html')