from django.urls import path
from .views import contact, winery, vineyard, index, shop, book, story, visit, privacy, terms, cookies, who_we_are, events, adopt_a_vine, product_detail, newsletter_signup
# from .views import wine_club_register, wine_club_login, wine_club_verify, wine_club_logout, wine_club_home, wine_club_product_detail, wine_club_admin_approve, wine_club_admin_reject

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:handle>/', product_detail, name='product-detail'),  # NEW
    path('book-a-tasting/', book, name='book'),
    path('who-we-are/', who_we_are, name='who-we-are'),
    path('visit/', visit, name='visit-us'),
    path('contact/', contact, name='contact'),
    path('story/', story, name='our-story'),
    path('events/', events, name='events'),
    path('winery/', winery, name='winery'),
    path('vineyard/', vineyard, name='vineyard'),
    path('adopt-a-vine/', adopt_a_vine, name='adopt-vine'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
    path('cookies/', cookies, name='cookies'),
    # path('wine-club/register/', wine_club_register, name='wine-club-register'),
    # path('wine-club/login/', wine_club_login, name='wine-club-login'),
    # path('wine-club/verify/<str:token>/', wine_club_verify, name='wine-club-verify'),
    # path('wine-club/logout/', wine_club_logout, name='wine-club-logout'),
    # path('wine-club/', wine_club_home, name='wine-club-home'),
    # path('wine-club/shop/<slug:handle>/', wine_club_product_detail, name='wine-club-product-detail'),
    # path('wine-club/admin/<int:member_id>/approve/', wine_club_admin_approve, name='wine-club-admin-approve'),
    # path('wine-club/admin/<int:member_id>/reject/', wine_club_admin_reject, name='wine-club-admin-reject'),
    path('newsletter/signup/', newsletter_signup, name='newsletter-signup'),
]