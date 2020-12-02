from db.run_sql import run_sql
from models.city import City
from models.country import Country
from models.visit import Visit
from models.sight import Sight
import requests
import configparser

import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

def save(visit):
    sql = "INSERT INTO visits (city_id, country_id, sight_id, to_visit) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [visit.city.id, visit.country.id, visit.sight.id, visit.to_visit]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit

def select_all():
    visits = []

    sql = "SELECT * FROM visits"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        country = country_repository.select(row['country_id'])
        sight = sight_repository.select(row["sight_id"])
        visit = Visit(city, country, sight, row['to_visit'], row['id'])
        visits.append(visit)
    return visits

def delete_all():
    sql = "DELETE FROM visits"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# read and return api key from file
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['OPENWEATHERMAP']['api']

# return weather results in api url
def get_weather_results(city_name, api_key):
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city_name, api_key)
    r = requests.get(api_url)
    return r.json()