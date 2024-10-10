import requests


class TypiCodeController:
    def __init__(self):
        self.base_url = "http://jsonplaceholder.typicode.com/"

    def get_all_todos(self):
        url = self.base_url + "todos"
        res = requests.get(url).json()
        return res

    def get_all_users(self):
        url = self.base_url + "users"
        res = requests.get(url).json()
        return res
