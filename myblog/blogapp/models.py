from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    photo1=models.ImageField(upload_to='photo')
    photo2=models.ImageField(upload_to='photo')
    photo3=models.ImageField(upload_to='photo')
    post_body = models.TextField()
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
