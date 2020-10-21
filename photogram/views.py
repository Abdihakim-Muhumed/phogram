from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Photo
from .forms import NewPhotoForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')

@login_required(login_url='/accounts/login/')
def new_photo(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = current_user
            photo.save()
        return redirect('index')

    else:
        form = NewPhotoForm()
    return render(request, 'new_photo.html', {"form": form})