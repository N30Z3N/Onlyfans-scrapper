# 5.07.2023 -> 12.09.2023

# Class import
from Src.Util.Helper.console import console

# General import
import os, time, subprocess, sys, platform
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Driver:
    def __init__(self):
        self.close_chrome_instances()
        self.service = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.driver = None

    def close_chrome_instances(self):
        print("\n")
        console.log(f"[green]Closing chrome ...")
        try:
            if platform.system() == "Linux":
                subprocess.check_output("pkill -f chrome", shell=True)
            elif platform.system() == "Windows":
                subprocess.check_output("TASKKILL /IM chrome.exe /F", shell=True, creationflags=0x08000000)
        except Exception as e:
            pass

    def create(self, headless=False, minimize=False):
        if headless:
            self.options.add_argument("headless")
        self.options.add_argument("--window-size=1280,1280")

        user_data_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Google', 'Chrome', 'User Data')
        if platform.system() == "Windows":
            user_data_dir = user_data_dir.replace('/', '\\')
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
        except Exception as e:
            console.log(f"[red]Can't get url: [green]{url}")
            sys.exit(0)

    def close(self):
        console.log("[red]Close driver")
        self.driver.close()
        self.driver.quit()
