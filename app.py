from flask import Flask 
import pyodbc
import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

app = Flask(__name__)

driver = '{ODBC Driver 18 for SQL Server}'
database = 'adb1'
server = 'tcp:adb1server.database.windows.net,1433'
username = "mxj3280"
password = "Mjuta2022!16"
conn= pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = conn.cursor() #cursor 
cursor.execute('''Select * from all_day''')
check_username=cursor.fetchall()
print(check_username)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"