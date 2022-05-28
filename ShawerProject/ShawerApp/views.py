from django.shortcuts import render
from .models import counselor
# Create your views here.
def home(request):
    return render(request,'index.html',{'title':'home'})
def about(request):
    return render(request,'about.html')

def consolt(request):
    context= {'consoler':counselor.objects.all()}
    return render(request,'counsolting.html',context)