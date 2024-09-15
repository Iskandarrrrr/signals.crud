from django.urls import path
from .views import CustomerUserView


urlpatterns = [
    path('customs/', CustomerUserView.as_view()),
]