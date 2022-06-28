from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from Second_App.models import topic, Webpage,Accessrecord

# Create your views here.

def index(request):
    webpagelist=Accessrecord.objects.order_by('date')
    date_dict={'acces_records': webpagelist}
    return render(request, 'second_app/index.html', context=date_dict)
