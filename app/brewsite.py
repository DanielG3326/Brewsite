from flask import Flask
from flask import render_template as rt
import requests, json, warnings
response = requests.get("https://api.openbrewerydb.org/v1/breweries")

date = json.loads(response.content)

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user = "Daniel")

@app.route("/breweries")
def breweries():
    return rt("breweries.html", content = date)


@app.route("/beer_types")
def beer_types():
    return rt("beer_types.html", user = "Daniel")


@app.route("/about")
def about():
    return rt("about.html", user = "Daniel")



if __name__ == "__main__":
    app.run(debug=True)