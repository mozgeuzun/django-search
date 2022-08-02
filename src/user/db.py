
from cgi import print_form
from tkinter.tix import Select
from urllib import request
import mysql.connector
class db:
    @staticmethod
    def conn() :
        return mysql.connector.connect(
            host="db",
            user="root",
            password="12345",
            database="testdb1"
        )
    @staticmethod
    def liste(search:str):
        conn = db.conn()
        mycursor = conn.cursor()
        print(search, type(search))
        sql = "SELECT * FROM student WHERE (fnamestudent LIKE CONCAT('%','"+search+"','%') OR lnamestudent LIKE CONCAT('%','"+search+"','%'))"
       
        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()
        return myresult
    
    @staticmethod
    def delete(id:str):
        conn = db.conn()
        mycursor = conn.cursor()
        sql = "DELETE FROM student WHERE idstudent="+id
        print(sql)
        mycursor.execute(sql)
        conn.commit()
        mycursor.close()
        conn.close()
        return True


    @staticmethod
    def add(fnamestudent, lnamestudent, department):
        conn = db.conn()
        mycursor = conn.cursor()   
        mycursor.execute("INSERT INTO student (fnamestudent, lnamestudent, departnamestudent) VALUES (%s, %s, %s)",(fnamestudent, lnamestudent, department))          
        id = int(mycursor.lastrowid)
        conn.commit()
        mycursor.close()
        conn.close()
        print("ID",id)
        return id
   