from django.urls import path
from . import views

urlpatterns = [
    path('jobs-list/', views.jobs_list, name='jobs_list'),
    path('job-details/<int:id>/', views.job_details, name='job_details'),
    path('category-view/<int:id>/', views.category_view, name='category_view'),
    path('search/', views.search, name='search'),
    path('post-job/', views.post_job, name='post_job'),
    path('manage-jobs/', views.manage_job, name='manage_job'),
    path('update-job/<int:id>/', views.update_job, name='update_job'),
    path('delete-job/<int:id>/', views.delete_job, name='delete_job'),
    
]