from django.urls import path, include

from .views import user
from .views import bill


urlpatterns = [
    path('user/register', user.register),
    path('user/login', user.login),
    path('user/logout', user.logout),
    path('bill/create', bill.create),
]