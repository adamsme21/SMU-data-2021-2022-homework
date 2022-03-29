from flask import Flask, render_template, redirect
from mongoHelper import MongoHelper
from scrape_mars import ScrapingHelper

app = Flask(__name__)

# init helper classes
mongo = MongoHelper()
scraper = ScrapingHelper()

@app.route("/")
def home():
    data_list = list(mongo.db.mars_data.find())

    # Return template and data
    return render_template("index.html", mars_info=data_list)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    data = scraper.getData()

    mongo.insertData(data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)