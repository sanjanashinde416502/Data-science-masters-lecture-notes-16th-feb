import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
# to get all data:
# mycursor.execute("select *from Student_all_details_python.stud_college_info")
#for i in mycursor.fetchall():
 #   print(i)


# to get specific data:
#mycursor.execute("select roll_no,per,name from Student_all_details_python.stud_college_info")
#for i in mycursor.fetchall():
 #   print(i)

 # to get all data in (Stud_per_info_table):
#mycursor.execute("select *from Student_all_details_python.stud_per_iinfo")
#for i in mycursor.fetchall():
 #   print(i)

# to get secific data form(Stud_per_info_table):
mycursor.execute("select roll_no , name,address from Student_all_details_python.stud_college_info")
for i in mycursor.fetchall():
    print(i)



mydb.close()