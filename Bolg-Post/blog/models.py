from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	body = models.TextField()
	image_file = models.ImageField(upload_to='images/',null=True,blank=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail',args=(str(self.id)))

	