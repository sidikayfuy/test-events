from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('registration/', views.UserCreate.as_view(), name='register_user'),
    path('events/', views.EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('events/<int:event_id>/join/', views.join_event, name='join-event'),
    path('events/<int:event_id>/disjoin/', views.disjoin_event, name='disjoin-event'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]