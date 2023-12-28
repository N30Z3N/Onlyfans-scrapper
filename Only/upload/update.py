# 13.09.2023

# General import
import os, requests, zipfile, time
from rich.console import Console

# Variable
console = Console()


# Get main and base folder
main = os.path.abspath(os.path.dirname(__file__))
base = "\\".join(main.split("\\")[:-1])

def get_install_version():
    about = {}
    with open(os.path.join(main, '__version__.py'), 'r', encoding='utf-8') as f:
        exec(f.read(), about)
    return about['__version__']

def main_update():

    json = requests.get("https://api.github.com/repos/ghost6446/Onlyfans-scrapper/releases").json()[0]
    stargazers_count = requests.get("https://api.github.com/repos/ghost6446/Onlyfans-scrapper").json()['stargazers_count']
    last_version = json['name']
    down_count = json['assets'][0]['download_count']

    # Get percentaul star
    if down_count > 0 and stargazers_count > 0:
        percentual_stars = round(stargazers_count / down_count * 100, 2)
    else: percentual_stars = 0

    if get_install_version() != last_version:
        console.log(f"[red]A new version is available")

    else:
        console.log("[red]Everything up to date")
    
    print("\n")
    console.log(f"[red]Only was downloaded [yellow]{down_count} [red]times, but only [yellow]{percentual_stars}% [red]of You(!!) have starred it. \n\
        [cyan]Help the repository grow today, by leaving a [yellow]star [cyan]and [yellow]sharing [cyan]it to others online!")
    time.sleep(10)
    print("\n")
