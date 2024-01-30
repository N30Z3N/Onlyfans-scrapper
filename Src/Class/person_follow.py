# 31.12.23

class Person():
    def __init__(self, json_data):
        self.id = json_data['id']
        self.name = json_data['name']
        self.username =  json_data['username']
        self.avatar = json_data['avatar']
        self.headers = json_data['header']

class ListPerson():
    def __init__(self, json_data):
        self.follows = [Person(data_person) for data_person in json_data['list']]
