import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
#mycursor.execute("insert into  Student_all_details_python.stud_per_iinfo values(1, 80.00 , 'sanjana' , 'Gijavane')")
#mycursor.execute("insert into  Student_all_details_python.stud_per_iinfo values(2, 88.00 , 'prerana' , 'Gijavane')")
#mycursor.execute("insert into  Student_all_details_python.stud_per_iinfo values(3, 80.78 , 'sonam' , 'Gadhinglaj')")
#mycursor.execute("insert into  Student_all_details_python.stud_per_iinfo values(4, 90.00 , 'sanika' , 'Gijavane')")
#mycursor.execute("insert into  Student_all_details_python.stud_per_iinfo values(5, 60.00 , 'soniya' , 'Pune')")

mycursor.execute("insert into  Student_all_details_python.stud_college_info values(101,80.00,'sanjana','pune',7)")
mycursor.execute("insert into  Student_all_details_python.stud_college_info values(102,80.00,'sanjana','pune',7)")
mycursor.execute("insert into  Student_all_details_python.stud_college_info values(103,80.00,'sanjana','pune',7)")
mycursor.execute("insert into  Student_all_details_python.stud_college_info values(104,80.00,'sanjana','pune',7)")
mycursor.execute("insert into  Student_all_details_python.stud_college_info values(105,80.00,'sanjana','pune',7)")



mydb.commit()

mydb.close()