from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name="reservation_list"),
    path('create/',views.create_reservation,name='create_reservation'),
    path('edit/<int:pk>/', views.edit_reservation, name='edit_reservation'),
    path('delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
    path('<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('test/',views.test_page),
]