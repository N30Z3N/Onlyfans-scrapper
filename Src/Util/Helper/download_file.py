# 31.12.23

# Import
from Src.Util.Helper.console import console
import requests, time, os

def download(url, path, headers=None, ss=2):
    file_name = path.split('\\')[-1]

    if not os.path.exists(path):
        console.log(f"[green]Save: [cyan]{file_name}")

        try:
            req = requests.get(url, headers=headers)

            if(req.status_code == 200):
                with open(path, 'wb+') as f:
                    f.write(req.content)
            else:
                console.log(f"[red]Failed to download file: {path}, status: {req.status_code}")
                time.sleep(ss)

        except Exception as e:
            console.log(f'[yellow]Failed to download: {path}, e: {e}')

    else:
        console.log(f"[red]Skip file exist: {file_name}")

