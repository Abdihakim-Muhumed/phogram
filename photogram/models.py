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
        