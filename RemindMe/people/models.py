from django.db import models


# Create your models here.

class People(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    profile = models.ImageField(upload_to='profile_image', blank=True)
    meeting_place = models.CharField(max_length=60)
    meeting_time = models.DateTimeField()
    registration_time = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='people')

    def __str__(self):
        return self.first_name + " " + self.second_name
