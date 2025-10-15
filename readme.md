# 📝 Personal Blog with FastAPI

A simple blog management system built using **FastAPI**, **Jinja2 templates**, and **JSON-based article storage**.  
It supports:
- Adding, editing, deleting articles (admin only)
- Displaying articles on the home page
- A minimal, elegant front-end styled with CSS
- Session-based admin authentication

---

## 📂 **Project Structure**
```
├── articles/                # Folder where JSON articles are saved
├── static/                  # Static assets (CSS, images)
│   ├── hero-avatar.jpg
│   └── style.css
├── templates/               # Jinja2 HTML templates
│   ├── add_article.html
│   ├── article.html
│   ├── dashboard.html
│   ├── edit_article.html
│   ├── home.html
│   └── login.html
├── article_manager.py       # Handles CRUD operations for article storage
├── main.py                  # Main FastAPI application
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

---

## 🚀 **Features**

### 🏠 Frontend
- **Home page:** Lists all existing articles.
- **Article view:** Displays full article contents.
- **Responsive CSS design** using the *Inter* and *Playfair Display* fonts from Google Fonts.

### 🔐 Admin Functionality
- **Login system:** Protected via session handling.
- **Dashboard:** Lists all articles with *edit* and *delete* actions.
- **Add/Edit/Delete Articles** using simple forms.

### 📦 Data Storage
- Articles are stored as JSON files in the `/articles/` directory.
- Each JSON file contains:
  ```json
  {
    "title": "My Article",
    "content": "This is the content...",
    "date": "2025-02-25 17:00:00"
  }
  ```

---

## ⚙️ **Installation & Setup**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/fastapi-blog.git
cd fastapi-blog
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App
```bash
uvicorn main:app --reload
```

Then open your browser and go to ➡ **http://127.0.0.1:8000**

---

## 🔑 **Admin Access**

- **Login URL:** `/admin`
- **Default Credentials:**
  ```
  Username: admin
  Password: password
  ```
  *(You can change these in `main.py`)*

---

## 🧩 **Tech Stack**
- **Backend:** FastAPI (Python)
- **Templating:** Jinja2
- **Frontend:** HTML5, CSS3
- **Storage:** JSON Files (no database)
- **Session Management:** Starlette Sessions

---

## 🗑️ **How to Add Articles Manually**
You can create a `.json` file inside `/articles/` folder with the same structure used by `article_manager.py`.  

File names should follow this naming rule:
```
{title_in_lowercase_with_underscores}.json
```
Example:
> `"My First Blog Post"` → `my_first_blog_post.json`

---

## 📸 **Preview**

- **Home Page**
  Displays all available articles with preview cards.  
- **Dashboard**
  Shows a list of articles with action buttons (Edit/Delete).  
- **Add/Edit Forms**
  Simple text editor interface to manage blog content.

---

## ⚖️ **License**
This project is released under the **MIT License**. Feel free to reuse or modify it for your own blog.

---

## ❤️ **Author**
**Lakshit**  
Made with love and FastAPI.

