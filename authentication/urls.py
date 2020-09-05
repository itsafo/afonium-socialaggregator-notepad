# -*- encoding: utf-8 -*-
"""
HEREIN CONTAINS THE URL LINKS
YOU VAN CALL THIS FROM  YOUR ANCHOR TAG
"""

from django.urls import path
from .views import login_view, register_user, profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('profile/', profile, name="profile"),
    path("logout/", LogoutView.as_view(), name="logout")
]
