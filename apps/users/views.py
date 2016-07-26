from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def login_page(request):
	return render(request, "users/login_page.html")

def login(request):
	if request.method != "POST":
		return redirect("login_page")

	user = User.objects.filter(username=request.POST["username"])
	if not user:
		return redirect("login_page")
	else:
		user = user[0]

	request.session["id"] = user.id

	return redirect("travels")

def register(request):
	if request.method != "POST":
		return redirect("login_page")

	user = User.objects.filter(username=request.POST["username"])
	if user:
		return redirect("login_page")
	else:
		user = User.objects.create(name=request.POST["name"], password=request.POST["password"], username=request.POST["username"])

	request.session["id"] = user.id

	return redirect("travels")

def logout(request):
	request.session.clear()
	return redirect("login_page")