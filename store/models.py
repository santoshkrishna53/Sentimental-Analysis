from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class products(models.Model):
	product = models.CharField(max_length=100, unique=True)
	product_description = models.CharField(max_length=1000)
	overall_rating = models.IntegerField()
	neg_rating = models.IntegerField(default=0)
	product_id = models.CharField(max_length=3,unique=True)
	image = models.ImageField(upload_to='product_img', blank=True)
	#tst = models.CharField(max_length=10)
	class Meta:
		ordering = ['neg_rating']

class reviews(models.Model):
	title = models.CharField(max_length=100)
	#product_id = models.CharField(max_length=4)
	product_name = models.CharField(max_length=4, unique=True)
	#product =  models.ForeignKey(products, on_delete=models.CASCADE)
	review = models.CharField(max_length=100)
	total_score = models.IntegerField()
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=50)
