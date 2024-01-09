# 31.12.23

# Class import
from Src.Util.Helper.console import console

# Import
import requests, datetime, hashlib, sys, json

class OnlyRequest():

    def __init__(self):
        self.base_url = "https://onlyfans.com"
        self.api_url = "/api2/v2"
        self.profile_id = ""

    def get_rules(self):
        req = requests.get('https://raw.githubusercontent.com/DATAHOARDERS/dynamic-rules/main/onlyfans.json')
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
        if (queryParams):
            query = '&'.join('='.join((key, str(val))) for (key, val) in queryParams.items())
            path = f"{path}?{query}"

        unix_time = str(int(datetime.datetime.now().timestamp()))
        msg = "\n".join([self.rules["static_param"], unix_time, path, self.headers["user-id"]])
        message = msg.encode("utf-8")

        hash_object = hashlib.sha1(message)
        sha_1_sign = hash_object.hexdigest()
        sha_1_b = sha_1_sign.encode("ascii")

        checksum = sum([sha_1_b[number] for number in self.rules["checksum_indexes"]]) + self.rules["checksum_constant"]
        self.headers["sign"] = self.rules["format"].format(sha_1_sign, abs(checksum))
        self.headers["time"] = unix_time

    def api_request(self, endpoint, postdata=None, getparams=None):
        #print(f"MAKE REQ, URL = {self.base_url + self.api_url + endpoint}, POST DATA = {postdata}, PARAMS = {getparams}")

        if postdata is None:
            self.generate_sign(endpoint, getparams)
            req =  requests.get(self.base_url + self.api_url + endpoint, headers=self.headers, params=getparams)

            if req.status_code != 200:
                print(f"Error req -> {req.status_code}")
                sys.exit(0)

            return req

        else:
            self.generate_sign(endpoint, getparams)
            req =  requests.post(self.base_url + self.api_url + endpoint, headers=self.headers, params=getparams, data=postdata)
            
            if req.status_code != 200:
                print(f"Error req [{req.status_code}] -> {req.json()}")
                sys.exit(0)

            return req
        