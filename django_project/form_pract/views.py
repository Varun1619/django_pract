from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

# from django_project.form_pract.models import form_pract
from .forms import form_practForm
from .models import form_pract
# Create your views here.

def index(request):
    form = form_practForm()
    #Calling the Modelform and storing it under variable form

    if request.method == 'POST':
        form = form_practForm(request.POST)
        #transfer the entered Modelform data into the varialble form

        if form.is_valid():
            #If the data is Valid then save it

            form.save()
            return redirect('index')
    context = {'form' : form}
    #This allows us to make the Modelform directly into the website

    return render(request,'form_pract/index.html',context)

def read(request):
    data_list= form_pract.objects.all()
    #Fetch the data from Class 

    context = {'data_list' : data_list}
    return render(request, 'form_pract/read.html', context)

def update(request, pk):
    data_list = form_pract.objects.get(id = pk)
    #Fetching data according to the particular id

    form = form_practForm(instance=data_list)
    #store data of the selected data and store in the form in update section

    if request.method == 'POST':
        form = form_practForm(request.POST, instance=data_list)
        #Store the updated data in the form 

        if form.is_valid():
            form.save()
            return redirect('read')
    context = {'form' : form}
    return render(request, 'form_pract/update.html',context)

def delete_data(request,pk):
    data_list = form_pract.objects.get(id = pk)
    data_list.delete()
    #Directly deletes the data of the particular id
    
    context = {'data_list' : data_list}
    return redirect('read')