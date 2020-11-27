import pdb
from models.city import City
from models.country import Country
from models.visits import Visits
from models.user import User

import repositories.user_repository as user_repository
import repositories.city_repository as city_repository

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

pdb.set_trace()