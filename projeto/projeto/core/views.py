from datetime import datetime
from django.shortcuts import render
from .models import Dispositivo,Dados
from datetime import datetime, timedelta, time
from django.utils import timezone

# Create your views here.
def index2(request):
    return render(request,"index.html")


def index(request):
    today = timezone.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    listO = Dados.objects.select_related('dispositivo')
    loc = Dispositivo.objects.get(pk=1)
    list = Dados.objects.all().filter(dispositivo=1).filter(data__lte=today_end, data__gte=today_start)
    ult = Dados.objects.latest('data')
    listDisp = Dispositivo.objects.all()

    api_key = 
    contex = { 'list':list,
              'api_key': api_key,
              'lat': loc,
              'long': loc,
              'ult':ult,
              'listO':listO,
              'listDisp':listDisp,

              }
    #return JsonResponse(list)
    return render(request,"index.html", contex)
