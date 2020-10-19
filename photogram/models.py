from django.db import models

# Create your models here.
class Profile(models.Model):
    bio = models.CharField(max_length=150)

    def save_category(self):
         self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.bio

class Photo(models.Model):
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile)
    likes = models.CharField()
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.bio