from requests import Session
import uuid
import os
from time import sleep
from colorama import Fore, init
init()
session = Session()

class Auth:
    Auth_URL = 'https://cracked.io/auth.php'
    Auth_Key = ''
    UUID = []


def CrackedAuth(auth, save=None, info=None, error_exit=None):
    global CrackedUsername, CrackedPost, CrackedLikes, CrackedRank, CrackedErrorAuth

    if save is None:
        save = False
    else:
        save = save
    if info is None:
        info = False
    else:
        info = info
    if error_exit is None:
        error_exit = False
    else:
        error_exit = error_exit

    if auth == str(auth):
        json = {
            "a": "auth",
            "k": str(auth),
            "hwid": str(
                uuid.getnode()
                )
        }
        
        CrackedRequest = session.post(url=Auth.Auth_URL, data=json)
        CrackedData = CrackedRequest.json()
        
        if '"auth":true' in CrackedRequest.text:
            CrackedUsername = CrackedData['username']
            CrackedLikes = CrackedData['likes']
            CrackedPost = CrackedData['posts']
            CrackedRank = CrackedData['group']
            
            if save == True:
                if info == True:
                    print(f'{Fore.LIGHTGREEN_EX}-{Fore.WHITE} Successfully logged in.{Fore.RESET}')
                    if os.path.isfile('Auth.auth'):
                        pass
                    else:
                        try:
                            save = open('Auth.auth')
                            save.write(auth)
                        except FileNotFoundError:
                            s = open('Auth.auth', 'w')
                            s.write(auth)
                else:
                    pass
            elif save == False:
                if info == True:
                    print(f'{Fore.LIGHTGREEN_EX}-{Fore.WHITE} Successfully logged in.{Fore.RESET}')
            else:
                pass

        if '"error":"invalid key"' in CrackedRequest.text:
            if info == True:
                if error_exit == True:
                    print(f'{Fore.RED}- {Fore.WHITE}Failed to authenticate with cracked.io key, {Fore.GREEN}closing application{Fore.RESET}')
                else:
                    print(f'{Fore.RED}- {Fore.WHITE}Failed to authenticate with cracked.io key{Fore.RESET}')
            CrackedErrorAuth = '"error":"invalid key"'