from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Blog, Categories, Tags, Comments
from .form import CommentForm
from django.contrib import messages


def blog_single_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = Comments.objects.filter(blog=blog)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog = blog
            form.save()
            messages.success(request, 'You have successfully commentary')
            return redirect('main:index')
    blogs_margin = Blog.objects.order_by('-id')[:2]
    categories = Categories.objects.all()
    tags = Tags.objects.all()
    context = {
        'blog': blog,
        'categories': categories,
        'tags': tags,
        'blogs_margin': blogs_margin,
        'form': form,
        'comments': comments,
    }
    return render(request, 'single.html', context)


def blog_list_view(request):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    sorch = request.GET.get('sorch')
    blogs = Blog.objects.order_by('-id')
    if cat:
        blogs = blogs.filter(category__name__exact=cat)
    if tag:
        blogs = blogs.filter(tags__name__exact=tag)
    if sorch:
        blogs = blogs.filter(name__icontains=sorch)
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)



