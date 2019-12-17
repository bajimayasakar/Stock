from django.db import models

#database creation, but first creating class called Stock
class Stock(models.Model):
	ticker = models.CharField(max_length=10) #CharField is  a database datatype.
	
	def __str__(self):
		return self.ticker