from django.urls import path

from task_manager.tasks import views

urlpatterns = [
    path('', views.ListTasks.as_view(), name='tasks_list'),
    path('create/', views.AddTask.as_view(), name='add_task'),
    path('<int:pk>/update/', views.UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete/', views.DeleteTask.as_view(), name='delete_task'),
    path('<int:pk>/', views.TaskView.as_view(), name='task_view')
]
