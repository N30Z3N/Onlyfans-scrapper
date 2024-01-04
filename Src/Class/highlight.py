

class High():

    def __init__(self, json):
        self.id = json['id']
        self.title = json['title']
        self.cover = json['cover']

class List_high():

    def __init__(self, json):
        self.n_high = len(json['list'])
        self.list_hig = []

        for json_high in json['list']:
            self.list_hig.append(High(json_high))
    
    def get_high(self, index) -> (High):
        return self.list_hig[index]
    
    def to_string(self):
        print(f"High find: {len(self.list_hig)}")


class Media():

    def __init__(self, json):
        self.id = json['id']
        self.type = json['type']
        self.can_view = json['canView']
        self.create_at = json['createdAt']
        self.url = json['files']['source']['url']
        self.preview = json['files']['preview']['url']

    def get_ext(self):
        if self.type == "photo":
            return ".jpg"
        if self.type == "video":
            return ".mp4"

    def to_string(self):
        print(self.__dict__)

class Single_stories():

    def __init__(self, json) -> None:
        self.id = json['id']
        self.title = json['title']
        self.stori_count = json['storiesCount']
        self.media = []

        for json_story in json['stories']:
            for json_media in json_story['media']:
                self.media.append(Media(json_media))

    def get_media(self, index) -> Media:
        return self.media[index]
    
    def to_string(self):
        print(f"Medias find: {len(self.media)}")
