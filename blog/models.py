from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	content = models.TextField()
	published_at = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-published_at"]