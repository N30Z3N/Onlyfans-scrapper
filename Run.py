# 23.12.23 -> 28.12.23

# Class import
from Only.src.util.message import hello
from Only.src.util.console import console, msg
from Only.only import Main

# General import
import sys

def run():

    hello()

    cp = int(msg.ask(f"""        
        [yellow][Auto]
        [red][0]: [green]Make login
                     
        [yellow][Download]
        [red][1]: [green]Get all post
        [red][2]: [green]Get last post
        [red][3]: [green]Get all media     
        [red][4]: [green]Get last media
                     
        [yellow][Profile data]
        [red][5]: [green]Get char (whit id)
                     
        [yellow][Profile info]
        [red][6]: [green]Get social buttons
        [red][7]: [green]Get list subscribe
        [red][8]: [green]Download profile photo
        [red][9]: [green]Donwload avatar photo

    """))

    print("\n\n")
    us = str(msg.ask("[red]Insert username: ")).strip()
    print("\n")
    main_only = Main(us)

    # SWITCH DOESNT EXIST IN PYTHON 3.9
    if cp == 0:
        main_only.make_login()

    elif cp == 1:
        main_only.get_all_post()
    elif cp == 2:
        main_only.get_last_post()
    elif cp == 3:
        main_only.get_all_media()
    elif cp == 4:
        main_only.get_last_media()

    elif cp == 5:
        id_chat = str(msg.ask("[red]Insert chat id: ")).strip()
        main_only.get_chat(id_chat)

    elif cp == 6:
        main_only.get_social_buttons()
    elif cp == 7:
        main_only.get_list_first_subscribe()
    elif cp == 8:
        main_only.get_profile_photo()
    elif cp == 9:
        main_only.get_avatar_photo()

    else:
        console.log("[red]Wrong")
        sys.exit(0)

run()