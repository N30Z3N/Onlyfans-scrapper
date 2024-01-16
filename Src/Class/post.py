# 31.12.23

class Media():

    def __init__(self, json):
        self.id = json['id']
        self.type = json['type']
        self.can_view = json['canView']
        self.create_at = json['createdAt']
        self.url = json['full']
        self.preview = json['preview']

    def get_ext(self):
        if self.type == "photo":
            return ".jpg"
        elif self.type == "video":
            return ".mp4"
        elif self.type == "audio":
            return ".mp3"
        elif self.type == "gif":
            return ".gif"
        else:
            print(f"CANT MANAGE: {self.type}")
            return f".{self.type}"

    def to_string(self):
        print(self.__dict__)
        
class Post():

    def __init__(self, json):
        self.id = json['id']
        self.posted_at = json['postedAt']
        self.media_count = json['mediaCount']
        self.text = json['text']
        self.price = json['price']
        self.n_media = len(json['media'])
        self.media = []

        if self.n_media > 0:
            for json_media in json['media']:
                self.media.append(Media(json_media))

    def get_media(self, index) -> (Media):
        return self.media[index]
    
    def to_string(self):
        print(f"[{self.id}] Find: {len(self.media)} media")

class Home_post():

    def __init__(self, json) -> None:
        self.has_more = json['hasMore']
        self.head_marker = json['headMarker']
        self.tail_marker = json['tailMarker']
        self.n_post = len(json['list'])
        self.posts = []

        if self.n_post > 0:
            for json_post in json['list']:
                self.posts.append(Post(json_post))

    def get_post(self, index) -> (Post):
        return self.posts[index]