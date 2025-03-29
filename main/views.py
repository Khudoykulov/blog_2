from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Contact
from .form import ContactForm
from django.contrib import messages
from blog.models import AboutMe, Blog, Services, Results, Skills


def main_index(request):
    default_about = {
        "lname": "Default Last Name",
        "name": "Default Name",
        "email": "example@example.com",
        "message": "No message available",
        "image_my": None,
        "tel": None,
        "address": "No address provided",
        "birth": "2000-01-01",
        "project_count": 0,
        "zip_code": 100000,
        "awards": 0
    }
    skills = Skills.objects.all()
    results = Results.objects.all()
    services = Services.objects.all()
    blog_all = Blog.objects.all()
    blogs = Blog.objects.order_by('-id')[:3]
    try:
        about = AboutMe.objects.order_by('-id')[0]
    except IndexError:
        about = default_about
    contacts = Contact.objects.all().count()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST,)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered')
            return redirect('/')
    content = {
        'form': form,
        'about': about,
        'blogs': blogs,
        'services': services,
        'contacts': contacts,
        'results': results,
        'skills': skills,
        'blog_all': blog_all

    }
    return render(request, 'main/index.html', content)
