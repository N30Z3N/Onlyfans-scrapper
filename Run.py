# 31.12.23

# Class import
from Src.Api.api import Call_api
from Src.Util.Generator.generate_headers import generate, make_login
from Src.Util.Helper.console import console, msg
from Src.Util.Other.msg import hello
from Src.Util.upload.upload_v import main_update

call_api = Call_api()

def main():

    hello()
    main_update()

    if msg.ask("[green]Do you want to auto generare headers file? (With login)") == "y":
        if msg.ask("[green]Have yuo already logged in ?") == "n":
            make_login()
        else:
            generate()

    print("\n")
    call_api.get_me()

    print("\n")
    call_api.get_follow()

    print("\n")
    if msg.ask("[green]Do you want to donwload avatar and header") == "y":
        call_api.donwload_avatar()

    print("\n")
    if msg.ask("[green]Do you want to donwload stories") == "y":
        call_api.download_stories()
    
    print("\n")
    if msg.ask("[green]Do you want to donwload all post") == "y":
        call_api.download_posts()

    print("\n")
    if msg.ask("[green]Do you want to donwload all highligth") == "y":
        call_api.donwload_high()

    console.log("[red]End")

main()