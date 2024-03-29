from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		#pk_41bb53754d8446b99174a8813fbec2c3
		#api request garne through above code
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_41bb53754d8446b99174a8813fbec2c3")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
			
		return render(request,'home.html', {'api': api})

	else:
		return render(request,'home.html', {'ticker': "Enter a ticker symbol above..."})

	

def about(request):
	return render(request,'about.html', {})

def add_stock(request):

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added"))
			return redirect('add_stock')
	else:	
		ticker = Stock.objects.all()
		return render(request,'add_stock.html', {'ticker': ticker})