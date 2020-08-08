from django.urls import path
from .views import user_creation_page, login_page

urlpatterns = [
    path("sign_up/", user_creation_page),
    path("login/", login_page)
]
