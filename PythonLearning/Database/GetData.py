import requests

class ApiAccess:

    def __init__(self,url):
        self.url=url


    def getrequestdata(self):
        requestdata = requests.get(self.url)
        return requestdata.json()


