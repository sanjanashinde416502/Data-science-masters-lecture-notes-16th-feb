# here we can easily do things that we can do in sql so then why we should use pyhthn because for 
# an appication we write all code in python and all work should be python so this reason pyhton 
# connectivity and executing through pyhton is neccessory so thats here we are learning

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
#mycursor.execute("select * from test2.test2_table")  # to get all data in table
mycursor.execute("select c1,c2,c3 from test2.test2_table") # to get specific columns data
for i in mycursor.fetchall():
    print(i)
mydb.close()