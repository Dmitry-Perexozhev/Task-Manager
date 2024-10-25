from django.urls import path
from task_manager.user import views

urlpatterns = [
    path('', views.ListUsers.as_view(), name='users_list'),
    path('create/', views.AddUser.as_view(), name='add_user'),
    path('edit/<int:pk>/', views.UpdateUser.as_view(), name='edit_user'),
    path('delete/<int:pk>/', views.DeleteUser.as_view(), name='delete_user'),
]