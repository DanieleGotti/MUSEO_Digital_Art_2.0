"""
URL configuration for museodigitalart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import viewssala
from . import viewstema
from . import viewsopera
from . import viewsautore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tema/', viewstema.tema, name='tema'),  
    path('sala/', viewssala.sala, name='sala'),
    path('opera/', viewsopera.opera, name='opera'),  
    path('autore/', viewsautore.autore, name='autore'),  
    
    path('autore/create', viewsautore.create_autore, name='create_autore'),
    path('autore/update/<str:codice>/', viewsautore.update_autore, name='update_autore'),
    path('autore/delete/<str:codice>/', viewsautore.delete_autore, name='delete_autore'),
]