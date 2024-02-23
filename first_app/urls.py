from django.urls import path
from first_app.views import home, add_task, show_task, edit_task, delete_task, is_completed

urlpatterns = [
    path('', home),
    path('add_task/', add_task, name='addTask'),
    path('show_task/', show_task, name='showTask'),
    path('edit_task/<int:id>', edit_task, name='edit_task'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('is_completed/<int:id>', is_completed, name='is_completed'),
]