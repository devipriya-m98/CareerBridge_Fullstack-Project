from django.urls import path

from . import views


urlpatterns = [
    path('api/list_jobs/', views.api_list_jobs, name='api_list_jobs'),
    path('api/jobs/<int:j_id>/', views.api_get_job, name='api_get_job'),
]