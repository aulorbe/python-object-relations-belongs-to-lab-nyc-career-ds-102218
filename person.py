# import car class here
from car import Car

class Person:

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation


    @property
    def name(self):
        return self._name

    @property
    def occupation(self):
        return self._occupation



    @classmethod # class method that returns the person instance object that owns the oldest car
    def has_oldest_car(cls):
        oldest_year = sorted([i.year for i in Car._all])[0] #1978
        for i in Car._all:
            if i.year == oldest_year:
                return i.owner.name
