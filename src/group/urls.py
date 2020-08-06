from django.urls import path, include
from .views import groups_page,group_create_page

urlpatterns = [
    path("",groups_page),
    path("create/",group_create_page)

]
