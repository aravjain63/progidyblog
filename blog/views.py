from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm





# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    #post_author_name = Post.author_name
    return render(request, 'blog/post_detail.html', {'post' : post})
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) 
            post.author_name = request.user
          # post.pub_date = timezone.now() 
            post.save()
            return redirect('post_detail', pk=post.pk)   
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk= pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author_name = request.user
            #post.pub_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post_new.html', {'form': form})

def bookmark(request):
    posts = Post.object.all().filter(author_name = request.user)
    return render(request, 'blog/bookmark.html', {'posts': posts})

