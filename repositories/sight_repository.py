from db.run_sql import run_sql
from models.city import City
from models.country import Country
from models.visit import Visit
from models.sight import Sight

def save(sight):
    sql = "INSERT INTO sights( name ) VALUES ( %s ) RETURNING id"
    values = [sight.name]
    results = run_sql( sql, values )
    sight.id = results[0]['id']
    return sight

def select_all():
    sights = []

    sql = "SELECT * FROM sights"
    results = run_sql(sql)
    for row in results:
        sight = Sight(row['name'], row['id'])
        sights.append(sight)
    return sights

def select(id):
    sight = None
    sql = "SELECT * FROM sights WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        sight = Sight(result['name'], result['id'] )
    return sight

def delete(id):
    sql = "DELETE FROM sights WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)


def cities(sight):
    results = []
    sql = """SELECT cities.* 
            FROM cities
            INNER JOIN visits ON cities.id = visits.city_id
            INNER JOIN sights ON sights.id = visits.sight_id
            WHERE sights.id = %s"""
    values = [sight.id]
    sql_results = run_sql(sql, values)
    
    for row in sql_results:
        city = City(row['name'], row['id'])
        results.append(city)
    
    return results
