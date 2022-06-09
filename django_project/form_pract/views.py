from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

# from django_project.form_pract.models import form_pract
from .forms import form_practForm
from .models import form_pract
# Create your views here.

def index(request):
    form = form_practForm()
    if request.method == 'POST':
        form = form_practForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form' : form}
    return render(request,'form_pract/index.html',context)

def read(request):
    data_list= form_pract.objects.all()
    context = {'data_list' : data_list}
    return render(request, 'form_pract/read.html', context)