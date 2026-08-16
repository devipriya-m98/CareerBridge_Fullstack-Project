from django.urls import path
from . import views


urlpatterns = [
    path('profile-dashboard/', views.profile_dashboard, name='profile_dashboard'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('addJobseeprofile-details/', views.addJobseeprofile_details, name='addJobseeprofile_details'),
    path('update-profile/', views.update_profile, name='update_profile'),


]