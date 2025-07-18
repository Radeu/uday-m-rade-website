from flask import Flask, render_template, url_for
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', year=datetime.now().year)

@app.route('/career')
def career():
    return render_template('career.html', year=datetime.now().year)

@app.route("/lifestyle")
def lifestyle():
    return render_template("lifestyle.html", year=datetime.now().year)

@app.route("/lifestyle/fitness")
def lifestylefitness():
    return render_template("lifestylefitness.html", year=datetime.now().year)

@app.route("/lifestyle/travel")
def lifestyletravel():
    return render_template("lifestyletravel.html", year=datetime.now().year)

# List of valid cities
travel_cities = ['sandiego', 'chicago', 'lax', 'sfo', 'indy', 'slc','miami','nyc','agra','delhi','amritsar','jandk']

@app.route("/lifestyle/travel/<city>")
def travel_city(city):
    if city not in travel_cities:
        return "City not found", 404

    folder = os.path.join("static", "Lifestyle", "Travel", city)
    images = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif','heif','heic'))]
    image_urls = [url_for('static', filename=f"Lifestyle/Travel/{city}/{img}") for img in images]
    return render_template(f"travel/travel{city}.html", image_urls=image_urls, year=datetime.now().year)

@app.route("/lifestyle/hobbies")
def lifestylehobbies():
    folder = os.path.join("static", "Lifestyle", "Hobbies", "Cooking")
    image_files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    image_urls = [url_for('static', filename=f"Lifestyle/Hobbies/Cooking/{img}") for img in image_files]
    return render_template("lifestylehobbies.html", Cooking_items=image_urls, year=datetime.now().year)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
