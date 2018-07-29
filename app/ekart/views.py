from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Cyclone
from .forms import registration_form, login_form, cyclone_form
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register(request):
    form = registration_form(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        # username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        return redirect('ekart:user_login')
    return render(request, 'ekart/registration_form.html', context={'form': form, 'caption':'register',})

def user_logout(request):
    logout(request)
    return redirect('ekart:user_login', permanent=True)


def user_login(request):
    form = login_form(request.POST or None)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('ekart:index')
            else:
                return render(request, 'ekart/login_form.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'ekart/login_form.html', {'form': form, 'error_message': 'Invalid login'})
    return render(request, 'ekart/login_form.html', {'form': form,})

def login_page(request):
    return render(request, 'ekart/base_visitor.html');


def add_cyclone_image(request):
    form = cyclone_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form':form,
        'caption': 'Add cyclone image',
    }
    return render(request, 'ekart/cycloneForm.html',context)