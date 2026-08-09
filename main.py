from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from data.cv_data import PROFILE, SKILLS, EXPERIENCE, PROJECTS, BLOG_POSTS, EDUCATION, BOOKS, BLOGS_AND_VLOGS

app = FastAPI(title="Ayush Suryawanshi — Portfolio")

@app.get("/debug/blogs")
async def debug_blogs():
    return BLOGS_AND_VLOGS

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    portfolio_projects = [p for p in PROJECTS if p.get("category") == "portfolio"]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "profile": PROFILE,
        "projects": portfolio_projects[:4],
        "posts": BLOG_POSTS[:2],
        "active": "home",
    })


@app.get("/experience", response_class=HTMLResponse)
async def experience(request: Request):
    return templates.TemplateResponse("experience.html", {
        "request": request,
        "experience": EXPERIENCE,
        "education": EDUCATION,
        "active": "experience",
    })


@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {
        "request": request,
        "projects": PROJECTS,
        "active": "projects",
    })


@app.get("/stack", response_class=HTMLResponse)
async def stack(request: Request):
    return templates.TemplateResponse("stack.html", {
        "request": request,
        "skills": SKILLS,
        "active": "stack",
    })


@app.get("/blog", response_class=HTMLResponse)
async def blog(request: Request):
    return templates.TemplateResponse("blog.html", {
        "request": request,
        "posts": BLOG_POSTS,
        "active": "blog",
    })


@app.get("/blog/{slug}", response_class=HTMLResponse)
async def blog_post(request: Request, slug: str):
    post = next((p for p in BLOG_POSTS if p["slug"] == slug), None)
    if not post:
        return HTMLResponse("<h1>Post not found</h1>", status_code=404)
    return templates.TemplateResponse("blog_post.html", {
        "request": request,
        "post": post,
        "active": "blog",
    })


@app.get("/learnings", response_class=HTMLResponse)
async def learnings(request: Request):
    return templates.TemplateResponse("learnings.html", {
        "request": request,
        "education": EDUCATION,
        "books": BOOKS,
        "blogs_and_vlogs": BLOGS_AND_VLOGS,
        "active": "learnings",
    })


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {
        "request": request,
        "profile": PROFILE,
        "active": "contact",
    })
