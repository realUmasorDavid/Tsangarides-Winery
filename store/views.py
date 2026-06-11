from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def visit(request):
    return render(request, 'visit.html')

def contact(request):
    return render(request, 'contact.html')

def book(request):
    return render(request, 'book.html')

def events(request):
    return render(request, 'index.html')

def story(request):
    return render(request, 'story.html')

def privacy(request):
    return render(request, 'index.html')

def terms(request):
    return render(request, 'index.html')

def cookies(request):
    return render(request, 'index.html')