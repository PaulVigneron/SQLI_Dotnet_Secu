#coding:utf-8
import mysql.connector as mc
import cgi
import cgitb
import hashlib

cgitb.enable()
form = cgi.FieldStorage()

try:
    # A modifier pour bien se connecter à son localhost
    conn = mc.connect(host = 'localhost', database = 'secu', user = 'root', password = '')
    cursor = conn.cursor()
    
    print("Content-type: text/html; charset=utf-8\n")

    html = """<!DOCTYPE html>
    <head>
        <meta charset="UTF-8">
        <title>Accueil</title>
    </head>
    <body>
        <h1>Accueil</h1>
    """
    print(html)
    
    username = form.getvalue("username")
    passw = form.getvalue("password")
    md5hash = hashlib.md5()
    md5hash.update(passw.encode("utf8"))
    passw = md5hash.hexdigest()

    cursor.execute("SELECT * FROM admin WHERE username = '%s' OR password = 'test'" % username)

    users = cursor.fetchall()
    
    for user in users:
        if passw == user[2]:
            print('Connected')
        else:
            print("Incorrect")
    
except mc.Error as err:
    print(err)
finally:
    if(conn.is_connected()):
        cursor.close()
        conn.close()

# Affiche Incorrect quand le mdp n'est pas le bon et Connected si c'est le bon

# admin1 
# Récupère 2 users (le champ user + celui la fin de la requête SQL test)dont 1 qui peut se connecter si il a le bon mdp 

# admin1'; -- -
# Récupère un seul user (met en commentaire le reste de la requête)

# admin1' and (SELECT substr(password, 1, 1) = "e" FROM admin limit 1) -- -
# Affiche Connected si le caractère recherché est bon
# Affiche rien si c'est pas le bon caractère
