from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import reviews, products
from django.views.generic.edit import CreateView
from .forms import reviewform
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# Create your views here.
def pro_score():
    for product in products.objects.all():
        su =0
        for review in reviews.objects.all():
            if review.product_name==product.product_id:
                sc = review.total_score
                su = su + sc
        print(su)
        nu = -su
        print(nu)
        product.overall_rating = su
        products.objects.filter(product_id=product.product_id).update(overall_rating=su) 
        products.objects.filter(product_id=product.product_id).update(neg_rating=nu) 


def sentiment(s):
    analyzer = SentimentIntensityAnalyzer()
    neg_count=0
    neg_correct=0
    pos_count = 0
    pos_correct = 0
    threshold=0.5
    vs=analyzer.polarity_scores(s)
    
    if vs['compound'] >= threshold or vs['compound'] <= -threshold:
        if vs['compound']>0:
            pos_correct +=1
        
        
    if vs['compound'] >= threshold or vs['compound'] <= -threshold:
        if vs['compound']<=0:
            neg_correct +=1
        
    if vs['compound'] <= threshold or vs['compound'] >= -threshold:
        if vs['compound']>0.4:
            pos_correct+=1
        if vs['compound']<-0.4:
            neg_correct+=1
    
    if pos_correct>neg_correct:
        return 1
    elif neg_correct>pos_correct:
        return -1
    else:
    	return 0


def home(request):
    pro_score()
    context = {
	'products' : products.objects.all()
	}
    return render(request, 'store/index.html',context)

def product1(request, id):
	#form = reviewform(request.POST or None)
    if request.user.is_authenticated:
        if request.POST.get('review')!=None:
            print(request.user.username)
            r = reviews()
            r.author = request.user.username
            r.product_name = id
            review = str(request.POST.get('review'))
            r.review =review
            score = sentiment(review)
            r.total_score = score
            r.save()
            print(score) 

	#if form.is_valid():
		#form.save()
		#print('this is working')
		#if request.user.is_authenticated:
		#	print(request.user.username)
		#for review in reviews.objects.all():
		#	print(sentiment(review.review))

    context = {
	'reviews' : reviews.objects.all(),
	'products': products.objects.filter(product_id= id),
    'pro_id': id
	}
    return render(request, 'store/products/product1.html',context)
	
	
