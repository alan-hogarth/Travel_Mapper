from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sight import Sight
import repositories.sight_repository as sight_repository

sights_blueprint = Blueprint("sights", __name__)

@sights_blueprint.route("/sights")
def sights():
    sights = sight_repository.select_all() 
    return render_template("sights/index.html", sights = sights)