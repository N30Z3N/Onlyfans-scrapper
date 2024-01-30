# 31.12.23

# Import
from Src.Util.Helper.console import console
import requests, time, os

def download(url, path, headers=None, sleep_seconds=2):
    
    file_name = os.path.basename(path)

    if os.path.exists(path):
        console.log(f"[red]Skip file exists: {file_name}")
        return

    console.log(f"[red]Save: [cyan]{file_name}")

    try:
        req = requests.get(url, headers=headers)

        if req.status_code == 200:
            with open(path, 'wb+') as f:
                f.write(req.content)
        else:
            console.log(f"[red]Failed to download file: {path}, status: {req.status_code}")
            time.sleep(sleep_seconds)

    except Exception as e:
        console.log(f'[yellow]Failed to download: {path}, error: {e}')

