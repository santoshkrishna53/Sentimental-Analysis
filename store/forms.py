from django import forms

from .models import reviews

class reviewform(forms.ModelForm):
	
	class Meta:
		model = reviews
		fields = [
		'title',
		'product_name',
		#'product',
		'review',
		#'positive_percentage',
		#'negative_percentage',
		'author'

		]