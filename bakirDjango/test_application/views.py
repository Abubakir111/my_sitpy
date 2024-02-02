from django.shortcuts import render
from .models import Bakir
# Create your views here.
def index(request):
    get_db = Bakir.objects.all()
    return render(request,'main/index.html',{'db':get_db})
def create(request):
    return render(request, 'main/create.html')