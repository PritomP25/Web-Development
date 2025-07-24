from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html",num=random_num, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender_given = gender_data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age_given = age_data["age"]


    return render_template("guess.html",username=name, gender=gender_given, age=age_given)


# @app.route("/blog")
# def blog():


if __name__ == "__main__":
    app.run(debug=True)


