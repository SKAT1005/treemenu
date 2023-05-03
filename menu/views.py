from django.shortcuts import render

from .models import Menu


def menu(request, item=None):
    return render(request, 'index.html', {'item': item})