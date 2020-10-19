from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=30)
    bio = models.CharField(max_length=150)
    profile_photo = CloudinaryField('image')

    def save_category(self):
         self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_bio(cls, id, bio):
        cls.objects.filter(id=id).update(bio=bio)

    @classmethod
    def update_username(cls, id, username):
        cls.objects.filter(id=id).update(username=username)


    def __str__(self):
        return self.username

class Photo(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.bio

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def update_caption(cls, id, caption):
        cls.objects.filter(id=id).update(caption=caption)
