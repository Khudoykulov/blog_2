from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class AboutMe(models.Model):
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
