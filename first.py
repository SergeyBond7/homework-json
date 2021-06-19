import json

class Stadium(object):

    def __init__(self,name='', year='', country='', capacity='', club=''):
        self.name = name
        self.year = year
        self.country = country
        self.capacity = capacity
        self.club = club

    def __str__(self):
        return f"{self.name}: {self.year}: {self.country}: {self.capacity}: {self.club}"

def FormateData(instance):
    result = {}
    for key in instance.__dict__:
        result[key] = instance.__dict__[key]
    return result

def FromDictToInstance(dictionary, cls):
    obj = cls()
    obj.name = dictionary['name']
    obj.year = dictionary['year']
    obj.country = dictionary['country']
    obj.capacity = dictionary['capacity']
    obj.club = dictionary['club']
    return obj


stadium = Stadium("Etihad", 2002, "England", 55000, "Manchester City")

# Сериализация
serialized = json.dumps(FormateData(stadium))

# Десериализация
desirialized = json.loads(serialized)
# print(desialized)

print(FromDictToInstance(desirialized, Stadium))

