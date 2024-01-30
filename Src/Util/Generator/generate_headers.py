# 31.12.23

# Import
from Src.Util.Helper.driver import Driver
from Src.Util.Helper.console import console
import time, json, sys

# Variable
sleep_time = 15
api_name = "users/me"
base_api = "api2"

def make_login():

    driver = Driver()
    driver.create(False)
    console.log("[cyan]Load home page")
    driver.get_page("https://onlyfans.com/", 5)
    time.sleep(999)

def generate():
    
    driver = Driver()
    driver.create(False, False)
    console.log("[cyan]Load home page")
    driver.get_page("https://onlyfans.com/", sleep_time)

    headers = None
    auth_headers = {}
    for req in driver.driver.requests:
        if base_api in str(req.url) and api_name in str(req.url):
            console.log("[green]Valid api: [red]FIND")
            headers = dict(req.headers)
            break

    if headers != None:

        for col in ['user-agent', 'app-token', 'accept', 'x-bc', 'accept-encoding', 'accept-language']:
            auth_headers[col] = headers[col]

        cookie_string = ("{" + str(headers['cookie']).replace("; ", "', '").replace("=", "':'") + "}")[1:-1]
        cookie_pairs = [pair.split("':'") for pair in cookie_string.split("', '")]
        cookie_dict = {key: value for key, value in cookie_pairs}

        auth_headers['user-id'] = cookie_dict['auth_id']
        auth_headers['cookie'] = "sess=" + cookie_dict["sess"]

        console.log("[green]Config.json file save ...")
        with open("Src/Util/Generator/config.json", 'w') as json_file:
            json.dump(auth_headers, json_file, indent=2)

        # Close driver
        driver.close()

    else:
        # Close driver and quit
        console.log("[red]Wrong headers")
        driver.close()
        sys.exit(0)
