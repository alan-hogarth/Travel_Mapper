import pdb
from models.city import City
from models.country import Country
from models.visit import Visit
from models.sight import Sight

import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.visit_repository as visit_repository

sight_repository.delete_all()
city_repository.delete_all()
country_repository.delete_all()
visit_repository.delete_all()

sight_1 = Sight("Beach")
sight_repository.save(sight_1)

sight_2 = Sight("Cathedral")
sight_repository.save(sight_2)

sight_3 = Sight("Art Gallery")
sight_repository.save(sight_3)

city_1 = Sight("Havana")
city_repository.save(city_1)

city_2 = City("Barcelona")
city_repository.save(city_2)

city_3 = City("Florence")
city_repository.save(city_3)

country_1 = Country("Cuba")
country_repository.save(country_1)

country_2 = Country("Spain")
country_repository.save(country_2)

country_3 = Country("Italy")
country_repository.save(country_3)

visit_1 = Visit(city_2, country_2, sight_2, True)
visit_repository.save(visit_1)

visit_2 = Visit(city_1, country_1, sight_1, True)
visit_repository.save(visit_2)

visit_3 = Visit(city_3, country_3, sight_3, False)
visit_repository.save(visit_3)

pdb.set_trace()