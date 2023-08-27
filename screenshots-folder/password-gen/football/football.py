import requests
import time
import json
from win10toast import ToastNotifier

def update():
    uri = "https://api.football-data.org/v4/competitions/PL/teams"
    headers = {'X-Auth-Token': '7ceab684f89c4d139c153a8560001ecd'}

    r = requests.get(uri, headers=headers)
    #print(r.json()['matches'])
    for match in r.json()['teams']:
       print(match) 

    while True:
        toast = ToastNotifier()
        toast.show_toast(match, duration=20)
        time.sleep(20)


update()
    