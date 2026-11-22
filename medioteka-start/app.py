"""Локальный учебный стенд. Запуск: python app.py."""
from flask import Flask, render_template, request, abort
from catalog import load_catalog, search_items, filter_by_category, total_duration, duration_label

app = Flask(__name__)
app.jinja_env.filters["duration"] = duration_label

@app.get("/")
def index():
    all_items = load_catalog()
    query = request.args.get("q", "")
    category = request.args.get("category", "")
    items = filter_by_category(search_items(all_items, query), category)
    return render_template("index.html", items=items, query=query, category=category,
                           categories=sorted({x["category"] for x in all_items}),
                           duration=total_duration(items))

@app.get("/video/<int:item_id>")
def video(item_id):
    item = next((x for x in load_catalog() if x["id"] == item_id), None)
    if item is None:
        abort(404)
    return render_template("video.html", item=item)

@app.get("/lab")
def lab():
    return render_template("lab.html")

@app.get("/privacy")
def privacy():
    return render_template("privacy.html")

@app.get("/ads")
def ads():
    return render_template("ads.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    message = "Форма учебная. Вводите только вымышленные данные."
    if request.method == "POST":
        message = "Учебная отправка выполнена. Аккаунт и сеанс входа не создаются."
    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
