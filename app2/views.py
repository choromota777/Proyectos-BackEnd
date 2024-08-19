from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Index App2</h1>")


def texto(request):
    return HttpResponse("<p>Soy un párrafo de la app2</p>")