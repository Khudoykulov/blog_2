from django.urls import path
from .views import (
    blog_single_view,
    blog_list_view,
)
app_name = 'blog'


urlpatterns = [
    path('detail/<slug:slug>/', blog_single_view, name='detail'),
    path('list/', blog_list_view, name='list'),

]
