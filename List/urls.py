from django.urls import path
from datetime import date
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addItem/', views.addItem, name="add-item"),
    path('updateItem/<int:itemId>', views.updateItem, name="update-item"),
    path('deleteItem/<int:itemId>', views.deleteItem, name="delete-item"),
]
