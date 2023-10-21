from django.shortcuts import render,redirect
from .form import CityForm
from .models import City
import requests 
from django.contrib import messages

def home(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={},&appid=1684f0a98b1b9e32c4ab15bbf969f314&units=metric'

    if request.method=="POST":
        form=CityForm(request.POST)        
        if form.is_valid():
            NCity=form.cleaned_data['name']            
            CCity=City.objects.filter(name=NCity).count()
            if CCity==0:
                res=requests.get(url.format(NCity)).json()
                print(res)                
                if res['cod']==200:
                    form.save()
                    messages.success(request," "+NCity+" Added Successfully...!!!")
                else: 
                    messages.error(request,"City Does Not Exists...!!!")
            else:
                messages.error(request,"City Already Exists...!!!")  
    form=CityForm()
    cities=City.objects.all()
    data=[]
    for city in cities:        
        res=requests.get(url.format(city)).json()   
        city_weather={
            'city':city,
            'temperature' : res['main']['temp'],
            'description' : res['weather'][0]['description'],
            'country' : res['sys']['country'],
            'icon' : res['weather'][0]['icon'],
        }
        data.append(city_weather)  
    context={'data' : data,'form':form}
    return render(request,"weatherapp.html",context)

def delete_city(request,CName):
    City.objects.get(name=CName).delete()
    messages.success(request," "+CName+" Removed Successfully...!!!")
    return redirect('Home')


   
'''   total=int(count)+1
   response= render(request,'cook.html',{'count':total})
   response.set_cookie('count',total)
   return response'''


#form.cleaned_data: returns a dictionary of validated form input fields and their values, where string primary keys are returned as objects.

#form.data: returns a dictionary of un-validated form input fields and their values in string format (i.e. not objects).
