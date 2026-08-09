from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("experience", views.experience, name="experience"),
    path("projects", views.projects, name="projects"),
    path("stack", views.stack, name="stack"),
    path("blog", views.blog, name="blog"),
    path("blog/<slug:slug>", views.blog_post, name="blog_post"),
    path("learnings", views.learnings, name="learnings"),
    path("contact", views.contact, name="contact"),
]
