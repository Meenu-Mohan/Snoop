from django.db import models
from django.contrib.auth.models import AbstractUser
import os

def upload_to(instance, filename):
    # Get the filename and extension
    base_filename, ext = os.path.splitext(filename)
    # Construct the directory path using the instance name
    directory = 'profile/{}'.format(instance.name)
    # Construct the full file path
    filepath = '{}/{}{}'.format(directory, base_filename, ext)
    return filepath

# Create your models here.
class CustomUser(AbstractUser):
    # Add your custom fields here
    name = models.CharField(max_length=50, null=False, blank=False)
    sex = models.CharField(max_length=10)
    mobile = models.CharField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_to, default='profile/default.png')
    address = models.CharField(max_length=255)

    # Optionally, add any additional methods or customization as needed

    # Update the Meta class to set the table name
    class Meta:
        db_table = 'auth_user'
