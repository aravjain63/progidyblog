from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone, dateformat
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    print(post.author_name)
    return render(request, 'blog/post_detail.html', {'post' : post})
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) 
            post.author_name = request.user
            post.save() 
            return redirect('post_detail', pk=post.pk)   
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk= pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post_new.html', {'form': form})

def user_posts(request):
    posts = Post.objects.all().filter(author_name = request.user)
    return render(request, 'blog/user.html', {'posts': posts})

"""def user_posts_details(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/YourPost.html', {'post' : post})"""

def user_post_details_delete(request,pk):
    posts = get_object_or_404(Post,pk=pk)
    #posts.delete()
    return redirect('post_del')
    #return render(request,'blog/YourPost.html',{'posts': posts})

def user_post_details_del(request,pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Your password')
        return redirect('post_list')
    return render(request, 'blog/delete_confirm.html', {'post' : post})

def user_posts_p(reqest,pk):
    post = get_object_or_404(Post,pk = pk)
    author = post.author_name
    posts = Post.objects.all().filter(author_name = author)
    return render(reqest,'blog/YourPosts_p.html',{'posts': posts})
def del_image(request,pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        post.image.delete()
        messages.success(request, 'Your password')
        return redirect('post_detail', pk = post.pk)
    return render(request, 'blog/delete_confirm.html', {'post' : post})



