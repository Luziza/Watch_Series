from django.urls import path
from pages.views import HomePageView, AboutPageView, FavoritePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('favoritos/', FavoritePageView.as_view(), name="favoritos" ),
]