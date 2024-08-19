from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el indecs de app1</h1>")

def vista1(request):
    html=""""
 <h1 style="color:green">Titulo app1</h1>
 <h2>Subtitulo app1</h2>
 """
    return HttpResponse(html)