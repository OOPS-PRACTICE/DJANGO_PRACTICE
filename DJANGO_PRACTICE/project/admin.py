from django.contrib import admin
from .models import ProjectTypes, ProjectReview, ProjectCertificate, Deployment
# Register your models here.

class ProjectReviewInline(admin.TabularInline):
    model = ProjectReview
    extra = 2

class ProjectTypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added') 
    inlines = [ProjectReviewInline]

class DeploymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location') 
    filter_horizontal = ('project_deployments',)

class ProjectCertificateAdmin(admin.ModelAdmin):
    list_display = ('project', 'certificate_number')      

# admin.site.register(ProjectTypes)
admin.site.register(ProjectTypes,ProjectTypesAdmin)
admin.site.register(Deployment,DeploymentAdmin)
admin.site.register(ProjectCertificate,ProjectCertificateAdmin)
