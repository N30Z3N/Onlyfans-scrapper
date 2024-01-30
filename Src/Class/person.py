# 31.12.23

class Person():
    def __init__(self, json):
        self.name= json['name']
        self.user= json['username']
        self.id= json['id']
        self.n_posts= json['postsCount']
        self.n_photos= json['photosCount']
        self.n_videos= json['videosCount']
        self.n_audio= json['audiosCount']
        self.n_medias= json['mediasCount']
        self.join_data= str(json['joinDate']).split("T")[0]