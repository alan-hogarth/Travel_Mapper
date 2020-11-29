from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.visit import Visit
from models.city import City
from models.country import Country
from models.user import User

import repositories.visit_repository as visit_repository
import repositories.user_repository as user_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

trips_blueprint = Blueprint("trips", __name__)

@trips_blueprint.route("/trips")
def trips():
    trips = visit_repository.select_all() 
    return render_template("trips/index.html", trips = trips)

@trips_blueprint.route("/trips/new", methods=['GET'])
def new_trip():
    users = user_repository.select_all()
    city = city_repository.select_all()
    country = country_repository.select_all()
    return render_template("trips/new.html", users = users, city = city, country = country)

# @trips_blueprint.route("/trips",  methods=['POST'])
# def create_trip():
#     user = request.form["name"]
#     country = request.form["country"]
#     city = request.form["city"]
#     new_user = User(user)
#     new_country = Country(country) 
#     new_city = City(city)
#     trip = Visit(new_user, new_country, new_city)
#     visit_repository.save(trip)
#     return redirect("/trips")
    
@trips_blueprint.route("/trips/<id>/delete", methods=["POST"])
def delete_trip(id):
    visit_repository.delete(id)
    return redirect("/trips")



