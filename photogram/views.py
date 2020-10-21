from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Photo
from .forms import NewPhotoForm,EditProfileForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'index.html')
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    try:
        profile = Profile.objects.filter(user = current_user).first()
        photos = Profile.objects.filter(user = current_user).all()
        return render(request,'profile.html',{"profile":profile,"photos":photos,"current_user":current_user})
    except:
        return redirect('edit-profile')

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = EditProfileForm()
    return render(request, 'edit_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_photo(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = current_user
            photo.save()
        return redirect('profile')

    else:
        form = NewPhotoForm()
    return render(request, 'new_photo.html', {"form": form})