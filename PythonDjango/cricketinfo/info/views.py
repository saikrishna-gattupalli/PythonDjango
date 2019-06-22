from django.shortcuts import render
# Create your views here.
def home_view(request):
	return render(request, "home.html")

def player_view(request):
	return render(request, "player.html")

def country_view(request):
	return render(request, "country.html")

def create_country_view(request):
	return render(request, "create_country.html")