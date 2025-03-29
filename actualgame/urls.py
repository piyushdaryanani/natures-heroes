from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('menu/', views.menu, name='menu'),
    path('select_bin/', views.select_bin, name='select_bin'),
    path('recycling_game/', views.recycling_game, name='recycling_game'),
    path('compost_bin/', views.compost_bin, name='compost_bin'),
    path('ewaste_bin/', views.ewaste_bin, name='ewaste_bin'),
    path('trash_bin/', views.trash_bin, name='trash_bin'),
    path('rules/', views.rules, name='rules'),
    path('exit/', views.exit_game, name='exit_game'),
    path('game/', views.game_page, name='game_page'),
]
