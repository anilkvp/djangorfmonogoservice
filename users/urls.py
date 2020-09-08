from django.urls import path
from .views import CreateView


urlpatterns = [
    path('users/', CreateView.as_view(), name="users-all"),
]