# import car class here
from car import Car



class Person:

    _all = []

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation
        Person._all.append(self)

# GETTERS

    @property
    def name(self):
        return self._name

    @property
    def occupation(self):
        return self._occupation

# CLASS METHODS

    @classmethod # class method that returns the person instance object that owns the oldest car
    def has_oldest_car(cls):
        oldest_year = sorted([i.year for i in Car._all])[0] #1978
        for i in Car._all:
            if i.year == oldest_year:
                return i.owner.name

    @classmethod
    def drives_a(cls,make): #class method that returns a list of person instance objects that own a Ford
        makes = list(filter(lambda i: i.make==make,Car._all))
        drives_a_ = []
        for i in makes:
            drives_a_.append(i.owner.name)
        return drives_a_

    @classmethod
    def all(cls):
        return Person._all



# INSTANCE METHOD #
    def drives_same_make_as_me(self): # instance method that returns a list of other dunder mifflin employees who drive the same make car as the instance object it was called on
        #inputting a person's instance
        # getting out a list of other people instances with the same make of car as input

        jims_make = [] #toyota
        for i in Car._all:
            if i.owner.name == self.name:
                jims_make.append(i.make)

        all_makes = Person.drives_a(jims_make[0]) #gives list of people with the same make as jim
        return list(filter(lambda i:  i != self.name,all_makes))

        #brain work:
        # say what make of car i drive
        # see what make of car everyone else has
        # and then i want to compare my make and everyone else's makes to find a match
