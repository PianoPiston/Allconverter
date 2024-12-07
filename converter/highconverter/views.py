from django.shortcuts import render

# Create your views here.

def converter(request):
    return render(request, "allscale_converter.html")

