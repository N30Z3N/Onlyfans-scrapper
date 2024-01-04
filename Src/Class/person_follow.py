# 31.12.23

class Person():

    def __init__(self, json):
        self.id = json['id']
        self.name = json['name']
        self.username =  json['username']
        self.avatar = json['avatar']
        self.headers = json['header']

    def to_string(self):
        print(self.__dict__)

class ListPerson():

    def __init__(self, json):
        self.follows = [Person(json_person) for json_person in json['list']]

    def get_person(self, index) -> (Person):
        return self.follows[index]

    def to_string(self):
        print(f"Follows find: {len(self.follows)}")