class Car():

    _all = []

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        Car._all.append(self)

#getters:
    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def owner(self):
        return self._owner

#setters:
    @make.setter
    def make(self,make):
        self._make = make

    @model.setter
    def model(self,model):
        self._model = model

    @year.setter
    def year(self,year):
        self._year = year

    @owner.setter
    def owner(self,owner):
        self._owner = owner

#deleters:
    @make.deleter
    def make(self,make):
        del self._make

    @model.deleter
    def model(self,model):
        del self._model

    @year.deleter
    def year(self,year):
        del self._year

    @owner.deleter
    def owner(self,owner):
        del self._owner

# classmethods:
    @classmethod
    def all(cls):
        return Car._all

    @classmethod
    def cars_driven_by(cls,occupation): # class method that returns a list of car instance objects that are driven by people whose occupation is "Paper Salesperson." Example: [dwight, jim, stanley]
        from person import Person
        occupation_objects = list(filter(lambda i: i.occupation==occupation  ,Person._all))
        names_object_instances = [i.name for i in occupation_objects]
        return names_object_instances
