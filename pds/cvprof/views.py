from django.shortcuts import render
from django.http import HttpResponse
from .models import CVModel

# Create your views here.
def index(request,id=1):
    data = CVModel.objects.get(pk=id)
    return render(request,'cvprof/index.html',{'data':data})

def profile(request):
    context = {}
    data = CVModel.objects.all()
    context = {'records': data}
    return render(request,'cvprof/prof.html',context)

def addprofile(request):
    context = {}
    data = CVModel.objects.all()
    context = {'records': data}
    return render(request,'cvprof/addprof.html',context)