from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all() 
    return render_template("cities/index.html", cities = cities)


@cities_blueprint.route("/cities/<id>")
def show(id):
    city = city_repository.select(id)
    city_users = city_repository.users(city)
    return render_template("cities/show.html", city=city, users=city_users)
    
@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    city = request.form["city"]
    new_city = City(city)
    city_repository.save(new_city)
    return redirect("/cities/index.html")


    
    # @cities_blueprint.route("/cities/<id>")
# def show_country(id):
#     city = city_repository.select(id)
#     city_countries = city_repository.countries(city)
#     return render_template("cities/index.html", cities=city, countries=city_countries)
