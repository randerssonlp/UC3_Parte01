import statistics
from django.shortcuts import render
from django.shortcuts import render, HttpResponse
import os
from django.http import FileResponse
# Create your views here.

layout = """
    <h1>LOGO UNTELS</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/rango">Primos</a>
        </li>
        <li>
            <a href="/saludo">Examen</a>
        </li>
    </ul>
    <hr>
    <h1>UNTELS - LP3 - LÓPEZ PURIS - 20/11/2023</h1>
"""

def index(request):
    mensaje="""
    """
    return HttpResponse(layout + mensaje)

def saludo(request):
    mensaje = """
    """
    return HttpResponse(layout + mensaje)

def rango(request):
    resultado = """
    """
    return HttpResponse(layout + resultado)