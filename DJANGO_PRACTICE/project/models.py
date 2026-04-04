from django.db import models
from django.utils import timezone

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

    def __str__(self):
        return self.name