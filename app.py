from flask import Flask
from flask import render_template
from flask import request, redirect
import csv
app = Flask(__name__)


@app.route("/")
def render_index():
    return render_template("index.html")


@app.route("/works")
def render_works():
    return render_template("works.html")


@app.route("/work")
def render_work():
    return render_template("work.html")


@app.route("/about")
def render_about():
    return render_template("about.html")


@app.route("/contact")
def render_contact():
    return render_template("contact.html")


@app.route("/thankyou")
def render_thankyou():
    return render_template("thankyou.html")


@app.route("/submit", methods=["POST"])
def handle_form():
    formdata = request.form.to_dict()
    # with open("./database.csv", "a") as db:
    #     db.write("\n")
    #     db.write(formdata["email"]+"," +
    #              formdata["subject"] + "," + formdata["message"])

    #     db.close()
    with open("database.csv", newline='', mode="a") as db:
        csv_writer = csv.writer(
            db, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([formdata["email"],
                             formdata["subject"], formdata["message"]
                             ])
        db.close()
        return redirect("/thankyou")
