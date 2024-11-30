from django.urls import path

from task_manager.user import views

urlpatterns = [
    path('', views.ListUsers.as_view(), name='users_list'),
    path('create/', views.AddUser.as_view(), name='add_user'),
    path('logout/', views.LogoutUser.as_view(), name='logout_user'),
    path('<int:pk>/update/', views.UpdateUser.as_view(), name='update_user'),
    path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete_user'),
]
