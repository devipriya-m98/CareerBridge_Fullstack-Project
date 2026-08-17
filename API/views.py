from django.shortcuts import render

from job.models import Job
from .serializers import JobSerializer

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status



# Create your views here.



# LIST JOBS
@api_view(['GET'])
@permission_classes([AllowAny])
def api_list_jobs(request):

    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)



# GETTING JOB BY ID
@api_view(['GET'])
@permission_classes([AllowAny])
def api_get_job(request, j_id):

    job = get_object_or_404(Job, id=j_id)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)



