from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import Post


# def my_login(request):
#     print(request)
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#     else:
#         return("what the fuck")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return index(request)
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def index(request):
    latest_posts = Post.objects.order_by('-post_publish_date')
    context = {'latest_posts': latest_posts}
    print("about to send new posts")
    return render(request, 'SocialBoard/index.html', context)

@csrf_protect
def new_post(request):
    post_title = request.POST.get("title")
    post_publish_date = timezone.now()
    post_content = request.POST.get("content")
    post_author = request.POST.get("author")
    post = Post.objects.create(post_title=post_title, post_publish_date=post_publish_date,post_content=post_content, post_author=post_author)
    latest_posts = Post.objects.order_by('-post_publish_date')
    print(latest_posts)
    context = {'latest_posts': latest_posts}
    print("about to send new posts")
    return render(request, 'SocialBoard/index.html', context)