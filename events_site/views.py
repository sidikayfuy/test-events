import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from events_site.forms import CustomUserCreationForm
from events_site.models import CustomUser, Event


class IndexView(TemplateView):
    template_name = 'events_site/site/index.html'


index = login_required(IndexView.as_view())


class UserRegistrationView(CreateView):
    template_name = 'events_site/auth/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().get(request, *args, **kwargs)


registration = UserRegistrationView.as_view()


class UserLoginView(LoginView):
    template_name = 'events_site/auth/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().get(request, *args, **kwargs)


login = UserLoginView.as_view()


class UserLogoutView(LogoutView):
    next_page = 'login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().get(request, *args, **kwargs)


logout = login_required(UserLogoutView.as_view())


class ProfileView(DetailView):
    model = CustomUser
    template_name = 'events_site/site/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user


profile = login_required(ProfileView.as_view())


def ajaxEvents(request):
    events = Event.objects.prefetch_related('participants').all()
    events_list = []
    for event in events:
        participants_list = [{'id': participant.id, 'name': str(participant)} for participant in event.participants.all()]
        event_dict = {
            'id': event.id,
            'title': event.title,
            'text': event.text,
            'date': event.date,
            'creator': event.creator.id,
            'participants': participants_list
        }
        events_list.append(event_dict)
    return JsonResponse({'status': 'success', 'events': list(events_list)})


def ajaxUser(request):
    user = CustomUser.objects.get(id=request.GET.get('id'))
    user_json = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'birthdate': user.birthdate,
    }
    return JsonResponse({'status': 'success', 'user': user_json})


def joinEvent(request):
    user = CustomUser.objects.get(id=request.user.id)
    event = Event.objects.get(id=request.GET['event'])
    event.participants.add(user)
    return JsonResponse({'status': 'join success'})


def disjoinEvent(request):
    user = CustomUser.objects.get(id=request.user.id)
    event = Event.objects.get(id=request.GET['event'])
    event.participants.remove(user)
    return JsonResponse({'status': 'disjoin success'})
