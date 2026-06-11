from django.urls import path
from .views import contact, index, shop, book, story, visit, events, privacy, terms, cookies

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('book-a-tasting/', book, name='book'),
    path('events/', events, name='events'),
    path('visit/', visit, name='visit-us'),
    path('contact/', contact, name='contact'),
    path('story/', story, name='our-story'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
    path('cookies/', cookies, name='cookies'),
]