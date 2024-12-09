from django.shortcuts import render

# Create your views here.
def home(request):
    names=['chinmaye','lakshmi','aliakbar']
    return render(request,'secondapp/index.html',{'names':names})