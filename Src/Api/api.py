# 31.12.23

# Class import
from Src.Class.person import Person
from Src.Class.person_follow import ListPerson
from Src.Class.request import OnlyRequest
from Src.Class.post import Home_post
from Src.Class.stories import Home_stories
from Src.Class.highlight import List_high, Single_stories

# Util import
from Src.Util.Helper.download_file import download
from Src.Util.Helper.headers import get_headers
from Src.Util.Helper.console import console
from inquirer import prompt, List
import os, concurrent.futures


class Call_api():

    def __init__(self) -> None:
        self.only_req = OnlyRequest()
        self.only_req.get_rules()
        self.only_req.generata_auth()
        self.only_req.generate_sign("/users/me", {})

        self.list_follow = []
        self.person_select = None
        self.base_folder = None

    def get_me(self):

        json_me = self.only_req.api_request("/users/me").json()
        self.me = Person(json_me)

        console.log(f"[green]Me: [cyan]{self.me.__dict__}")

    def get_follow(self):

        json_follows = self.only_req.api_request(endpoint="/subscriptions/subscribes", getparams={'offset': '0','type': 'active','limit': '99','format': 'infinite'}).json()
        self.list_follow = ListPerson(json_follows)

        dict_follows = {i:self.list_follow.get_person(i).name for i in range(len(self.list_follow.follows))}
        answers = prompt([List('selected_follow', message='Seleziona a person', choices=dict_follows.values())])
        
        id_selezionato = {v: k for k, v in dict_follows.items()}.get(answers['selected_follow'])

        self.person_select = self.list_follow.get_person(id_selezionato)
        console.log(f"[greeb]Select: [cyan]{self.person_select.username}")

        self.base_folder = os.path.join("data", str(self.person_select.username))
        os.makedirs(self.base_folder, exist_ok=True)

    def donwload_avatar(self):

        folder_path = os.path.join(self.base_folder, "Profile")
        os.makedirs(folder_path, exist_ok=True)

        download(url=self.person_select.avatar, path=os.path.join(folder_path, "_avatar.jpg"))
        download(url=self.person_select.headers, path=os.path.join(folder_path, "_header.jpg"))

    def download_posts(self, next_tail = None):
            
        if next_tail == None: 
            json_first_post_json = self.only_req.api_request(endpoint=f"/users/{self.person_select.id}/posts", getparams={'limit': '20', 'order': 'publish_date_desc', 'skip_users': 'all', 'format': 'infinite', 'pinned': '0', 'counters': '1'}).json()
        else: 
            json_first_post_json = self.only_req.api_request(endpoint=f"/users/{self.person_select.id}/posts", getparams={'limit': '20', 'order': 'publish_date_desc', 'skip_users': 'all', 'format': 'infinite', 'pinned': '0', 'counters': '1', 'beforePublishTime': next_tail}).json()
        
        home_api_post = Home_post(json_first_post_json)

        img_folder_path = os.path.join(self.base_folder, "posts\\images")
        video_folder_path = os.path.join(self.base_folder, "posts\\videos")
        os.makedirs(img_folder_path, exist_ok=True)
        os.makedirs(video_folder_path, exist_ok=True)

        for k in range(home_api_post.n_post):
            post_n = home_api_post.get_post(k)

            with concurrent.futures.ThreadPoolExecutor(10) as executor:
                for j in range(post_n.n_media):
                    media = post_n.get_media(j)

                    if str(media.id) != None or media.get_ext() != None:
                        if media.get_ext() == ".jpg":
                            executor.submit(download, url=media.url, path=os.path.join(img_folder_path, str(media.id) + media.get_ext()), headers={"user-agent": get_headers()})
                        else:
                            executor.submit(download, url=media.url, path=os.path.join(video_folder_path, str(media.id) + media.get_ext()), headers={"user-agent": get_headers()})

                    else:
                        media.to_string()
        # GO next
        if home_api_post.has_more:
            self.download_posts(home_api_post.tail_marker)

    def download_stories(self):

        json_stories = self.only_req.api_request(f"/users/{self.person_select.id}/stories").json()
        list_stories = Home_stories(json_stories)

        img_folder_path = os.path.join(self.base_folder, "stories\\images")
        video_folder_path = os.path.join(self.base_folder, "stories\\videos")
        os.makedirs(img_folder_path, exist_ok=True)
        os.makedirs(video_folder_path, exist_ok=True)

        for i in range(list_stories.n_media):
            media = list_stories.get_media(i)
            
            if str(media.id) != None or media.get_ext() != None:
                if media.get_ext() == ".jpg":
                    download(url=media.url, path=os.path.join(img_folder_path, str(media.id) + media.get_ext()), headers={"user-agent": get_headers()})
                else:
                    download(url=media.url, path=os.path.join(video_folder_path, str(media.id) + media.get_ext()), headers={"user-agent": get_headers()})
            
            else:
                media.to_string()

    def __donwload_high_story__(self, id):

        json_stories = self.only_req.api_request(f"/stories/highlights/{id}").json()
        single_stori = Single_stories(json_stories)

        img_folder_path = os.path.join(self.base_folder, "highlights\\images")
        video_folder_path = os.path.join(self.base_folder, "highlights\\videos")
        os.makedirs(img_folder_path, exist_ok=True)
        os.makedirs(video_folder_path, exist_ok=True)

        for i in range(len(single_stori.media)):
            media = single_stori.get_media(i)

            if str(media.id) != None or media.get_ext() != None:
                if media.get_ext() == ".jpg":
                    download(url=media.url, path=os.path.join(img_folder_path, str(media.id) + media.get_ext()), headers={"user-agent": get_headers()})
                else:
                    download(url=media.url, path=os.path.join(video_folder_path, str(media.id) + media.get_ext()), headers={"user-agent": get_headers()})
                    
            else:
                media.to_string()
                
    def donwload_high(self):

        json_highs = self.only_req.api_request(endpoint=f"/users/{self.person_select.id}/stories/highlights", getparams={'limit': '999', 'offset': '0'}).json()
        list_highs = List_high(json_highs)

        for i in range(len(list_highs.list_hig)):
            obj_high = list_highs.get_high(i)
            self.__donwload_high_story__(obj_high.id)
            

        