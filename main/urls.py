from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view, name="index"),
    path('index_two_view', index_two_view, name="index_two_view"),
    path('blog_view/<int:pk>/', blog_view, name="blog"),
    path('blog_details_view', blog_details_view, name="blog_details_view"),
]