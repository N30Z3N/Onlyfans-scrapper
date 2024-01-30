# 31.12.23

# Class import
from Src.Class.person import Person
from Src.Class.person_follow import ListPerson
from Src.Class.request import OnlyRequest
from Src.Class.post import Home_post
from Src.Class.stories import Home_stories
from Src.Class.highlight import List_high, Single_stories
from Src.Class.message import JsonResponse as MsgJsonResponse

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
        self.only_req.generate_auth()
        self.only_req.generate_sign("/users/me", {})

        self.list_follow = []
        self.person_select = None
        self.base_folder = None

    def get_me(self):

        console.print("[green]Checking user login ...")
        json_me = self.only_req.api_request("/users/me/").json()
        self.me = Person(json_me)

        console.print(f"=> [red]Me: [cyan]{self.me.__dict__}")

    def get_follow(self):

        json_follows = self.only_req.api_request(endpoint="/subscriptions/subscribes/", getparams={'offset': '0','type': 'active','limit': '99','format': 'infinite'}).json()
        self.list_follow = ListPerson(json_follows)

        dict_follows = {i: person.name for i, person in enumerate(self.list_follow.follows)}
        answers = prompt([List('selected_follow', message='Select a person', choices=dict_follows.values())])
        index_user_select = {v: k for k, v in dict_follows.items()}.get(answers['selected_follow'])

        self.person_select = self.list_follow.follows[index_user_select]
        console.log(f"[green]Select: [cyan]{self.person_select.username}")

        self.base_folder = os.path.join("data", str(self.person_select.username))
        os.makedirs(self.base_folder, exist_ok=True)

    def download_avatar(self):

        folder_path = os.path.join(self.base_folder, "Profile")
        os.makedirs(folder_path, exist_ok=True)

        download(url=self.person_select.avatar, path=os.path.join(folder_path, "_avatar.jpg"))
        download(url=self.person_select.headers, path=os.path.join(folder_path, "_header.jpg"))

    def download_posts(self, next_tail = None):
            
        if next_tail == None: 
            json_first_post_json = self.only_req.api_request(endpoint=f"/users/{self.person_select.id}/posts/", getparams={'limit': '20', 'order': 'publish_date_desc', 'skip_users': 'all', 'format': 'infinite', 'pinned': '0', 'counters': '1'}).json()
        else: 
            json_first_post_json = self.only_req.api_request(endpoint=f"/users/{self.person_select.id}/posts/", getparams={'limit': '20', 'order': 'publish_date_desc', 'skip_users': 'all', 'format': 'infinite', 'pinned': '0', 'counters': '1', 'beforePublishTime': next_tail}).json()
        
        home_api_post = Home_post(json_first_post_json)

        img_folder_path = os.path.join(self.base_folder, "posts\\images")
        video_folder_path = os.path.join(self.base_folder, "posts\\videos")
        os.makedirs(img_folder_path, exist_ok=True)
        os.makedirs(video_folder_path, exist_ok=True)

        for post_n in home_api_post.posts:
            with concurrent.futures.ThreadPoolExecutor(10) as executor:
                for media in post_n.media:
                    if media.is_valid():
                        folder_path = img_folder_path if media.get_ext() == ".jpg" else video_folder_path
                        download(url=media.src, path=os.path.join(folder_path, f"{media.id}{media.get_ext()}"), headers={"user-agent": get_headers()})

        # Go next
        if home_api_post.has_more:
            self.download_posts(home_api_post.tail_marker)

    def download_stories(self):

        json_stories = self.only_req.api_request(f"/users/{self.person_select.id}/stories/").json()
        list_stories = Home_stories(json_stories)

        img_folder_path = os.path.join(self.base_folder, "stories\\images")
        video_folder_path = os.path.join(self.base_folder, "stories\\videos")
        os.makedirs(img_folder_path, exist_ok=True)
        os.makedirs(video_folder_path, exist_ok=True)

        for media in list_stories.media:
            if media.is_valid():
                folder_path = img_folder_path if media.get_ext() == ".jpg" else video_folder_path
                download(url=media.src, path=os.path.join(folder_path, f"{media.id}{media.get_ext()}"), headers={"user-agent": get_headers()})
            
    def __download_high_story__(self, id):

        json_stories = self.only_req.api_request(f"/stories/highlights/{id}/").json()
        single_story = Single_stories(json_stories)

        img_folder_path = os.path.join(self.base_folder, "highlights\\images")
        video_folder_path = os.path.join(self.base_folder, "highlights\\videos")
        os.makedirs(img_folder_path, exist_ok=True)
        os.makedirs(video_folder_path, exist_ok=True)

        for media in single_story.media:
            if media.is_valid():
                folder_path = img_folder_path if media.get_ext() == ".jpg" else video_folder_path
                download(url=media.src, path=os.path.join(folder_path, f"{media.id}{media.get_ext()}"), headers={"user-agent": get_headers()})
                
    def download_high(self):

        json_highs = self.only_req.api_request(endpoint=f"/users/{self.person_select.id}/stories/highlights/", getparams={'limit': '999', 'offset': '0'}).json()
        list_highs = List_high(json_highs)

        for obj_high in list_highs.list_high:
            self.__download_high_story__(obj_high.id)
            
    def get_list_chats(self, has_more = False, next_id = None, right_id_select=None):

        if not has_more and right_id_select is not None:
            console.log("[red]End get chat\n")
            return

        if not has_more:
            json_chat = self.only_req.api_request(endpoint="/chats/", getparams={'limit': '100', 'offset': '0', 'skip_users': 'all', 'order': 'recent'})

            dict_user_chat_id = {i: msg['withUser']['id'] for i, msg in enumerate(json_chat.json()['list'])}
            answers = prompt([List('select_id', message='Select a chat id', choices=dict_user_chat_id.values())])
            id_user_select = {v: k for k, v in dict_user_chat_id.items()}.get(answers['select_id'])

            right_id_select = dict_user_chat_id.get(id_user_select)
            json_user_id = self.only_req.api_request(endpoint=f"/chats/{right_id_select}/messages/", getparams={'limit': '100', 'order': 'desc', 'skip_users': 'all'})
            
        else:
            json_user_id = self.only_req.api_request(endpoint=f"/chats/{right_id_select}/messages/", getparams={'limit': '100', 'order': 'desc', 'skip_users': 'all', 'id': next_id})

        img_folder_path = os.path.join(f"data\\chats\\{str(right_id_select)}\\images")
        video_folder_path = os.path.join(f"data\\chats\\{str(right_id_select)}\\videos")
        os.makedirs(img_folder_path, exist_ok=True)
        os.makedirs(video_folder_path, exist_ok=True)

        user_data = MsgJsonResponse(json_user_id.json())
        next_has_more = user_data.hasMore
        next_use_id = user_data.list[-1].id

        for msg in user_data.list:
            if msg.mediaCount > 0:
                for media in msg.media:
                    if media.is_valid():
                        folder_path = img_folder_path if media.get_ext() == ".jpg" else video_folder_path
                        download(url=media.src, path=os.path.join(folder_path, f"{media.id}{media.get_ext()}"), headers={"user-agent": get_headers()})

        self.get_list_chats(next_has_more, next_use_id, right_id_select)
