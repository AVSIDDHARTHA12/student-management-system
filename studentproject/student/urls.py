from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_student, name='view_student'),
    path('add-student/', views.add_student, name='add_student'),
    path('add-marks/', views.add_marks, name='add_marks'),
    path('edit-details/<str:roll>/', views.edit_details, name='edit_details'),
]