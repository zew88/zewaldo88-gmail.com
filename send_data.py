#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:16:25 2020

@author: ewaldozihan
"""
# importing the requests library 
import requests 

  
url_mcp = 'https://172.30.20.20'
url_auth = url_mcp +'/tron/api/v1/tokens'

username = 'zihan'
password = 'Password!123'

# alarm_filter
severity = 'CRITICAL'
service_affecting = 'SERVICE_AFFECTING'
acknowledg_state = ''
number_of_alarm = '10'

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
r = requests.get(url = url_alrm_fin, headers=header_params, verify= False) 

alarm = r.json() 

#curl -X GET "https://172.30.20.20/nsa/api/v1/alarms/filter/activeAlarms?severity=CRITICAL&offset=0&pageSize=500" -H "accept: application/json" -H "Token: c4822817f60089718db8"