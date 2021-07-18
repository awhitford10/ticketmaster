from django.shortcuts import render
from django.http import HttpResponse

def search_page(request):
    return render(request, 'ticketmaster/index.html')

