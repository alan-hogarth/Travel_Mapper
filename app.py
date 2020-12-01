from flask import Flask, render_template, request

from controllers.city_controller import cities_blueprint
from controllers.country_controller import countries_blueprint
from controllers.sight_controller import sights_blueprint
from controllers.visit_controller import trips_blueprint
import repositories.visit_repository as visit_repository

app = Flask(__name__)

app.register_blueprint(trips_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(sights_blueprint)
app.register_blueprint(countries_blueprint)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def render_results():
    city_name = request.form['city']

    api_key = visit_repository.get_api_key()
    data = visit_repository.get_weather_results(city_name, api_key)   
   
    temp = "{}".format(data["main"]["temp"]) 
    feels_like = "{}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]
    wind_speed = data["wind"]["speed"]

    return render_template('results.html',
                           location=location, temp=temp,
                           feels_like=feels_like, weather=weather, wind_speed=wind_speed)


if __name__ == '__main__':
    app.run(debug=True)