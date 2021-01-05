#!/usr/bin/python3.8
# cgi formalities
print("Content-Type: text/html\n\r\n")

# import some shit
import cgitb, cgi, hashlib
import mysql.connector

# Get values from form
form = cgi.FieldStorage()
try:
    username = form.getvalue("username")
    password = form.getvalue("password")
except:
    print("<h1>Something went wrong!<h1>")

# function to encode username to sha256
def encode_username():
    global username
    result = hashlib.sha256(username.encode())
    final_hash = result.hexdigest()
    username = str(final_hash)
    return username

# function to encode password to sha256
def encode_password():
    global password
    result = hashlib.sha256(password.encode())
    final_hash = result.hexdigest()
    password = str(final_hash)
    return password

# executing definations
encode_username()
encode_password()

# uploading creds to database
db = mysql.connector.connect(host='localhost', user='username', password='passs', database='database')

cursor = db.cursor()
rqst = "INSERT INTO creds(username, password) VALUES('{}','{}');".format(username, password)
cursor.execute(rqst)
db.commit()

# printing HTML page
print(f'''
<html>
<body><br>
Thank you for registering, you can now Die!
</body>
</html>
''')