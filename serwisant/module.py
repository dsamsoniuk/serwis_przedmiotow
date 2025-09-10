import requests
from PySide6 import QtCore
from service.TokenService import TokenService
import os

class ApiItemsModule():

    def __init__(self):
        pass

    def makeRequest(self, url: str, method: str = "get", data: dict = {}):
        token           = self.getToken()
        pageApiItemUrl  = os.environ.get('PAGE_API_ITEM_URL')

        headers = {
            "Content-Type": "application/json; charset=utf-8", 
            "Authorization": "Bearer " + token
        }

        if method == "get":
            response = requests.get(pageApiItemUrl + url, headers=headers, data=data)
        elif method == "post":
            response = requests.post(pageApiItemUrl + url, headers=headers, json=data)
        elif method == "patch":
            response = requests.patch(pageApiItemUrl + url, headers=headers, json=data)
        else:
            raise Exception("Brak dostępnej metody")
        
        if response.status_code != 200:
            message = " - Error ApiItem :: " + url + " :: " + str(response.json())
            raise Exception(message)

        return response
    
    def getToken(self):
        pageApiItemUrl          = os.environ.get('PAGE_API_ITEM_URL')

        settings        = QtCore.QSettings("MyApp", "Runner")
        tokenService    = TokenService()
        token           = settings.value('access_token') or False
        expireTime      = int(settings.value('expire_time')) or 0
        pageApiItemUsername     = settings.value('login')
        pageApiItemUPass        = settings.value('password')

        if tokenService.isExpired(expireTime) == True or token:
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
            payload = {
                'username': pageApiItemUsername, 
                'password': pageApiItemUPass
            }
            r = requests.post(pageApiItemUrl + '/token', headers=headers, data=payload)

            if r.status_code != 200:
                raise Exception("Brak dostępu do api items - fastapi")
            
            token = r.json()['access_token']
            expireTime = r.json()['expire_time']
            settings.setValue('access_token', token)
            settings.setValue('expire_time', expireTime)

        if isinstance(token, str) == False:
            raise Exception("Blad - brak tokena")
            
        return token
    