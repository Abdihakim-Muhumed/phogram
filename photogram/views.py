from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Photo,comments,Following
from .forms import NewPhotoForm,EditProfileForm
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    photos = Photo.objects.all()
    all_comments = comments.objects.all()
    return render(request,'index.html',{"photos":photos,"all_comments":all_comments})
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    try:
        profile = Profile.objects.filter(user = current_user).first()
    except:
        return redirect('edit-profile')
    photos = Photo.objects.filter(user = current_user).all()
    posts = photos.count()
    followings = Following.objects.filter(profile = profile).all()
    following = followings.count()
    all_followers = Following.objects.filter(user = current_user).all()
    followers = all_followers.count()
    return render(request,'profile.html',{"profile":profile,"photos":photos,"current_user":current_user,"posts":posts,"following":following,"followers":followers})

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

@login_required(login_url='/accounts/login/')
def comment(request,photo_id):

    if 'comment' in request.GET and request.GET["comment"]:
        comment = request.GET.get("comment")
        new_comment = comments(comment = comment)
        new_comment.user = request.user
        comment_photo = Photo.objects.filter(id= photo_id).first()
        new_comment.photo = comment_photo
        new_comment.save()
    return redirect('index')


@login_required(login_url='/accounts/login/')
def like_photo(request,photo_id):
    photo = Photo.objects.filter(id = photo_id).first()
    photo.likes +=1
    photo.save()
    return redirect('index')
@login_required(login_url='/accounts/login/')
def follow_user(request,user_id):
    current_user = request.user
    profile = Profile.objects.filter(user = current_user).first()
    user = User.objects.filter(id=user_id).first()
    follow = Following(profile = profile,user = user)
    follow.save()
    return redirect('people')

@login_required(login_url='/accounts/login/')
def people(request):
    profiles = Profile.objects.all()
    return render(request,'people.html',{"profiles":profiles})