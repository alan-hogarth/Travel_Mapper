from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all() 
    return render_template("countries/index.html", countries = countries)

@countries_blueprint.route("/countries/<id>")
def show_country(id):
    country = country_repository.select(id)
    country_cities = country_repository.cities(country)
    return render_template("countries/show.html", country=country, cities=country_cities)

@countries_blueprint.route("/countries/<id>")
def show_user(id):
    country = country_repository.select(id)
    country_users = country_repository.users(country)
    return render_template("countries/show.html", country=country, users=country_users)


# EDIT
@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    return render_template("countries/edit.html", country=country)


# UPDATE
@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["name"]
    country = Country(name, id)
    country_repository.update(country)
    return redirect("/countries")
