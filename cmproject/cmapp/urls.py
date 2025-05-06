from django.urls import path
from cmapp import views

urlpatterns = [
    path('tasks/', views.task_list),
]