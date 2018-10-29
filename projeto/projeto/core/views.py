from datetime import datetime
from django.shortcuts import render
from .models import Dispositivo,Dados

# Create your views here.
def index2(request):
    return render(request,"index.html")


def index(request):
    listO = Dados.objects.select_related('dispositivo')
    lat = Dispositivo.objects.get(pk=1)
    list = Dados.objects.all().filter(dispositivo=1)
    ult = Dados.objects.latest('data')
    # list = Dados.objects.filter(Dados.objects.latest('data'))
    ult = Dados.objects.latest('data')
    listDisp = Dispositivo.objects.all()

    api_key = 'AIzaSyC-gwBjleF-ixYwe5NhiF6TMVIMNe1WED4'
    contex = { 'list':list,
              'api_key': api_key,
              'lat': lat,
              'long': '-48.06575099999998',
              'ult':ult,
              'listO':listO,
              'listDisp':listDisp,

              }
    #return JsonResponse(list)
    return render(request,"index.html", contex)