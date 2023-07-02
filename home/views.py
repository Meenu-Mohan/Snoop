from django.shortcuts import render
from .models import Juvenile
from django.http import HttpResponse

# Create your views here.
def index(request):

    juvs = Juvenile.objects.filter(missing=True).order_by('-id')[:3]

    return render(request, 'index.html',{'juvs':juvs})

def sos(request):
    return render(request, 'sos.html')