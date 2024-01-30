# 01.01.24

class Media():

    def __init__(self, json_data):
        self.id = json_data['id']
        self.type = json_data['type']
        self.can_view = json_data['canView']
        self.create_at = json_data['createdAt']
        self.src = json_data['files']['source']['url']
        self.preview = json_data['files']['preview']['url']

    def get_ext(self):
        if self.type == "photo": return ".jpg"
        else: return ".mp4"

    def is_valid(self):
        return bool(self.id and self.get_ext() and self.can_view and self.src)

class Home_stories():
    def __init__(self, json_data):
        self.media = [Media(media['media'][0]) for media in json_data]
        self.n_media = len(self.media)