from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class ProjectTypes(models.Model):
    PROJECT_TYPE = [
        ('RP','Research Projects'),
        ('DP','Development Projects'),
        ('MP','Maintenance Projects'),
        ('EP','Exploratory Projects'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=PROJECT_TYPE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name 
    

#One to Many

class ProjectReview(models.Model):
    project = models.ForeignKey(ProjectTypes, on_delete=models.CASCADE, 
                                related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.user.username} review for {self.project.name}'
    
# Many to Many
class Deployment(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    project_deployments = models.ManyToManyField(ProjectTypes, related_name="deployments") 

    def __str__(self):
        return self.name
    
# One to One 
class ProjectCertificate(models.Model):
    project = models.OneToOneField(ProjectTypes, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.project}'