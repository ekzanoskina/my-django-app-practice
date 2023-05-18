from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse

def get_rectangle_area(request, height: int, width: int):
    return HttpResponse(f'Площадь прямоугольника размером {height}x{width} равна {height * width}')
def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width ** 2}')
def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга радиуса {radius} равна {pi * (radius ** 2)}')

def redirect_rectangle(request, height: int, width: int):
    redirect_url_rect = reverse('rectangle', args=[height, width])
    return HttpResponseRedirect(redirect_url_rect)

def redirect_square(request, width: int):
    redirect_url_sq = reverse('square', args=[width])
    return HttpResponseRedirect(redirect_url_sq)

def redirect_circle(request, radius: int):
    redirect_url_cir = reverse('circle', args=[radius])
    return HttpResponseRedirect(redirect_url_cir)