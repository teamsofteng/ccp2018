from django.shortcuts import render
def home(request):
	return render(request, 'account/Homepage.html')

