import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists Student_all_details_python.stud_college_info(roll_no int, per FLOAT , name VARCHAR(50) ,address VARCHAR(30),std int)")
mydb.close()