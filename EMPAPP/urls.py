from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='emp_data'),

    # CREATE
    path('insert/', views.insert, name='insert'),

    # UPDATE
    path('update/<int:id>/', views.employee_update, name='update'),

    # DELETE
    path('delete/<int:id>/', views.employee_delete, name='delete'),
]