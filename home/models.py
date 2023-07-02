from django.db import models
import os


def upload_juvenile_image(instance, filename):
    base_filename, ext = os.path.splitext(filename)
    directory = 'juveniles/{}'.format(instance.name)
    filepath = '{}/{}{}'.format(directory, base_filename, ext)
    return filepath


def upload_more_images(instance, filename):
    base_filename, ext = os.path.splitext(filename)
    juvenile = instance.juvenile
    directory = 'juveniles/{}'.format(juvenile.name)
    filepath = '{}/{}{}'.format(directory, base_filename, ext)
    return filepath


SEX_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class Juvenile(models.Model):
    name = models.CharField(max_length=100)
    juvenile_img = models.ImageField(upload_to=upload_juvenile_image)
    sex = models.CharField(choices=SEX_CHOICES, max_length=10)
    age = models.IntegerField()
    dob = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    address = models.TextField()
    missing = models.BooleanField(default=False)
    missing_date = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to=upload_more_images, null=True, blank=True)
    juvenile = models.ForeignKey(Juvenile, on_delete=models.CASCADE, null=True, related_name='more_images')

    def __str__(self):
        return str(self.image)