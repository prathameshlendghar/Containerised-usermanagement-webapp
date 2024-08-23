
from django.urls import path
from . import views

urlpatterns = [
    path('emp/', views.emp, name='emp'),  
    path('show/', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),  
    path('delete/<int:id>', views.destroy, name='delete'),  
]
