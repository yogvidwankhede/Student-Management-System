import mysql.connector
from tabulate import tabulate

myconn = mysql.connector.connect(host="localhost",
                                 user="root ",
                                 password="abc123",
                                 database="collegedb",
                                 port="3307"
                                 )
mycursor = myconn.cursor()

class Student:
    list = ["STUDENT NUMBER", "NAME", "ROLL NUMBER",
            "MATHEMATICS", "PHYSICS", "CHEMISTRY", "RESULT"]
    m = 0
    db = None
    colNum = None
    
    def Set_Details(self):
        self.m = int(input("Enter Number Of Students Data to be added: "))
        print("\n")
        for self.k in range(0, self.m):
            print("Enter Student", (self.k + 1), "Information: \n")
            self.name = input("Enter your name : ")
            self.roll_number = int(input("Enter your roll no. : "))
            self.mathematics = int(input("Enter marks in Mathematics : "))
            self.physics = int(input("Enter marks of Physics : "))
            self.chemistry = int(input("Enter marks of Chemistry : "))
            print('------------------------------------')
            self.result = (
                float((self.mathematics + self.physics + self.chemistry)/3))
            sql = "insert into collegedb.collegetb(Name, Roll_Number, Mathematics, Physics, Chemistry, Result) values(%s, %s, %s, %s, %s, %s);"
            value = (self.name, self.roll_number, self.mathematics,
                     self.physics, self.chemistry, float(self.result))
            mycursor.execute(sql, value)
            myconn.commit()
            print("Data Inserted")
            print("\n")

    def Display_Details(self):
        mycursor.execute("SELECT * FROM collegetb")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=self.list,
              tablefmt="grid", floatfmt=".2f"))

    def delete_student(self):
        sql = "DELETE FROM collegetb WHERE Roll_Number = %s"
        self.x = int(input("Enter Roll Number to delete data: "))
        mycursor.execute(sql, (self.x,))
        myconn.commit()

    def update_student(self):
        update = "UPDATE collegetb SET Name = %s WHERE Roll_Number = %s "
        update_r = "UPDATE collegetb SET Roll_Number = %s WHERE Roll_Number = %s "
        update_p1 = "UPDATE collegetb SET Mathematics = %s WHERE Roll_Number = %s "
        update_p2 = "UPDATE collegetb SET Physics = %s WHERE Roll_Number = %s "
        update_p3 = "UPDATE collegetb SET Chemistry = %s WHERE Roll_Number = %s "
        update_res = "UPDATE collegetb SET Result = %s WHERE Roll_Number = %s"

        v = 1
        self.q = int(input("Enter roll no. : "))
        while v == 1:
            print('''What would you like to update
                1. Name.
                2. Roll Number.
                3. Marks In Mathematics.
                4. Marks In Physics.
                5. Marks In Chemistry.
                6. Exit 
                  ''')
            self.ch = int(input("Enter choice: "))
            if self.ch == 1:
                mycursor.execute(
                    "SELECT Name FROM collegetb where Roll_Number= %s ", (self.q,))
                row = mycursor.fetchone()
                print('Your current name : ', row[0])
                self.na = input("Enter New name:  ")
                val = (self.na, self.q)
                mycursor.execute(update, val)
                myconn.commit()
                print('Record Updated')
                print('------------------------------------')
            elif self.ch == 2:
                mycursor.execute(
                    "SELECT Roll_Number FROM collegetb where Roll_Number= %s ", (self.q,))
                row = mycursor.fetchone()
                print('Your current roll : ', row[0])
                self.rl = input("Enter New roll:  ")
                val = (self.rl, self.q)
                mycursor.execute(update_r, val)
                myconn.commit()
                print('Record Updated')
                print('------------------------------------')
            elif self.ch == 3:
                mycursor.execute(
                    "SELECT Mathematics FROM collegetb where Roll_Number= %s ", (self.q,))
                row = mycursor.fetchone()
                print('Your current Mathematics marks : ', row[0])
                self.p1 = int(input("Enter marks:  "))
                val = (self.p1, self.q)
                mycursor.execute(update_p1, val)
                mycursor.execute(
                    "SELECT Physics FROM collegetb where Roll_Number= %s ", (self.q,))
                p2 = mycursor.fetchone()
                mycursor.execute(
                    "SELECT Chemistry FROM collegetb where Roll_Number= %s ", (self.q,))
                p3 = mycursor.fetchone()
                self.r = (self.p1 + p2[0] + p3[0])/3
                value = (self.r, self.q)
                mycursor.execute(update_res, value)
                myconn.commit()
                print('Record Updated')
                print('------------------------------------')
            elif self.ch == 4:
                mycursor.execute(
                    "SELECT Physics FROM collegetb where Roll_Number= %s ", (self.q,))
                row = mycursor.fetchone()
                print('Your current Physics marks : ', row[0])
                self.p2 = input("Enter marks:  ")
                val = (self.p2, self.q)
                mycursor.execute(update_p2, val)
                mycursor.execute(
                    "SELECT Mathematics FROM collegetb where Roll_Number= %s ", (self.q,))
                p1 = mycursor.fetchone()
                mycursor.execute(
                    "SELECT Chemistry FROM collegetb where Roll_Number= %s ", (self.q,))
                p3 = mycursor.fetchone()
                self.r = (p1[0] + self.p2 + p3[0])/3
                value = (self.r, self.x)
                mycursor.execute(update_res, value)
                myconn.commit()
                print('Record Updated')
                print('------------------------------------')
            elif self.ch == 5:
                mycursor.execute(
                    "SELECT Chemistry FROM collegetb where Roll_Number= %s ", (self.q,))
                row = mycursor.fetchone()
                print('Your current Chemistry marks : ', row[0])
                self.p3 = input("Enter marks:  ")
                val = (self.p3, self.q)
                mycursor.execute(update_p3, val)
                mycursor.execute(
                    "SELECT Physics FROM collegetb where Roll_Number= %s ", (self.q,))
                p2 = mycursor.fetchone()
                mycursor.execute(
                    "SELECT Mathematics FROM collegetb where Roll_Number= %s ", (self.q,))
                p1 = mycursor.fetchone()
                self.r = (p1[0] + p2[0] + self.p3)/3
                value = (self.r, self.q)
                mycursor.execute(update_res, value)
                myconn.commit()
                print('Record Updated')
                print('------------------------------------')
            elif self.ch == 6:
                v = 0
                val = (self.m)
                mycursor.execute("SELECT * FROM collegetb")
                tb = mycursor.fetchall()
                print(tabulate(tb, headers=self.list,
                               tablefmt="grid", floatfmt=".2f"))
                myconn.commit()
                print('------------------------------------')
            else:
                print("!!!!INVALID CHOICE!!!!")
                print('------------------------------------')

    def search_student(self):
        self.x = int(input("Enter Roll Number to search data: "))
        mycursor.execute(
            "SELECT * FROM collegetb WHERE Roll_Number = %s", (self.x,))
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=self.list,
              tablefmt="grid", floatfmt=".2f"))


obj = Student()
print("\n")
print("Welcome to Student Management System")

while True:

    print("\n")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Search Student")
    print("6. Quit")
    print("\n")

    choice = input("Enter your choice: ")
    if choice == '1':
        obj.Set_Details()
        print("\n")
    elif choice == '2':
        obj.Display_Details()
        print("\n")
    elif choice == '3':
        obj.delete_student()
        print("List After Deletion")
        obj.Display_Details()
        print("\n")
    elif choice == '4':
        obj.update_student()
    elif choice == '5':
        obj.search_student()
        print("\n")
    elif choice == '6':
        print("Thank-You")
        break
    else:
        print("Wrong Choice")
