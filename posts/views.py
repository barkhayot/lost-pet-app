from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Account
from .models import Post, PostComment, Category
from .forms import PostCreateForm, PostCommentForm



def GetPosts(request):
    post = Post.objects.all()

    context = {
        'posts': post
    }
    return render(request, 'posts/posts.html', context)

def PostCreate(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.author=request.user
            data.save()
            return redirect('GetPosts')
    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)

def PostDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    category = Category.objects.all()
    comment = PostComment.objects.filter(post=post).order_by('-date_posted')
    comment_form = PostCommentForm()
    if request.method == 'POST':
        comment_form = PostCommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.save(commit=False)
            data.author = request.user
            data.post = post
            data.save()
            return redirect('PostDetail', pk=post.pk)

    context = {
        'post': post,
        'comments': comment,
        'categories': category,
        'comment_form': comment_form
    }
    return render(request, 'posts/detail.html', context)
