from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Food
from .forms import food_form, registration_form, login_form
from django.contrib.auth import authenticate, login, logout
from django.utils.http import quote_plus
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'ekart/base.html', {'form': login_form(None)})
    else:
        context = {
            'foods': Food.objects.all(),
            'username': request.user.get_username(),
        }
        return render(request, 'ekart/index.html', context)

def details(request, food_id):

    food = get_object_or_404(Food, pk=food_id)
    # share_string = quote_plus(food.food_title)
    context = {
        'food':food,
        # 'share_string':share_string,
    }
    return render(request, 'ekart/details.html', context)

def favourite_food(request,food_id):
    food = get_object_or_404(Food, pk=food_id)
    if food.is_favourite:
        food.is_favourite = False
    else:
        food.is_favourite = True
    food.save()
    return redirect('ekart:index')

# def favourite_song(request, food_id, song_id):
#     food = get_object_or_404(Food, pk=food_id)
#     song = get_object_or_404(Song, pk=song_id)
#     if song.is_favourite:
#         song.is_favourite = False
#     else:
#         song.is_favourite = True
#     song.save()
#     return HttpResponseRedirect(food.get_absolute_url())
#     # try:
#     #     selected_song = get_object_or_404(Song, pk=request.POST['checked'])
#     # except (KeyError, Song.DoesNotExist):
#     #     context = {
#     #         'food': food,
#     #         'error_message':'you did not select the valid song',
#     #     }
#     #     return render(request, 'ekart/details.html', context)
#     # else:
#     #     selected_song.is_favourite = True
#     #     selected_song.save()
#     #     context = {
#     #         'food':food,
#     #     }
#     #     return HttpResponseRedirect(food.get_absolute_url())

def add_food(request):
    if not request.user.is_authenticated:
        return redirect("ekart:user_login")
    else:
        form = food_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        context = {
            'form':form,
            'caption': 'Add Food',
        }
        return render(request, 'ekart/food_form.html',context)
    
# def add_song(request, food_id):
#     form = song_form(request.POST or None, request.FILES or None)
#     food = get_object_or_404(Food, pk=food_id)
#     if form.is_valid():
#         song_title = request.POST.get('song_title')
#         audio_file = request.FILES.get('audio_file')
#         food.song_set.create(song_title=song_title, audio_file=audio_file)
#         return HttpResponseRedirect(food.get_absolute_url())
#     context = {
#         'form':form,
#         'caption': 'Add Song',
#     }
#     return render(request, 'ekart/song_form.html', context)

def update_food(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    form = food_form(request.POST or None, instance=food, files=request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(food.get_absolute_url())
    context = {
        'form':form,
        'caption': 'Update Food',
    }
    return render(request, 'ekart/food_form.html',context)

# def update_song(request, food_id, song_id):
#     song = get_object_or_404(Song, pk=song_id)
#     _ = get_object_or_404(Food, pk=food_id)
#     form = song_form(request.POST or None, request.FILES or None, instance=song)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         return HttpResponseRedirect(_.get_absolute_url())
#     context = {
#         'form': form,
#         'caption': 'Update Song',
#     }
#     return render(request, 'ekart/song_form.html', context)

def delete_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    food.delete()
    return redirect('ekart:index')

# def delete_song(request, food_id, song_id):
#     food =get_object_or_404(Food, pk=food_id)
#     song = get_object_or_404(Song, pk=song_id)
#     song.delete()
#     return HttpResponseRedirect(food.get_absolute_url())

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

# def all_songs(request):
#     context ={
#         'foods': Food.objects.all(),
#     }
#     return render(request, 'ekart/all_songs.html', context)
