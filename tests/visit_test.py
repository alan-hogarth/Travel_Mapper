import unittest
from models.visit import Visit

class TestVisit(unittest.TestCase):
    
    def setUp(self):
        self.visit = Visit("Helsinki", "Finland", "lakes")
    
    def test_visit_has_country(self):
        self.assertEqual("Finland", self.visit.country)
    
    def test_visit_has_city(self):
        self.assertEqual("Helsinki", self.visit.city)
    
    def test_visit_has_sight(self):
        self.assertEqual("lakes", self.visit.sight)
    
    def test_check_to_visit(self):
        self.visit.visited()
        self.assertEqual(True, self.visit.to_visit)

