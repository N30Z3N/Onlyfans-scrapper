

class High():
    def __init__(self, json_data):
        self.id = json_data['id']
        self.title = json_data['title']
        self.cover = json_data['cover']

class List_high():
    def __init__(self, json_data):
        self.n_high = len(json_data['list'])
        self.list_high = [High(json_high) for json_high in json_data['list']]

class Media():
    def __init__(self, json):
        self.id = json['id']
        self.type = json['type']
        self.can_view = json['canView']
        self.create_at = json['createdAt']
        self.src = json['files']['source']['url']
        self.preview = json['files']['preview']['url']

    def get_ext(self):
        if self.type == "photo": return ".jpg"
        else: return ".mp4"

    def is_valid(self):
        return bool(self.id and self.get_ext() and self.can_view and self.src)

class Single_stories():
    def __init__(self, json_data) -> None:
        self.id = json_data['id']
        self.title = json_data['title']
        self.story_count = json_data['storiesCount']
        self.media = [Media(json_media) for json_story in json_data['stories'] for json_media in json_story['media']]