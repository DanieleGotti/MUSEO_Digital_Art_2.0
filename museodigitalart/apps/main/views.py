from django.shortcuts import render
import sqlite3

def home(request):
    return render(request, 'main/home.html')