from django.urls import path
from task_manager.labels import views


urlpatterns = [
    path('', views.ListLabels.as_view(), name='labels_list'),
    path('create/', views.AddLabel.as_view(), name='add_label'),
    path('<int:pk>/update/', views.UpdateLabel.as_view(), name='update_label'),
    path('<int:pk>/delete/', views.DeleteLabel.as_view(), name='delete_label'),
]