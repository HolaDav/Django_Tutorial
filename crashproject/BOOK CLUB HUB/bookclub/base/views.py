from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Club, Genre
from .forms import ClubForm

# Create your views here.

# clubs = [
#     {"id":1, "name":"The Page Turners"},
#     {"id":2, "name":"Readers' Haven"},
#     {"id":3, "name":"The Book Nook"},
#     {"id":4, "name":"Bound by Books"},
#     {"id":5, "name":"Chapters & Conversations"},
#     {"id":6, "name":"The Literary Lounge"},
#     {"id":7, "name":"The Story Seekers"},
#     {"id":8, "name":"Beyond the Cover"},
#     {"id":9, "name":"Read & Relate"},
#     {"id":10, "name":"Tales & Tea"},
# ]

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exits')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is not correct')

    context = {}
    return render(request, 'base/login_register.html', context)

def logoutuser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    clubs = Club.objects.filter(
        Q(genre__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    genres = Genre.objects.all()

    club_count = clubs.count()

    context = {"clubs": clubs, 'genres': genres, 'club_count': club_count}
    return render(request, 'base/home.html', context)

def club(request, pk):
    club = Club.objects.get(id=pk)
    context = {"club": club}
    return render(request, 'base/club.html', context)

def createClub(request):
    form = ClubForm()

    if request.method == "POST":
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {"form":form}
    return render(request, 'base/club_form.html', context)

def updateClub(request, pk):
    club = Club.objects.get(id=pk)
    form = ClubForm(instance=club)

    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/club_form.html', context)

def deleteClub(request, pk):
    club = Club.objects.get(id=pk)

    if request.method == 'POST':
        club.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {"obj":club})