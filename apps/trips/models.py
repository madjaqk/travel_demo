from django.db import models
from ..users.models import User

# Create your models here.
class Trip(models.Model):
	destination = models.TextField(max_length=255)
	description = models.TextField(max_length=1000)
	travelto = models.DateField()
	travelfrom = models.DateField()
	creator = models.ForeignKey(User, related_name="creator")
	travellers = models.ManyToManyField(User, related_name="travellers")