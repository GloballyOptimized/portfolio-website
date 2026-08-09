from django.shortcuts import render
from django.http import HttpResponse

from data.cv_data import PROFILE, SKILLS, EXPERIENCE, PROJECTS, BLOG_POSTS, EDUCATION, BOOKS, BLOGS_AND_VLOGS


def home(request):
    portfolio_projects = [p for p in PROJECTS if p.get("category") == "portfolio"]
    return render(request, "index.html", {
        "profile": PROFILE,
        "projects": portfolio_projects[:4],
        "posts": BLOG_POSTS[:2],
        "active": "home",
    })


def experience(request):
    return render(request, "experience.html", {
        "experience": EXPERIENCE,
        "education": EDUCATION,
        "active": "experience",
    })


def projects(request):
    return render(request, "projects.html", {
        "projects": PROJECTS,
        "active": "projects",
    })


def stack(request):
    return render(request, "stack.html", {
        "skills": SKILLS,
        "active": "stack",
    })


def blog(request):
    return render(request, "blog.html", {
        "posts": BLOG_POSTS,
        "active": "blog",
    })


def blog_post(request, slug):
    post = next((p for p in BLOG_POSTS if p["slug"] == slug), None)
    if not post:
        return HttpResponse("<h1>Post not found</h1>", status=404)
    return render(request, "blog_post.html", {
        "post": post,
        "active": "blog",
    })


def learnings(request):
    return render(request, "learnings.html", {
        "education": EDUCATION,
        "books": BOOKS,
        "blogs_and_vlogs": BLOGS_AND_VLOGS,
        "active": "learnings",
    })


def contact(request):
    return render(request, "contact.html", {
        "profile": PROFILE,
        "active": "contact",
    })
