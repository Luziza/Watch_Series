from django.urls import path
from pages.views import HomePageView, AboutPageView, FavoritePageView, LoginPageView, MaidPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('favoritos/', FavoritePageView.as_view(), name='favoritos' ),
    path('login/', LoginPageView.as_view(), name='login'),
    path('maid/', MaidPageView.as_view(), name='maid.html'),
]