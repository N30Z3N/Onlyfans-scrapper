# 23.12.23

import sys
from Only.util.message import hello
from Only.only import Main
from Only.util.console import console, msg

def run():

    hello()

    cp = int(msg.ask(f"""
        [red][0]: [green]Make login,
        [red][1]: [green]Get all post
        [red][2]: [green]Get all media     
        [red][3]: [green]Get last post
        [red][4]: [green]Get last media
    """))

    us = str(msg.ask("[red]Insert username: ")).strip()
    console.log("\n[green]#####################################################\n")
    main_only = Main(us)

    # SWITCH DOESNT EXIST IN PYTHON 3.9
    if cp == 0:
        main_only.make_login()
    elif cp == 1:
        main_only.get_all_post()
    elif cp == 2:
        main_only.get_all_media()
    elif cp == 3:
        main_only.get_last_post()
    elif cp == 4:
        main_only.get_last_media()
    else:
        console.log("[red]Wrong")
        sys.exit(0)

run()