
from django.shortcuts import render


from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.decorators  import  login_required
from .forms import CustomForm

# Create your views here.


# def user(request):

#   return render(request, 'userAuth/user.html')


def register(request):
  page='register'
  userForm = CustomForm()
  if request.method == 'POST':
    userForm = CustomForm(request.POST)
    if userForm.is_valid():
      user = userForm.save(commit=False)
      user.save()
      login(request, user)
      return redirect('movies')
    else:
      messages.error(request, 'register error')

  context={'userForm':userForm, 'page':page}
  return render(request, 'userAuth/register.html',context)


def loginView(request):
  if request.user.is_authenticated:
    return redirect('user')

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'login error!')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('movies')
    else:
      messages.error(request, 'login credentials  missmatch!')

  context={}
  return render(request, 'userAuth/login.html',context)

def logoutView(request):
  logout(request)
  return redirect('movies')
