# 30.01.24

class Media:
    def __init__(self, data):
        self.id = data.get("id")
        self.canView = data.get("canView")
        self.type = data.get("type")
        self.src = data.get("src")
        self.video = data.get("video", {})

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
        return bool(self.id and self.get_ext() and self.canView and self.src)

class Message:
    def __init__(self, data):
        self.text = data.get("text")
        self.isFree = data.get("isFree")
        self.price = data.get("price")
        self.mediaCount = data.get("mediaCount")
        self.media = [Media(media) for media in data.get("media", [])]
        self.id = data.get("id")
        self.isNew = data.get("isNew")
        
class JsonResponse:
    def __init__(self, data):
        self.list = [Message(msg) for msg in data.get("list", [])]
        self.hasMore = data.get("hasMore")
