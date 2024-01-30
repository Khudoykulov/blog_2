from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from .models import Contact
from .form import ContactForm
from django.contrib import messages
from blog.models import AboutMe, Blog, Services, Results, Skills


def main_index(request):
    skills = Skills.objects.all()
    for skill in skills:
        if skill.unit == 0:
            print(skills)
    results = Results.objects.all()
    services = Services.objects.all()
    blog_all = Blog.objects.all()
    blogs = Blog.objects.order_by('-id')[:3]
    about = AboutMe.objects.order_by('-id')[0]
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
