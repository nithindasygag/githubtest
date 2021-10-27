from django.urls import path
from . import views


urlpatterns = [
    path('create', views.index, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('list', views.list_all, name='list'),
    # path('details/<int:id>', views.details, name='details'),
    path('delete/<int:id>', views.delete),
]