from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class comments(models.Model):
    comment = models.CharField(max_length = 30)

    def __str__(self):
        return self.comment

class Profile(models.Model):
    bio = models.CharField(max_length=150)
    profile_photo = CloudinaryField('image')
    comments = models.ManyToManyField(comments)
    def save_profile(self):
         self.save()

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def update_bio(cls, id, bio):
        prof = cls.objects.filter(id=id).first()
        prof.bio = bio
        prof.save()


    def __str__(self):
        return self.username

class Photo(models.Model):
    image = CloudinaryField('image')
    caption = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    likes = models.IntegerField(default=0)
    comments = models.ManyToManyField(comments)

    class Meta:
        ordering = ['caption',]
    

    def __str__(self):
        return self.bio

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def update_caption(cls, id, caption):
        cls.objects.filter(id=id).update(caption=caption)


