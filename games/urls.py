from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import GameListView, GameDetailView, register, login_view, logout_view

urlpatterns = [
    path('', GameListView.as_view(), name='game_list'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
