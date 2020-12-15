from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Crimelist, Login
from django.contrib.auth.decorators import login_required
from .import forms


def homepage(request):
    return render(request, 'CrimeReportingSystem/homepage.html')


def Crimes(request):
    cl = Crimelist.objects.all().order_by('date')
    return render(request, 'CrimeReportingSystem/crimelist.html', {'cl': cl})


def Detail(request, crime_id):
    return HttpResponse('<h2> This are the details about the crime:'+str(crime_id)+'</h2>')


@login_required(login_url="/login")
def Add_create_view(request):
    if request.method == 'POST':
        form = forms.AddCrimes(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
            return redirect('CrimeReportingSystem:crimelist')
    else:
        form = forms.AddCrimes()
    return render(request, 'CrimeReportingSystem/add_crimes.html', {'form': form})







