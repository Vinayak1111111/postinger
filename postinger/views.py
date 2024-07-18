from django.shortcuts import render
from .models import posts
from .forms import postform, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def home(request):
    return render(request, 'postit/home.html')

def index(request):
    return render(request, 'postit/index.html')

def post_list(request):
    post = posts.objects.all().order_by('-created_at')
    return render(request, 'postit/post_list.html', {'post':post})

@login_required
def create_post(request):
    if request.method == 'POST':
       form = postform(request.POST, request.FILES)
       if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else :
        form = postform()
    return render(request,'postit/post_form.html', {'form':form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(posts, pk=post_id, user = request.user)
    if request.method == 'POST':
       form = postform(request.POST, request.FILES, instance=post)
       if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else :
        form = postform(instance=post)
    return render(request,'postit/post_form.html', {'form':form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(posts, pk=post_id, user = request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'postit/delete_confirmation.html',{'post' : post})


def register(request):
    if request.method =='POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('post_list')
    else:
        form = UserRegistrationForm() 
    return render(request, 'registration/register.html', {'form':form})


def search(request):
    query = request.GET['query']
    # allpost = posts.objects.all()
    allpost = posts.objects.filter(caption__icontains = query)
    # post = posts.objects.all().order_by('-created_at')
    
    return render(request, 'postit/searchresult.html',{'allpost':allpost})