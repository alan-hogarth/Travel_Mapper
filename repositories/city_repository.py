from db.run_sql import run_sql
from models.city import City
from models.country import Country
from models.visit import Visit
from models.sight import Sight

def save(city):
    sql = "INSERT INTO cities( name ) VALUES ( %s ) RETURNING id"
    values = [city.name]
    results = run_sql( sql, values )
    city.id = results[0]['id']
    return city

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        city = City(row['name'], row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = City(result['name'], result['id'] )
    return city

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def update(city):
    sql = "UPDATE cities SET name = %s WHERE id = %s"
    values = [city.name, city.id]
    run_sql(sql, values)


# get all attractions for cities
def sights(city):
    results = []
    sql = """SELECT sights.* 
            FROM sights
            INNER JOIN visits ON sights.id = visits.sight_id
            INNER JOIN cities ON cities.id = visits.city_id
            WHERE cities.id = %s"""
    values = [city.id]
    sql_results = run_sql(sql, values)
    
    for row in sql_results:
        sight = Sight(row['name'], row['id'])
        results.append(sight)
    
    return results

# get all countries for cities
def countries(city):
    results = []
    sql ="""SELECT countries.*
            FROM countries
            INNER JOIN visits ON countries.id = visits.country_id
            INNER JOIN cities ON cities.id = visits.city_id
            WHERE cities.id = %s"""
    values = [city.id]
    sql_results = run_sql(sql, values)

    for row in sql_results:
        country = Country(row['name'], row['id'])
        results.append(country)
    
    return results