from django.urls import path

from . import views


urlpatterns = [
    path('apply-job/<int:id>/', views.apply_job, name='apply_job'),
    path('my-applications/', views.my_application, name='my_application'),
    path('view-applicants/<int:id>/', views.view_applicants, name='view_applicants'),
    path('all-applicants-list/', views.all_applicants, name='all_applicants'),
    path('update-status/<int:id>/', views.update_status, name='update_status'),
]