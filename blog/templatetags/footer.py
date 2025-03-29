from django import template
from blog.models import AboutMe


register = template.Library()


@register.simple_tag
def footer_author():
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
    try:
        about = AboutMe.objects.order_by('-id')[0]
    except IndexError:
            about = default_about
    return about



