# 22.12.2023

# Import
import os
from Src.Util.Helper.console import console

# [Function]
def hello():

    os.system("CLS")

    msg = """  /$$$$$$                  /$$          
 /$$__  $$                | $$          
| $$  \ $$ /$$$$$$$       | $$ /$$   /$$
| $$  | $$| $$__  $$      | $$| $$  | $$
| $$  | $$| $$  \ $$      | $$| $$  | $$
| $$  | $$| $$  | $$      | $$| $$  | $$
|  $$$$$$/| $$  | $$      | $$|  $$$$$$$
 \______/ |__/  |__/      |__/ \____  $$
                               /$$  | $$
                              |  $$$$$$/
                               \______/ """

    console.print(f"[purple]{msg}")