from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all() 
    return render_template("cities/index.html", cities=cities)

# select cities by id
@cities_blueprint.route("/cities/<id>")
def show(id):
    city = city_repository.select(id)
    city_users = city_repository.users(city)
    return render_template("cities/show.html", city=city, users=city_users)

# location for creating new city
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    cities = city_repository.select_all()
    return render_template("cities/new.html", cities=cities)

    # form for creating new city
@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    city = request.form["city"]
    new_city = City(city)
    city_repository.save(new_city)
    return redirect("/cities")

# delete city by id
@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")
    

