# 31.12.23

# Class import
from Src.Api.api import Call_api
from Src.Util.Generator.generate_headers import generate, make_login
from Src.Util.Helper.console import console, msg
from Src.Util.Other.msg import hello
from Src.Util.upload.upload_v import main_update

# Import
import sys

call_api = Call_api()

def main():

    hello()
    try: main_update()
    except: 
        console.log("[red]Cant connect to github")
        sys.exit(0)

    if msg.ask("[green]Do you want to auto generate headers file? (With login)") == "y":
        if msg.ask("[green]Have you already logged in ?") == "n":
            make_login()
        else:
            generate()

    print("\n")
    call_api.get_me()

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