from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    principal = models.CharField(max_length=50)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):    # to redirect to detail page after creating new school
        return reverse('basic_app:detail', kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name="students")

    def __str__(self):
        return self.name
















