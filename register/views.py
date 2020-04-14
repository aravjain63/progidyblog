from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm,ProfileForm,UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .models import Profile


def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts/login')
	else:
	    form = RegisterForm()
	return render(request, "register/register.html", {"form":form})

def user_details(request):		
	return render(request,'profile/profile_p.html')

@login_required(login_url = '/login')
def update_profile(request):
	if request.method == "POST":
		user_form = UserForm(request.POST,instance=request.user)
		profile_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('/profile')
	else:
		user_form = UserForm(request.POST,instance = request.user)
		profile_form = ProfileForm(request.POST,request.FILES,instance = request.user.profile)
	return render(request,'profile/update.html',{'user_form':user_form,'profile_form':profile_form})

@login_required(login_url = '/login')
def delete_image(request):
	user = User.objects.get(username = request.user.username)
	if request.method == "POST":
		user.profile.image.delete()
	return render(request,'profile/profile_p.html')
def login(request):
	if request.user_is.authenticated():
		return redirect('/')
	return render(request,'registration/login.html')



	



