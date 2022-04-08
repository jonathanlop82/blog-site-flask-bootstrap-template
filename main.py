from flask import Flask
from flask import render_template
import requests

URL = "https://api.npoint.io/fac1592d674bdb8082a8"

app = Flask(__name__)

@app.route('/')
def get_index():
    response = requests.get(URL)
    all_posts = response.json()
    return render_template('index.html', posts=all_posts)

@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route('/contact')
def get_contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def get_post(id):
    response = requests.get(URL)
    all_posts = response.json()
    for post in all_posts:
        if post['id'] == id:
            title = post["title"]
            subtitle = post["subtitle"]
            date = post["date"]
            author = post["author"]
            body = post["body"]
            return render_template("post.html", title=title, subtitle=subtitle, date=date, author=author, body=body)

if __name__ == "__main__":
    app.run(debug=True)