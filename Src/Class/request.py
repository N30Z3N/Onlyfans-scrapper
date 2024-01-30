# 31.12.23

# Class import
from Src.Util.Helper.console import console

# Import
import requests, time, hashlib, sys, json

class OnlyRequest():

    def __init__(self):
        self.base_url = "https://onlyfans.com"
        self.api_url = "/api2/v2"
        self.profile_id = ""

    def get_rules(self):
        req = requests.get('https://raw.githubusercontent.com/SneakyOvis/onlyfans-dynamic-rules/main/rules.json')
        if req.ok:
            self.rules = req.json()
        else:
            console.log(f"Cant get rules, error: {req.status_code}")
            sys.exit(0)

    def generate_auth(self):
        with open('Src/Util/Generator/config.json', 'r') as json_file:
            self.headers = json.load(json_file)
        
    def generate_sign(self, link, queryParams):
        path = self.api_url + link

        if queryParams:
            query = '&'.join('='.join((key, str(val))) for (key, val) in queryParams.items())
            path = f"{path}?{query}"

        timestamp = str(int(time.time() * 1000))
        msg = '\n'.join([self.rules['static_param'], timestamp, path, self.headers["user-id"]]).encode('utf-8')
        sha = hashlib.sha1(msg).hexdigest()
        checksum = sum(ord(sha[n]) for n in self.rules['checksum_indexes']) + self.rules['checksum_constant']
        
        self.headers["sign"] = ':'.join([self.rules['prefix'], sha, '%x' % checksum, self.rules['suffix']])
        self.headers["time"] = timestamp

    def api_request(self, endpoint, getparams=None):

        url = self.base_url + self.api_url + endpoint
        self.generate_sign(endpoint, getparams)

        try:
            response = requests.get(url, headers=self.headers, params=getparams)
            response.raise_for_status()
            return response

        except requests.RequestException as e:
            print(f"Error during API request: {e}")
            sys.exit(1)
        