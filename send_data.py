#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:16:25 2020

@author: ewaldozihan
"""
# importing the requests library 
import requests 
import json

# URL INFO
url_mcp = <URL>
url_auth = url_mcp +'/tron/api/v1/tokens'

username = 'zihan'
password = 'pass'

# alarm_filter
severity = 'CRITICAL'
service_affecting = 'SERVICE_AFFECTING'
acknowledg_state = ''
number_of_alarm = '10'

# Extract JSON
def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results
  
import telegram
from telegram.ext import Updater

TOKEN = <TOKEN>
ID = <ID>

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)

#CHAT_ID = bot.get_updates()[-1].message.chat_id
def sendToTelegram(alarms):
    bot.send_message(chat_id=<TOKEN>, text=alarms)
    print ('Message Sent')
    return;

# defining a params dict for the parameters to be sent to the API 
auth = {'username' : username,
          'password' : password}
  
# sending get request and saving the response as response object 
auth_res = requests.post(url = url_auth, data = auth, verify= False) 
  
# extracting data in json format 
auth_res = auth_res.json() 

# Get Alarm
url_act_alarm = url_mcp + '/nsa/api/v1/alarms/filter/activeAlarms'


# defining a params dict for the parameters to be sent to the API 
header_params = {'accept': 'application/json',
         'Authorization':'Bearer ' + auth_res['token']} 

url_alrm_fin = url_act_alarm + '?severity='+ severity + '&serviceAffecting=' + service_affecting + '&acknowledgeState=' + acknowledg_state + '&pageSize=' + number_of_alarm
  
# sending get request and saving the response as response object 
response = requests.get(url = url_alrm_fin, headers=header_params, verify= False) 

alarm = r.json() 

# Send to Telegram
sendToTelegram(alarm['data'])



