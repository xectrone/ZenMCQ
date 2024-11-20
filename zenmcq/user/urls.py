from django.urls import path
from .views import register_view, login_view, logout_view, edit_profile_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('edit-profile/', edit_profile_view, name='edit_profile'),
]
