from django.shortcuts import render
from .models import BlogPost as Post  # or your relevant model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import BlogPost, Like
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

def homepage(request):
    posts = Post.objects.all().order_by('-created_at')
    comment_forms = {post.id: CommentForm() for post in posts}
    return render(request, 'blog/home.html', {
        'posts': posts,
        'comment_forms': comment_forms,
    })



@login_required
def toggle_like(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    liked = False
    like_obj = Like.objects.filter(post=post, user=request.user).first()
    if like_obj:
        like_obj.delete()
    else:
        Like.objects.create(post=post, user=request.user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'likes_count': post.likes.count()
    })

@login_required
def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
    return redirect('homepage')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now login.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})