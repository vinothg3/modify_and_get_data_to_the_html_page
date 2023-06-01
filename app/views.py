from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def topic_data(request):
    #td=Topic.objects.all()
    #td=Topic.objects.order_by('-Topic_name')
    #td=Topic.objects.order_by(Length('Topic_name'))
    #td=Topic.objects.exclude(Topic_name='cricket')
    td=Topic.objects.filter(Topic_name__gt='cricket')
    d={'td':td}
    return render(request,'topic_data.html',d)

def webpage_data(request):
    wd=Webpage.objects.all()
    #wd=Webpage.objects.filter(Name='vinith').update(Email='123vi@gmail.com')
    #wd=Webpage.objects.filter(Name='vin').update_or_create (Topic_name='cricket', defaults={'Age':22,"Email":'govi@gmail.com','Name':'vi','Topic_name':'cricket'})
    #wd=Webpage.objects.filter(Name='vinith').delete()
    wd=Webpage.objects.order_by(Length('Name'))
    wd=Webpage.objects.all()
    d={'wd':wd}
    return render(request,'webpage_data.html',d)

