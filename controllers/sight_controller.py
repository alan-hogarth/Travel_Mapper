from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sight import Sight
import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository

sights_blueprint = Blueprint("sights", __name__)

@sights_blueprint.route("/sights")
def sights():
    sights = sight_repository.select_all() 
    return render_template("sights/index.html", sights = sights)


@sights_blueprint.route("/sights/<id>")
def show_sight(id):
    sight = sight_repository.select(id)
    sight_cities = sight_repository.cities(sight)
    return render_template("sights/show.html", sight=sight, cities=sight_cities)