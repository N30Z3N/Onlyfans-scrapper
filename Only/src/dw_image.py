# 24.10.2023

# General import
import requests
from Only.src.util.console import console

def donwload_image(url, name, folder):
    r = requests.get(url)
    if r.ok: open(folder + "\\" + name, "wb").write(r.content)
    else: console.log(f"[red]Cant get [green]{url}: [yellow]{r.status_code}")
