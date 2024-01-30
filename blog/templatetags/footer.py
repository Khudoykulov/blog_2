from django import template
from blog.models import AboutMe


register = template.Library()


@register.simple_tag
def footer_author():
    return AboutMe.objects.order_by('-id')[0]
