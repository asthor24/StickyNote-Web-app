
from django.urls import path, include
from .views import (
    sticky_note_detail_page, 
    sticky_note_overview_page, 
    sticky_note_test_page,
    sticky_note_create_page, 
    sticky_note_update_page, 
    sticky_note_delete_page, 
    ajax_note_update_page, 
    ajax_note_update_content_page, 
    ajax_note_update_zindex_page,
    ajax_note_delete_page
)

urlpatterns = [
    path('<int:note_id>/', sticky_note_detail_page),
    path('', sticky_note_overview_page),
    path('test/', sticky_note_test_page),
    path('create/', sticky_note_create_page),
    path('update/<int:note_id>/', sticky_note_update_page),
    path('delete/<int:note_id>/', sticky_note_delete_page),
    path('ajax/update/', ajax_note_update_page),
    path('ajax/update/content', ajax_note_update_content_page),
    path('ajax/update/zindex', ajax_note_update_zindex_page),
    path('ajax/delete/', ajax_note_delete_page)
]