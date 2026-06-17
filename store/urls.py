from django.urls import path
from .views import contact, winery, vineyard, index, shop, book, story, visit, privacy, terms, cookies, who_we_are, events

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('book-a-tasting/', book, name='book'),
    path('who-we-are/', who_we_are, name='who-we-are'),
    path('visit/', visit, name='visit-us'),
    path('contact/', contact, name='contact'),
    path('story/', story, name='our-story'),
    path('events/', events, name='events'),
    path('winery/', winery, name='winery'),
    path('vineyard/', vineyard, name='vineyard'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
    path('cookies/', cookies, name='cookies'),
]