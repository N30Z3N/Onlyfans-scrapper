# 31.12.23

class Media():
    def __init__(self, json_data):
        self.id = json_data['id']
        self.type = json_data['type']
        self.can_view = json_data['canView']
        self.create_at = json_data['createdAt']
        self.src = json_data['full']
        self.preview = json_data['preview']

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
        
    def is_valid(self):
        return bool(self.id and self.get_ext() and self.can_view and self.src)
        
class Post():
    def __init__(self, json_data):
        self.id = json_data['id']
        self.posted_at = json_data['postedAt']
        self.media_count = json_data['mediaCount']
        self.text = json_data['text']
        self.price = json_data['price']
        self.n_media = len(json_data['media'])
        self.media = [Media(json_media) for json_media in json_data['media']]

class Home_post():

    def __init__(self, json_data) -> None:
        self.has_more = json_data['hasMore']
        self.head_marker = json_data['headMarker']
        self.tail_marker = json_data['tailMarker']
        self.n_post = len(json_data['list'])
        self.posts = [Post(json_post) for json_post in json_data['list']]