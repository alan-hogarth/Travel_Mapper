import pdb
from models.city import City
from models.country import Country
from models.visit import Visit
from models.user import User

import repositories.user_repository as user_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.visit_repository as visit_repository

user_1 = User("Chris Columbus")
user_repository.save(user_1)

user_2 = User("Francis Drake")
user_repository.save(user_2)

user_3 = User("Walter Raleigh")
user_repository.save(user_3)

city_1 = City("Havana")
city_repository.save(city_1)

city_2 = City("Barcelona")
city_repository.save(city_2)

city_3 = City("Florence")
city_repository.save(city_3)

country_1 = Country("Cuba", city_1)
country_repository.save(country_1)

country_2 = Country("Spain")
country_repository.save(country_2)

country_3 = Country("Italy")
country_repository.save(country_3)

visit_1 = Visit(user_1, city_2, country_2, "On the bucket list!" )
visit_repository.save(visit_1)

visit_2 = Visit(user_2, city_1, country_3, "Checked off the bucket list")
visit_repository.save(visit_2)

visit_3 = Visit(user_3, city_3, country_1, "On the bucket list!")
visit_repository.save(visit_3)

pdb.set_trace()