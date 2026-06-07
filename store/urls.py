from django.urls import path
from .views import blog, contact, index, shop, story, visit, events, privacy, terms, cookies

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('events/', events, name='events'),
    path('visit/', visit, name='visit-us'),
    path('contact/', contact, name='contact'),
    path('story/', story, name='our-story'),
    path('blog/', blog, name='blog'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
    path('cookies/', cookies, name='cookies'),
]