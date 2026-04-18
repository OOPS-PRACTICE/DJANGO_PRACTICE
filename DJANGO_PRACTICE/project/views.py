from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ProjectTypes
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .forms import ProjectTypesForm

# Create your views here.

def all_projects(request):
    projects = ProjectTypes.objects.all()
    return render(request,'project/index.html', {'projects':projects})

def project_details(request, project_id):
    prj= get_object_or_404(ProjectTypes, pk=project_id)
    return render(request, 'project/project_details.html', {'project': prj})

# def project_deployment_view(request):
#     servers = None
#     if request.method == 'POST':
#         form = ProjectTypesForm(request.POST)
#         if form.is_valid():
#             # Data is safe! Access it via cleaned_data
#             project_type = form.cleaned_data['project_type']    
#     return render(request, 'project/project_deployments.html', {'servers':servers})


def create_project_type(request):
    if request.method == 'POST':
        form = ProjectTypesForm(request.POST)
        if form.is_valid():
            ProjectTypes.objects.create(
                name=form.cleaned_data['name']
            )
    else:
        form = ProjectTypesForm()

    return render(request, 'project/project_type_form.html', {'form': form})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_api(request):
    return Response({
        "message": "JWT working!",
        "user": request.user.username
    }) 