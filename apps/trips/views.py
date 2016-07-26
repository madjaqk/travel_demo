from django.shortcuts import render, redirect
from .models import Trip
from ..users.models import User

# Create your views here.
def index(request):
	if "id" not in request.session:
		return redirect("login_page")

	user = User.objects.get(id=request.session["id"])

	context = {
		"trips_on": Trip.objects.filter(creator=user) | Trip.objects.filter(travellers__id=user.id),
		"trips_off": Trip.objects.exclude(creator=user).exclude(travellers__id=user.id),
		"name": user.name,
	}
	return render(request, "trips/index.html", context)

def show(request, id):
	if "id" not in request.session:
		return redirect("login_page")

	context = {
		"trip": Trip.objects.get(id=id)
	}
	return render(request, "trips/show.html", context)

def new(request):
	if "id" not in request.session:
		return redirect("login_page")

	return render(request, "trips/new.html")

def join(request, id):
	if "id" not in request.session:
		return redirect("login_page")
	
	trip = Trip.objects.get(id=id)
	user = User.objects.get(id=request.session["id"])

	trip.travellers.add(user)

	return redirect("travels")

def create(request):
	if request.method != "POST":
		return redirect("travels")
	elif "id" not in request.session:
		return redirect("login_page")

	Trip.objects.create(destination=request.POST["destination"], description=request.POST["description"], travelfrom=request.POST["travelfrom"], travelto=request.POST["travelto"], creator=User.objects.get(id=request.session["id"]))

	return redirect("travels")