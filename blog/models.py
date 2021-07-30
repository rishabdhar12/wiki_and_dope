from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	content = RichTextField(null=True, blank=True)
	published_at = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(default='default.png', upload_to='images')


	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-published_at"]