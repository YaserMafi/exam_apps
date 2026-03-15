from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# صفحه اصلی (فرم)
@app.route("/")
def home():
    return render_template("index.html")


# ثبت جواب‌ها
@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name")
    age = request.form.get("age")
    q1 = request.form.get("q1")

    time = datetime.datetime.now()

    with open("answers.txt", "a", encoding="utf-8") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Answer: {q1}\n")
        f.write(f"Time: {time}\n")
        f.write("----------------------\n")

    return "جواب ثبت شد"


# دیدن جواب‌ها
@app.route("/answers")
def show_answers():
    with open("answers.txt","r",encoding="utf-8") as f:
        data = f.read()
    return "<pre>" + data + "</pre>"


if __name__ == "main":
    app.run(host="0.0.0.0", port=5000)
