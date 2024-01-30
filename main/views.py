from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from .models import Contact
from .form import ContactForm
from django.contrib import messages
from blog.models import AboutMe, Blog, Services, Results


def main_index(request):
    results = Results.objects.all()
    services = Services.objects.all()
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

    }
    return render(request, 'main/index.html', content)
