from django.db import models

# Create your models here.


class PostModel(models.Model):
	nama = models.CharField(max_length = 50)
	komentar =  models.CharField(max_length= 200)

	published = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return "{}. {}".format(self.id, self.nama )