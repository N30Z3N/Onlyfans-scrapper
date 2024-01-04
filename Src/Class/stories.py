# 01.01.24

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

class Home_stories():

    def __init__(self, json):
        self.n_media = len(json)
        self.media = []

        if self.n_media > 0:
            for media in json:
                self.media.append(Media(media['media'][0]))

    def get_media(self, index) -> (Media):
        return self.media[index]
    
    def to_string(self):
        print(f"Find: {len(self.media)} media")