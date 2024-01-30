from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils import timezone
from django.db.models.signals import pre_save


class AboutMe(models.Model):
    lname = models.CharField(max_length=123, null=False, blank=False)
    name = models.CharField(max_length=123)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    image_my = models.ImageField(upload_to='images/', null=True, blank=True)
    tel = PhoneNumberField(null=True, blank=True, region="UZ",)
    address = models.TextField()
    birth = models.DateField()
    project_count = models.IntegerField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Partners(models.Model):
    AboutMe = models.ForeignKey(AboutMe, on_delete=models.CASCADE, null=True, blank=True, related_name='partners')
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class Tags(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(AboutMe, on_delete=models.SET_NULL, null=True, blank=True, related_name='author')
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories')
    tags = models.ManyToManyField(Tags, related_name='tags')
    name = models.CharField(max_length=123)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    header_content = RichTextField(null=True, blank=True)
    footer_content = RichTextField(null=True, blank=True)
    author_message = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=123, unique=True)

    def __str__(self):
        return self.name


class Subblog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True, related_name='subblog')
    name = models.CharField(max_length=123)
    content = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    name = models.CharField(max_length=123)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    author = models.ForeignKey(AboutMe, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=123)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profession(models.Model):
    author = models.ForeignKey(AboutMe, on_delete=models.SET_NULL, null=True, blank=True, related_name='profession')
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Results(models.Model):
    UNIT = (
        (0, 'Education'),
        (1, 'Experience'),
        (3, 'Awards')
    )
    unit = models.IntegerField(choices=UNIT, default=0)
    name = models.CharField(max_length=123)
    company = models.CharField(max_length=123)
    created_time = models.DateTimeField()
    deleted_time = models.DateTimeField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


def blog_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name + " - " + timezone.now().date().strftime('%Y-%m-%d %H:%M:%S.%f'))


pre_save.connect(blog_pre_save, sender=Blog)
