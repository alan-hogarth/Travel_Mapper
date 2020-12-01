from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.visit import Visit
from models.city import City
from models.country import Country
from models.sight import Sight

import repositories.visit_repository as visit_repository
import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

trips_blueprint = Blueprint("trips", __name__)

@trips_blueprint.route("/trips")
def trips():
    trips = visit_repository.select_all() 
    return render_template("trips/index.html", trips = trips)

@trips_blueprint.route("/trips/new", methods=['GET'])
def new_trip():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    sights = sight_repository.select_all()
    trips = visit_repository.select_all()
    return render_template("trips/new.html", cities = cities, countries = countries, sights = sights, trips=trips)


@trips_blueprint.route("/trips", methods=['POST'])
def create_trip():
    city_id = request.form["city_id"]
    country_id = request.form["country_id"]
    sight_id = request.form["sight_id"]
    to_visit = request.form["to_visit"]
    new_city = City("name", city_id)
    new_country = Country("country", country_id)
    new_sight = Sight("sight", sight_id)
    trip = Visit(new_city, new_country, new_sight, to_visit)
    visit_repository.save(trip)
    import pdb; pdb.set_trace()
    return redirect("/trips")
    
@trips_blueprint.route("/trips/<id>/delete", methods=["POST"])
def delete_trip(id):
    visit_repository.delete(id)
    return redirect("/trips")


@trips_blueprint.route('/trips', methods=['POST'])
def render_results():
    city_name = request.form['city']

    api_key = visit_repository.get_api_key()
    data = visit_repository.get_weather_results(city_name, api_key)   
   
    temp = "{}".format(data["main"]["temp"]) 
    feels_like = "{}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]
    wind_speed = data["wind"]["speed"]
   

    return render_template('trips/results.html',
                           location=location, temp=temp,
                           feels_like=feels_like, weather=weather, wind_speed=wind_speed)
