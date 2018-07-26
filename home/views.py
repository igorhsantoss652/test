from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def index(request):
    return render(request, 'index.html')