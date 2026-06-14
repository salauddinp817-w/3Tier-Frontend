from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

// UPDATE THIS localhost with BACKEND IP
BACKEND_URL = "http://localhost:3000/tasks"

@app.route("/")
def home():
    tasks = requests.get(BACKEND_URL).json()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    requests.post(BACKEND_URL, json={"title": title})
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    requests.delete(f"{BACKEND_URL}/{id}")
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
