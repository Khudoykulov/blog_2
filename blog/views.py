from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog


def blog_single_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        'blog': blog
    }
    return render(request, 'single.html', context)


