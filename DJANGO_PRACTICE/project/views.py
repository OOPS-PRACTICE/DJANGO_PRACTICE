from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ProjectTypes
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

def all_projects(request):
    projects = ProjectTypes.objects.all()
    return render(request,'project/index.html', {'projects':projects})

def project_details(request, project_id):
    prj= get_object_or_404(ProjectTypes, pk=project_id)
    return render(request, 'project/project_details.html', {'project': prj})

def project_deployment_view(request):
    return render(request, 'project/project_deployments.html')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_api(request):
    return Response({
        "message": "JWT working!",
        "user": request.user.username
    }) 