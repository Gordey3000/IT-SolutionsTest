from django.urls import path

from . import views

urlpatterns = [
    path('ads/', views.AdsListAPIView.as_view(), name='food-list'),
    path('ads/<int:pk>/', views.AdsDetail.as_view(), name='food-detail'),
    path('register/', views.UserRegistrationAPIView.as_view(), name='user-registration'),
]
