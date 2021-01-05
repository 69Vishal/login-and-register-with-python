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

# checking creds with database
db = mysql.connector.connect(host='localhost', user='username', password='passs', database='database')
try:
    cursor = db.cursor()
    rqst = "select * from creds where username = '{}' and password = '{}';".format(username, password)
    cursor.execute(rqst)
    result = cursor.fetchone()
    if result == 'None':
        data_match = False
        text_to_print = 'login not successful'
    else:
        data_match = True
        text_to_print = 'login successful'
except:
    print('nothing found!')

# printing HTML page
print(f'''
<html>
<body><br>
{text_to_print}
</body>
</html>

''')