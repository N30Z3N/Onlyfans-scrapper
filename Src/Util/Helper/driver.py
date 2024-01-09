# 5.07.2023 -> 12.09.2023

# General import
from Src.Util.Helper.console import console
import os, time, subprocess, sys
from sys import platform
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Driver:

    def close_chrome_instances(self):
        if platform.startswith("linux"):
            try: subprocess.check_output("pkill -f chrome", shell=True)
            except: pass

        elif platform == "win32":
            try: subprocess.check_output("TASKKILL /IM chrome.exe /F", shell=True, creationflags=0x08000000)
            except: pass

    def __init__(self) -> None:
        self.close_chrome_instances()
        self.service = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()

    def create(self, headless=False, minimize=False):
        if headless: self.options.add_argument("headless")
        self.options.add_argument("--window-size=1280,1280")

        user_data_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Google', 'Chrome', 'User Data')
        if platform == "win32": user_data_dir = user_data_dir.replace('/', '\\')
        self.options.add_argument(f'--user-data-dir={user_data_dir}')

        self.options.add_experimental_option("useAutomationExtension", True)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.options.add_argument('--ignore-ssl-errors=yes')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-insecure-localhost')
        self.options.add_argument("--allow-running-insecure-content")
        self.options.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(options=self.options, service=self.service)

        if minimize:
            self.driver.minimize_window()
            
    def get_page(self, url, sleep=1):
        try:
            self.driver.get(url)
            time.sleep(sleep)
        except:
            console.log(f"[red]Cant get url: [green]{url}")
            sys.exit(0)

    def close(self): 
        console.log("[red]Close driver")
        self.driver.close()
        self.driver.quit()
