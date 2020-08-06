
from django.urls import path, include
from .views import sticky_note_detail_page, sticky_note_overview_page, sticky_note_test_page,sticky_note_create_page, update_count
from django.conf.urls import url

urlpatterns = [
    path('<int:note_id>/', sticky_note_detail_page),
    path('', sticky_note_overview_page),
    path('test/', sticky_note_test_page),
    path('create/', sticky_note_create_page),
    path('update_count/',update_count)
]
