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
    return render_template("trips/new.html", cities = cities, countries = countries)


# @trips_blueprint.route("/trips", methods=['POST'])
# def create_trip():
#     city = request.form["city"]
#     country = request.form["country"]
#     to_visit = request.form["to_visit"]
#     new_city = City(city)
#     new_country = Country(country) 
#     trip = Visit(new_city, to_visit, new_country)
#     visit_repository.save(trip)
#     return redirect("/trips")
    
@trips_blueprint.route("/trips/<id>/delete", methods=["POST"])
def delete_trip(id):
    visit_repository.delete(id)
    return redirect("/trips")



