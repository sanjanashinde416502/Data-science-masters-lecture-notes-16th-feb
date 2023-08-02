import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test2_table values(12,2.3445,'sanjana',4.5,'sudh')")
mycursor.execute("insert into test2.test2_table values(12,2.3445,'sanjana',4.5,'sudh')")
mycursor.execute("insert into test2.test2_table values(12,2.3445,'sanjana',4.5,'sudh')")
mycursor.execute("insert into test2.test2_table values(12,2.3445,'sanjana',4.5,'sudh')")
mycursor.execute("insert into test2.test2_table values(12,2.3445,'sanjana',4.5,'sudh')")
mycursor.execute("insert into test2.test2_table values(12,2.3445,'sanjana',4.5,'sudh')")
mycursor.execute("insert into test2.test2_table values(12,2.3445,'sanjana',4.5,'sudh')")
mycursor.execute("insert into test2.test2_table values(12,2.3445,'sanjana',4.5,'sudh')")
mydb.commit()  # while inserting data we should always commite the data 
#mysqldump -u <username> -p<password> <database_name> > <filename>.sql  to save
mydb.close()