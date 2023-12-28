# 9.08.2023 -> 12.09.2023 -> 24.10.2023

# Class import
from Only.src.util.Driver import Driver
from Only.src.util.console import console
from Only.src.api import get_creator, dump_post, donwload_medias, dump_chat
from Only.src.dw_image import donwload_image
from Only.upload.update import main_update

# General import
import time, json, sys, os
from seleniumwire.utils import decode

# Variable
sleep_load_page = 12


# Init
console.log("[blue]Get driver")
driver = Driver()
driver.create(headless = False)
driver.get_page("https://www.google.com/")


# [ func ]
def find_api_creator(creator_name):

    json_data = ""

    for req in driver.driver.requests:
        if "api2" in str(req.url) and str(creator_name) in str(req.url):

            response_body = decode(req.response.body, req.response.headers.get('Content-Encoding', 'identity'))
            json_data = json.loads(response_body)

    if json_data != "":
        get_creator(radice=json_data, msg="creator")
    else:
        console.log(f"[red]ERROR [yellow]find_api_creator by name: [green]{creator_name}")

def find_api_by_prefix(name_api, show_url=False):

    arr_json_data = []

    for req in driver.driver.requests:
        if "api2" in str(req.url) and str(name_api) in str(req.url):

            if(show_url): 
                console.log(f"[blue]FIND API [white]=> [green]{req.url}")

            try:
                response_body = decode(req.response.body, req.response.headers.get('Content-Encoding', 'identity'))

                arr_json_data.append({
                    'url': req.url,
                    'data': json.loads(response_body)
                })
            except:
                console.log("[red]ERROR [white]=> [yellow]No body in api")

    if len(arr_json_data) > 0:
        return arr_json_data
    else:
        console.log(f"[red]ERROR [yellow]find_api_creator by prefix: [green]{name_api}")
        sys.exit(0)

def find_api_me():
    json_data = find_api_by_prefix(name_api="users/me")[0]['data']
    get_creator(radice=json_data, msg="me")


# [ download ]
def download(url, name, prefix_api, scroll_all_page):
    
    driver.get_page(url=url, sleep=sleep_load_page)
    find_api_me()
    find_api_creator(creator_name=name)

    if(scroll_all_page):
        driver.scroll_to_end()

    # Scroll only 5 time to load api
    else:
        driver.scroll_to_end(max_scroll=5)

    # Try find api match with "prefix_api" and dump all data
    for succ_req in find_api_by_prefix(name_api=prefix_api):
        dump_post(radice = succ_req['data']['list'])

    # Download media find
    donwload_medias(name, prefix_api.replace("?", ""))

    # End
    driver.close()

def download_social_buttons(url, name, prefix_api = "social/buttons"):

    driver.get_page(url=url, sleep=sleep_load_page)
    find_api_me()
    find_api_creator(creator_name=name)

    # Custom "find_api_by_prefix"
    json_data = find_api_by_prefix(name_api=prefix_api)[0]['data']
    
    if str(json_data) != "[]":
        for i in range(len(json_data)):
            console.log(f"[blue]Find [white]([yellow]{json_data[i]['label']}[white]) = [red]{json_data[i]['url']}")
    else:
        console.log("[red][ERROR\INFO] [yellow]no data for this profile")

    driver.close()

def download_info_first_sub(url, prefix_api = "subscriptions/subscribe"):

    driver.get_page(url=url, sleep=sleep_load_page)
    find_api_me()

    # Custom "find_api_by_prefix"
    json_data = find_api_by_prefix(name_api=prefix_api)[0]['data']

    if len(json_data['list']) > 0:
        for sub in json_data['list']:

            obj = {'name': sub['name'], 'username': sub['username']}
            console.log(f"[blue]Info [green]sub [{json_data['list'].index(sub)}] [white]=> [cyan]{obj}")
            time.sleep(0.5)
    else:
        console.log("[red]ERROR\INFO [yellow]no data for this profile")

def donwload_profile_photo(url, name):

    driver.get_page(url=url, sleep=sleep_load_page)
    find_api_me()
    find_api_creator(creator_name=name)

    soup = driver.get_soup()
    html_profile = soup.find("img", class_="b-profile__header__cover-img")
    path_folder = os.path.join("data", name, "page_photo")
    os.makedirs(path_folder, exist_ok=True)

    if "http" in html_profile.get("src"):
        console.log("[blue]Image profile status: [red]Find")
        console.log(f"[blue]Folder path: [green]{path_folder}")

    donwload_image(
        url = html_profile.get("src"),
        name = "profile.jpg",
        folder = path_folder
    )

def donwload_avatar_photo(url, name):

    driver.get_page(url=url, sleep=sleep_load_page)
    find_api_me()
    find_api_creator(creator_name=name)

    soup = driver.get_soup()
    html_profile = soup.find("div", class_="g-avatar__img-wrapper").find("img")
    path_folder = os.path.join("data", name, "page_photo")
    os.makedirs(path_folder, exist_ok=True)

    if "http" in html_profile.get("src"):
        console.log("[blue]Image avatar: [red]Find")
        console.log(f"[blue]Folder path: [green]{path_folder}")

    donwload_image(
        url = html_profile.get("src"),
        name = "avatar.jpg",
        folder = path_folder
    )

def download_chat(id_chat):

    driver.get_page(f"https://onlyfans.com/my/chats/chat/{id_chat}/", sleep=sleep_load_page)

    console.log("[blue]SCROLL TO THE TOP !! ")
    time.sleep(1.5)
    console.log("[blue]IF TOP OF THE PAGE, PRESS ANY KEY")
    input("")

    #with open("sample.json", "w") as outfile:
    #    json.dump(find_api_by_prefix(name_api="chats"), outfile)

    # For all valid req in api xxx
    for req in find_api_by_prefix(name_api="chats"):
        #print("GET => ", req['url'])

        # For only first one
        if req['url'] == f"https://onlyfans.com/api2/v2/chats/{id_chat}?skip_users=all":
            dump_chat(req['data']['lastMessage']['media'])

        # all other
        else:
            for media in req['data']['list']:
                try:
                    dump_chat(media['media'])
                except:
                    pass


    donwload_medias(folder_name=id_chat, sub_folder="chat")
    driver.close()


# [ class ]
class Main:

    username = ""

    def __init__(self, username) -> None:
        self.username = username
        if username == None or username == "":
            console.log("[red]Insert username on main file")
            sys.exit(0)
        else:
            main_update()

    def make_login(self):
        driver = Driver()
        driver.create(False)
        console.log("[cyan]LOAD HOME PAGE")
        driver.get_page(url="https://onlyfans.com/", sleep=1)
        time.sleep(999)

    def get_url(self):
        if(self.username != None and self.username != ""):
            return f"https://onlyfans.com/{self.username}"


    def get_all_post(self):
        console.log("[yellow]GET ALL POST")
        download(
            url = self.get_url(), 
            name = self.username, 
            prefix_api = "posts?", 
            scroll_all_page = True
        )

    def get_last_post(self):
        console.log("[yellow]GET LAST POST")
        download(
            url = self.get_url(), 
            name = self.username, 
            prefix_api = "posts?", 
            scroll_all_page = False
        )

    def get_all_media(self):
        console.log("[yellow]GET ALL MEDIA")
        download(
            url = self.get_url() + "/media", 
            name = self.username, 
            prefix_api = "medias?", 
            scroll_all_page = True
        )

    def get_last_media(self):
        console.log("[yellow]GET LAST MEDIA")
        download(
            url = self.get_url() + "/media", 
            name = self.username, 
            prefix_api = "medias?", 
            scroll_all_page = False
        )


    def get_chat(self, id_chat):
        console.log("[yellow]GET CHAT")
        download_chat(
            id_chat=id_chat
        )


    def get_social_buttons(self):
        console.log("[yellow]GET SOCIAL")
        download_social_buttons(
            url = self.get_url(), 
            name = self.username
        )

    def get_list_first_subscribe(self):
        console.log("[yellow]GET FIRST 10 SUB")
        download_info_first_sub(
            url = "https://onlyfans.com/my/collections/user-lists/subscriptions/active"
        )

    def get_profile_photo(self):
        console.log("[yellow]DONWLOAD PROFILE PHOTO")
        donwload_profile_photo(
            url = self.get_url(),
            name = self.username
        )

    def get_avatar_photo(self):
        console.log("[yellow]DONWLOAD AVATAR PHOTO")
        donwload_avatar_photo(
            url = self.get_url(),
            name = self.username
        )
        
