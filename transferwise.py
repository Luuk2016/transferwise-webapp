#!flask/bin/python
import requests

BASE_URL = 'https://api.transferwise.com/v1'

class Transferwise:

    def __init__(self, apiKey):
        self.apiKey = apiKey

    def getProfileDetails(self):
        requestHeaders = {
            'Authorization': 'Bearer ' + self.apiKey
        }

        response = requests.get(BASE_URL + '/profiles',headers=requestHeaders)
        response.raise_for_status()

        responseBody = response.json()

        return responseBody[0]

    def getBalances(self, profileID):
        requestHeaders = {
            'Authorization': 'Bearer ' + self.apiKey
        }

        response = requests.get(BASE_URL + '/borderless-accounts?profileId='+str(profileID),headers=requestHeaders)
        response.raise_for_status()

        responseBody = response.json()

        return responseBody