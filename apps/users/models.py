from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=45)
	password = models.CharField(max_length=155)
	username = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "User with name {}".format(self.name)