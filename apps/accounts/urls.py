from django.urls import path
from .views.user_views import dashboard_view
from .views.auth_views import login_view, logout_view, signup_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('dashboard/', dashboard_view, name='dashboard'),
]
