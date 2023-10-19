from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def counter(request):
    words = request.GET['text']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
