from django.shortcuts import render
from .models import Tienda
# Create your views here.

def tienda(request):
    tiendas=Tienda.objects.all()
    return render(request, 'tienda.html', {'tiendas':tiendas})