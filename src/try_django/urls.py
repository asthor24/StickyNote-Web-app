"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_page,about_page
from note.views import sticky_note_detail_page, sticky_note_overview_page, sticky_note_test_page


urlpatterns = [
    path("", home_page),
    path('admin/', admin.site.urls),
    path('about/', about_page),
    path('note/<int:note_id>/', sticky_note_detail_page),
    path('note/', sticky_note_overview_page),
    path('test/', sticky_note_test_page)
]
