from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'labs/index.html')

def lab(request, lab_id):
    print("lab_id:"+lab_id)
    return render(request, 'labs/labs.html', {'lab_id': lab_id})

# Create your views here.
