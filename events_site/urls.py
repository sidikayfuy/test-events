from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('ajaxEvents/', views.ajaxEvents, name='ajaxEvents'),
    path('ajaxUser/', views.ajaxUser, name='ajaxUser'),
    path('joinEvent/', views.joinEvent, name='joinEvent'),
    path('disjoinEvent/', views.disjoinEvent, name='disjoinEvent'),
]
