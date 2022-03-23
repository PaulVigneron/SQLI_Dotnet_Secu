import cgi

print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Security</title>
</head>
<body>
    <h1>Bienvenue</h1>
    <form method="post" action="connexion.py">
        <p>Username</p><input type="text" name="username">
        <p>Password</p><input type="text" name="password">
        <input type="submit" value="Envoyer">
    </form>
</body>
</html>
"""

print(html)