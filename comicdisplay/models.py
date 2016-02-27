from django.db import models

# Create your models here.
class Comic(models.Model):
	comic_title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	comicfile = models.ImageField(upload_to='comicfiles/')

	def __str__(self):
		return self.comic_title