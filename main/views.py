from django.shortcuts import render, redirect
from .models import Contact
from .form import ContactForm
from django.contrib import messages
from blog.models import AboutMe


def main_index(request):
    about = AboutMe.objects.order_by('-id')[0]
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST,)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered')
            return redirect('/')
    content = {
        'form': form,
        'about': about
    }
    return render(request, 'main/index.html', content)
