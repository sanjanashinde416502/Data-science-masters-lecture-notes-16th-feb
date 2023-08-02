import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test2")
mydb.close()
# here in output exited with code =0 means code runned successufly
# if we go to demo.py file by reloding it we can see test2 file even in 
# going database we can see test2 database by reloading it .
# here we are doing creating of database by using python