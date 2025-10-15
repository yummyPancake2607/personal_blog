import os
import json
from datetime import datetime

ARTICLES_DIR = "articles"

if not os.path.exists(ARTICLES_DIR):
    os.makedirs(ARTICLES_DIR)

def save_article(title: str, content: str):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"{title.lower().replace(' ', '_')}.json"
    filepath = os.path.join(ARTICLES_DIR, filename)

    article_data = {"title": title, "content": content, "date": date}

    with open(filepath, "w") as f:
        json.dump(article_data, f, indent=4)

    return {"message": "Article saved successfully!", "file": filename}

def get_all_articles():
    articles = []
    for filename in os.listdir(ARTICLES_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(ARTICLES_DIR, filename)
            try:
                with open(filepath, "r") as f:
                    articles.append(json.load(f))
            except Exception as e:
                print(f"⚠️ Error reading {filename}: {e}")
    articles.sort(key=lambda x: x["date"], reverse=True)
    return articles

def get_article_by_title(title: str):
    filename = f"{title.lower().replace(' ', '_')}.json"
    filepath = os.path.join(ARTICLES_DIR, filename)
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Error reading {filename}: {e}")
        return None

def delete_article(title: str):
    filename = f"{title.lower().replace(' ', '_')}.json"
    filepath = os.path.join(ARTICLES_DIR, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return {"message": "Article deleted successfully!"}
    return {"error": "Article not found"}

def update_article(title: str, new_content: str):
    filename = f"{title.lower().replace(' ', '_')}.json"
    filepath = os.path.join(ARTICLES_DIR, filename)
    if not os.path.exists(filepath):
        return {"error": "Article not found"}
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        data["content"] = new_content
        data["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        return {"message": "Article updated successfully!"}
    except Exception as e:
        return {"error": f"Error updating article: {e}"}
