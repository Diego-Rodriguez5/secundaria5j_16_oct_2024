from django.shortcuts import render

# Create your views here.

def Index_visita(request):
    return render(request,"index.html")