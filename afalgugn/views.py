from django.shortcuts import render
from django.http import HttpResponse
from afalgugn.models import *
from .forms import *



# Create your views here.
def indexf(req):
    founditems = FoundItem.objects.all()
    context = {"founditems":founditems}
    return render(req, 'indexf.html', context)

def indexl(req):
    lostitems = LostItem.objects.all()
    context = {"lostitems":lostitems}
    return render(req, 'indexl.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']

            user = CustomUser.objects.create_user(username=username, password=password, email=email)


            return redirect('user_login')  
    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('indexf')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('indexf')