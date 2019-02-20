from django.shortcuts import render
from gallery.models import Gallery

def home(request):
    return render(request, 'home.html',{'gallerys' : Gallery.objects})