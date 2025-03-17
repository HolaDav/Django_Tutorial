from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Club
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

def home(request):
    clubs = Club.objects.all()
    context = {"clubs": clubs}
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