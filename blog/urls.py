from django.urls import path
from .views import (
    blog_single_view
)
app_name = 'blog'


urlpatterns = [
    path('detail/<slug:slug>', blog_single_view, name='detail')
]
