from django.shortcuts import render
from .models import User
# Create your views here.
def bla(request):

    return render(request,'main.html')

def form(request):
    if request.method =='POST':
        x= request.POST.get('usern')
        z= request.POST.get('passw')
        data = User(username=x,password=z)
        data.save()
    return render(request,'form.html')

def data(request):
    
    return render(request,'data.html',{'data':User.objects.all()})