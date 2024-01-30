# 31.12.23

# Class import
from Src.Api.api import Call_api
from Src.Util.Generator.generate_headers import generate, make_login
from Src.Util.Helper.console import console, msg
from Src.Util.Other.msg import hello
from Src.Util.upload.upload_v import main_update

# Import
import sys, json

# Varible
call_api = Call_api()

def check_json_variables(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)
            for key, value in json_data.items():
                if value is None or value == "" or (isinstance(value, list) and not value):
                    print(f"Variable '{key}' is empty.")
                    return False
            return True
    except FileNotFoundError:
        return False
    except json.JSONDecodeError:
        return False
    
def main():

    hello()
    try: 
        main_update()
    except: 
        console.log("[red]Cant connect to github \n")

    console.print("[green]Checking json file ...")
    if check_json_variables(r".\Src\Util\Generator\config.json"):
        console.print("[red]=> Json file valid \n")
    else:
        console.log("[red]Json file is not valid (retry generator)")
        sys.exit(0)

    if msg.ask("[green]Do you want to auto generate headers file? (With login)") == "y":
        if msg.ask("[green]Have you already logged in ?") == "n":
            make_login()
        else:
            generate()

    print("\n")
    call_api.get_me()

    print("\n")
    if msg.ask("[green]Do you want to download media from a chat") == "y":
        call_api.get_list_chats()


    print("\n")
    call_api.get_follow()

    print("\n")
    if msg.ask("[green]Do you want to download avatar and header") == "y":
        call_api.download_avatar()

    print("\n")
    if msg.ask("[green]Do you want to download stories") == "y":
        call_api.download_stories()
    
    print("\n")
    if msg.ask("[green]Do you want to download all post") == "y":
        call_api.download_posts()

    print("\n")
    if msg.ask("[green]Do you want to download all highlights") == "y":
        call_api.download_high()

    console.log("\n[red]End")

main()