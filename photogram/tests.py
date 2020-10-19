from django.test import TestCase
from .models import Profile,Photo
from .models import Profile,Photo
# Create your tests here.
class TestPhoto(TestCase):
    #set up
    def setUp(self):
        self.newProfile = Profile(username='Abdi')
        self.newProfile.save_profile()
        
        self.newImage = Photo(name = 'First image',caption = 'This is the first image.',likes = 0,comments = 'lit')

        self.newImage.save_photo()
        self.newImage.Profile.add(self.newProfile)

    def tearDown(self):
        Photo.objects.all().delete()
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.newImage, Photo))

    def test_delete_photo(self):
        self.newImage.delete_photo()
        Photo = Photo.objects.all()
        self.assertTrue(len(Photo) == 0)

    def test_save_photo(self):
        self.newImage.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos)>0)
    
    def test_update_caption(self):
        self.newImage.save_photo()
        image = Photo(name = 'Abdi2',caption='This is the first of all images',likes = 0,comments = 'lit')
        image.save_photo()
        new_caption = 'Yeah it is the first'
        image.update_caption(image.pk,new_caption)
        self.assertEqual(image.caption,'Yeah it is the first')





    
