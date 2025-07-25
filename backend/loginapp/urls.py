from django.urls import path
from .views import login_view, home_view

urlpatterns = [
    path('', home_view),
    path('login/', login_view),
]