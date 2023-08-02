# here we are creating table by python 
# for creating table just give command used to create table 
# inside the 'mycursor.exceute()' then run the code. 
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists test2.test2_table(c1 int, c2 FLOAT , c3 VARCHAR(50), c4 FLOAT , c5 VARCHAR(30))")
mydb.close()