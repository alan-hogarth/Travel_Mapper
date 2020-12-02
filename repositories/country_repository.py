from db.run_sql import run_sql
from models.city import City
from models.country import Country
from models.visit import Visit
from models.sight import Sight

def save(country):
    sql = "INSERT INTO countries (name)  VALUES ( %s ) RETURNING id"
    values = [country.name]
    results = run_sql( sql, values )
    country.id = results[0]['id']
    return country

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = Country(row['name'], row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['id'] )
    return country 

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def update(country):
    sql = "UPDATE countries SET name = %s WHERE id = %s"
    values = [country.name, country.id]
    run_sql(sql, values)

# get all sights for countries
def sights(country):
    results = []
    sql = """SELECT sights.* 
            FROM sights
            INNER JOIN visits ON sights.id = visits.sight_id
            INNER JOIN countries ON countries.id = visits.country_id
            WHERE countries.id = %s"""
    values = [country.id]
    sql_results = run_sql(sql, values)
    
    for row in sql_results:
        sight = Sight(row['name'], row['id'])
        results.append(sight)
    
    return results

# get all cities for countries
def cities(country):
    results = []
    sql ="""SELECT cities.*
            FROM cities
            INNER JOIN visits ON cities.id = visits.city_id
            INNER JOIN countries ON countries.id = visits.country_id
            WHERE countries.id = %s"""
    values = [country.id]
    sql_results = run_sql(sql, values)

    for row in sql_results:
        city = City(row['name'], row['id'])
        results.append(city)
    
    return results