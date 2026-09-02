from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def product_detail(request, handle):
    return render(request, 'product_detail.html', {'handle': handle})

def visit(request):
    return render(request, 'visit.html')

def contact(request):
    return render(request, 'contact.html')

def book(request):
    return render(request, 'book.html')

def who_we_are(request):
    return render(request, 'who.html')

def story(request):
    return render(request, 'story.html')

def events(request):
    return render(request, 'events.html')

def winery(request):
    return render(request, 'winery.html')

def vineyard(request):
    return render(request, 'vineyard.html')

def adopt_a_vine(request):
    return render(request, 'adopt_a_vine.html')

def privacy(request):
    return render(request, 'index.html')

def terms(request):
    return render(request, 'index.html')

def cookies(request):
    return render(request, 'index.html')
@require_POST
def newsletter_signup(request):
    email = request.POST.get('email', '').strip()
    interests = request.POST.getlist('interest')

    if not email:
        return JsonResponse({'message': 'Please enter a valid email address.'}, status=400)

    list_ids = [settings.BREVO_LISTS[i] for i in interests if i in settings.BREVO_LISTS]
    if not list_ids:
        return JsonResponse({'message': 'Please choose at least one interest.'}, status=400)

    try:
        response = requests.post(
            'https://api.brevo.com/v3/contacts',
            headers={
                'api-key': settings.ANYMAIL['BREVO_API_KEY'],
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            json={'email': email, 'listIds': list_ids, 'updateEnabled': True},
            timeout=8,
        )
    except requests.RequestException:
        return JsonResponse({'message': 'Something went wrong — please try again.'}, status=502)

    if response.status_code in (200, 201, 204):
        return JsonResponse({'message': "You're subscribed — thank you!"})

    return JsonResponse({'message': 'Something went wrong — please try again.'}, status=502)