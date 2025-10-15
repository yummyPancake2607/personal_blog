from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from article_manager import (
    get_all_articles, get_article_by_title, save_article,
    update_article, delete_article
)
import os

app = FastAPI()

# -------------------------------
# Static files and templates
# -------------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# -------------------------------
# Session middleware for admin login
# -------------------------------
app.add_middleware(SessionMiddleware, secret_key="supersecret123")  # change the secret key

# -------------------------------
# Hardcoded admin credentials
# -------------------------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# -------------------------------
# Homepage
# -------------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    articles = get_all_articles()
    for article in articles:
        content = article.get("content", "")
        article["excerpt"] = content[:150] + "..." if len(content) > 150 else content
    return templates.TemplateResponse("home.html", {"request": request, "articles": articles})

# -------------------------------
# Article page
# -------------------------------
@app.get("/article/{article_title}", response_class=HTMLResponse)
def read_article(request: Request, article_title: str):
    article = get_article_by_title(article_title)
    return templates.TemplateResponse("article.html", {"request": request, "article": article})

# -------------------------------
# Admin login
# -------------------------------
@app.get("/admin", response_class=HTMLResponse)
def admin_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@app.post("/admin", response_class=HTMLResponse)
def admin_login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        request.session["admin_logged_in"] = True
        return RedirectResponse(url="/dashboard", status_code=303)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

# -------------------------------
# Dashboard
# -------------------------------
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    if not request.session.get("admin_logged_in"):
        return RedirectResponse(url="/admin", status_code=303)
    articles = get_all_articles()
    return templates.TemplateResponse("dashboard.html", {"request": request, "articles": articles})

# -------------------------------
# Add Article
# -------------------------------
@app.get("/dashboard/add", response_class=HTMLResponse)
def add_article_page(request: Request):
    if not request.session.get("admin_logged_in"):
        return RedirectResponse(url="/admin", status_code=303)
    return templates.TemplateResponse("add_article.html", {"request": request})

@app.post("/dashboard/add", response_class=HTMLResponse)
def add_article_submit(request: Request, title: str = Form(...), content: str = Form(...)):
    save_article(title, content)
    return RedirectResponse(url="/dashboard", status_code=303)

# -------------------------------
# Edit Article
# -------------------------------
@app.get("/dashboard/edit/{article_title}", response_class=HTMLResponse)
def edit_article_page(request: Request, article_title: str):
    if not request.session.get("admin_logged_in"):
        return RedirectResponse(url="/admin", status_code=303)
    article = get_article_by_title(article_title)
    return templates.TemplateResponse("edit_article.html", {"request": request, "article": article})

@app.post("/dashboard/edit/{article_title}", response_class=HTMLResponse)
def edit_article_submit(request: Request, article_title: str, content: str = Form(...)):
    update_article(article_title, content)
    return RedirectResponse(url="/dashboard", status_code=303)

# -------------------------------
# Delete Article
# -------------------------------
@app.get("/dashboard/delete/{article_title}")
def delete_article_route(request: Request, article_title: str):
    if not request.session.get("admin_logged_in"):
        return RedirectResponse(url="/admin", status_code=303)
    delete_article(article_title)
    return RedirectResponse(url="/dashboard", status_code=303)