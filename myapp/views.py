from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def hello(request):
    return render(request, 'hello.html')

def homepage_view(request):
    if request.user.is_authenticated:
        # The user is logged in
        username = request.user.username
        return render(request, 'homepage.html', {'username': username})
    else:
        # The user is not logged in
        return render(request, 'login.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('homepage/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="myapp/register.html", context={"register_form":form})

def valid_login(request):
	userid = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=userid, password=password)
	
	if user is not None:
		login(request, user)
	else:
		print("Your username and password didn't match. Please try again.")

	return redirect('homepage/')