from functools import partial
from tkinter import *
from tkinter import ttk
from unicodedata import name
import mysql.connector
conn = mysql.connector.connect(host="localhost",
                               user="root ",
                               password="abc123",
                               database="tkdb",
                               port="3307"
                               )
print(conn, "connected")
mycursor = conn.cursor()
insert = "INSERT INTO tkdb.tktb(Roll,FName,LName) VALUES(%s,%s,%s)"
show = "SELECT * FROM tkdb.tktb"
fupdate = "UPDATE tkdb.tktb SET FName = %s WHERE Roll = %s "
lupdatel = "UPDATE tkdb.tktb SET LName = %s WHERE Roll = %s "
delete = "DELETE FROM tkdb.tktb WHERE Roll = %s"
search = "SELECT * FROM tkdb.tktb where Roll= %s "


class Management_System():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x300+500+200')
        self.root.title("Management_System")

    def geometry(self):
        self.branch = Tk()
        self.branch.geometry('350x300+520+200')
        self.branch.title("Management_System")

    def Interface(self):
        self.lab = Label(self.root).grid(row=1, column=2)
        self.label = Label(self.root, text="WELCOME",
                           font='Verdana 16').grid(row=1, column=4)
        self.label0 = Label(self.root, text="What would you like to do ?",
                            font='Verdana 14').grid(row=2, column=4)
        Exit = partial(self.Exit, self.root)
        self.bttn1 = Button(self.root, text="INSERT", command=self.Insert_Interface,
                            font='Verdana 12').grid(row=3, column=4)
        self.bttn2 = Button(self.root, text="SHOW", command=self.showdata,
                            font='Verdana 12').grid(row=4, column=4)
        self.bttn2 = Button(self.root, text="SEARCH", command=self.Search_Interface_1,
                            font='Verdana 12').grid(row=5, column=4)
        self.bttn2 = Button(self.root, text="UPDATE", command=self.Update_Interface,
                            font='Verdana 12').grid(row=6, column=4)
        self.bttn2 = Button(self.root, text="DELETE", command=self.Delete_Interface_1,
                            font='Verdana 12').grid(row=7, column=4)
        self.bttn2 = Button(self.root, text="EXIT", command=Exit,
                            font='Verdana 12').grid(row=8, column=4)
        self.root.mainloop()

    def Insert_Interface(self):
        self.geometry()
        self.roll = StringVar()
        self.fname = StringVar()
        self.lname = StringVar()
        self.labelNum1 = Label(self.branch, text="Roll No.",
                               font='Verdana 12').grid(row=1, column=0)
        self.labelNum2 = Label(
            self.branch, text="First Name", font='Verdana 12').grid(row=2, column=0)
        self.labelNum3 = Label(self.branch, text="Last Name",
                               font='Verdana 12').grid(row=3, column=0)
        self.entryRoll = Entry(self.branch, textvariable=self.roll)
        self.entryRoll.grid(row=1, column=2)
        self.entryFname = Entry(self.branch, textvariable=self.fname)
        self.entryFname.grid(row=2, column=2)
        self.entryLname = Entry(self.branch, textvariable=self.lname)
        self.entryLname.grid(row=3, column=2)
        Exit = partial(self.Exit, self.branch)
        self.bttn = Button(self.branch, text="SUBMIT",
                           command=self.insertdata, font='Verdana 12').grid(row=4, column=2)
        self.bttn1 = Button(self.branch, text="EXIT", command=Exit,
                            font='Verdana 12').grid(row=5, column=2)
        self.branch.mainloop()

    def insertdata(self):
        r = self.entryRoll.get()
        r1 = int(r)
        fn = (self.entryFname.get())
        ln = (self.entryLname.get())
        val = (r1, fn, ln)
        mycursor.execute(insert, val)
        conn.commit()
        self.Clear_Data()

    def Show_Interface(self):
        self.geometry()
        show_frame = Frame(self.branch)
        show_frame.pack()
        scrll = Scrollbar(show_frame)
        scrll.pack(side=RIGHT, fill=Y)
        scrll = Scrollbar(show_frame, orient='horizontal')
        scrll.pack(side=BOTTOM, fill=X)
        trev = ttk.Treeview(
            show_frame, yscrollcommand=scrll.set, xscrollcommand=scrll.set)
        trev.pack()
        scrll.config(command=trev.yview)
        scrll.config(command=trev.xview)
        trev['columns'] = ('roll', 'fname', 'lname')
        trev.column("#0", width=0,  stretch=NO)
        trev.column("roll", anchor=CENTER, width=80)
        trev.column("fname", anchor=CENTER, width=100)
        trev.column("lname", anchor=CENTER, width=100)

        trev.heading("#0", text="", anchor=CENTER)
        trev.heading("roll", text="Roll No.", anchor=CENTER)
        trev.heading("fname", text="First Name", anchor=CENTER)
        trev.heading("lname", text="Last Name", anchor=CENTER)

        for i in range(self.l):
            trev.insert(parent='', index='end', iid=i,
                        text='', values=self.a[i])
        trev.pack()
        Exit = partial(self.Exit, self.branch)
        self.bttn1 = Button(self.branch, text="EXIT", command=Exit,
                            font='Verdana 12')
        self.bttn1.pack()

    def showdata(self):
        mycursor.execute(show)
        self.a = mycursor.fetchall()
        self.l = len(self.a)
        self.Show_Interface()
        conn.commit()

    def Search_Interface_1(self):
        self.branch = Tk()
        self.branch.geometry('220x120+550+200')
        self.branch.title("Management_System")
        roll = StringVar()
        self.labNum1 = Label(self.branch, text="Enter your Roll No.",
                             font='Verdana 12').grid(row=1, column=0)
        self.entryRoll = Entry(self.branch, textvariable=roll)
        self.entryRoll.grid(row=2, column=0)
        Exit = partial(self.Exit, self.branch)
        self.bttn = Button(self.branch, text="SUBMIT",
                           command=self.Search_Interface_2, font='Verdana 10').grid(row=5, column=0)
        self.bttn1 = Button(self.branch, text="EXIT", command=Exit,
                            font='Verdana 10').grid(row=6, column=0)
        self.branch.mainloop()

    def Search_Interface_2(self):
        self.branch = Tk()
        self.branch.geometry('300x200+550+200')
        self.branch.title("Management_System")
        self.x = self.entryRoll.get()
        self.x = int(self.x)
        mycursor.execute(search, (self.x,))
        self.dt = mycursor.fetchone()
        self.labNum1 = Label(self.branch, text="Roll No.",
                             font='Verdana 12').grid(row=1, column=0)
        self.labNum2 = Label(self.branch, text="First Name",
                             font='Verdana 12').grid(row=2, column=0)
        self.labNum3 = Label(self.branch, text="Last Name",
                             font='Verdana 12').grid(row=3, column=0)
        self.entryRoll = Entry(self.branch, width=20, font=(
            'Arial'), disabledbackground='grey')
        self.entryRoll.insert(END, self.dt[0])
        self.entryRoll.grid(row=1, column=1)
        self.entryFname = Entry(self.branch, width=20, font=('Arial'))
        self.entryFname.insert(END, self.dt[1])
        self.entryFname.grid(row=2, column=1)
        self.entryLname = Entry(self.branch, width=20, font=('Arial'))
        self.entryLname.insert(END, self.dt[2])
        self.entryLname.grid(row=3, column=1)
        self.mssglab = Label(self.branch)
        self.mssglab.grid(row=7, column=1)
        Exit = partial(self.Exit, self.branch)
        self.bttn1 = Button(self.branch, text="EXIT", command=Exit,
                            font='Verdana 10').grid(row=6, column=1)
        conn.commit()
        self.branch.mainloop()

    def Update_Interface(self):
        self.branch = Tk()
        self.branch.geometry('220x120+550+200')
        self.branch.title("Management_System")
        roll = StringVar()
        self.labNum1 = Label(self.branch, text="Enter your Roll No.",
                             font='Verdana 12').grid(row=1, column=0)
        self.entryRoll = Entry(self.branch, textvariable=roll)
        self.entryRoll.grid(row=2, column=0)
        Exit = partial(self.Exit, self.branch)
        self.bttn = Button(self.branch, text="SUBMIT",
                           command=self.Update_Interface_2, font='Verdana 10').grid(row=5, column=0)
        self.bttn1 = Button(self.branch, text="EXIT", command=Exit,
                            font='Verdana 10').grid(row=6, column=0)
        self.branch.mainloop()

    def Update_Interface_2(self):
        self.branch = Tk()
        self.branch.geometry('300x200+550+200')
        self.branch.title("Management_System")
        self.x = self.entryRoll.get()
        self.x = int(self.x)
        mycursor.execute(search, (self.x,))
        self.dt = mycursor.fetchone()
        self.labNum1 = Label(self.branch, text="Roll No.",
                             font='Verdana 12').grid(row=1, column=0)
        self.labNum2 = Label(self.branch, text="First Name",
                             font='Verdana 12').grid(row=2, column=0)
        self.labNum3 = Label(self.branch, text="Last Name",
                             font='Verdana 12').grid(row=3, column=0)
        self.entryRoll = Entry(self.branch, width=20, font=(
            'Arial'), disabledbackground='grey')
        self.entryRoll.insert(END, self.dt[0])
        self.entryRoll.grid(row=1, column=1)
        self.entryFname = Entry(self.branch, width=20, font=('Arial'))
        self.entryFname.insert(END, self.dt[1])
        self.entryFname.grid(row=2, column=1)
        self.entryLname = Entry(self.branch, width=20, font=('Arial'))
        self.entryLname.insert(END, self.dt[2])
        self.entryLname.grid(row=3, column=1)
        self.mssglab = Label(self.branch)
        self.mssglab.grid(row=7, column=1)
        Exit = partial(self.Exit, self.branch)
        update = partial(self.update, self.mssglab)
        self.bttn = Button(self.branch, text="ENTER", command=update,
                           font='Verdana 10').grid(row=5, column=1)
        self.bttn1 = Button(self.branch, text="EXIT", command=Exit,
                            font='Verdana 10').grid(row=6, column=1)
        self.branch.mainloop()

    def update(self, label):
        fname = (self.entryFname.get())
        lname = (self.entryLname.get())
        mycursor.execute(fupdate, (fname, self.x))
        mycursor.execute(lupdatel, (lname, self.x))
        conn.commit()
        label.config(text='Record has been updated', font=('Arial', 12))

    def Delete_Interface_1(self):
        self.branch = Tk()
        self.branch.geometry('220x120+550+200')
        self.branch.title("Management_System")
        roll = StringVar()
        self.labNum1 = Label(self.branch, text="Enter your Roll No.",
                             font='Verdana 12').grid(row=1, column=0)
        self.entryRoll = Entry(self.branch, textvariable=roll)
        self.entryRoll.grid(row=2, column=0)
        Exit = partial(self.Exit, self.branch)
        self.bttn = Button(self.branch, text="SUBMIT",
                           command=self.Delete_Interface_2, font='Verdana 10').grid(row=5, column=0)
        self.bttn1 = Button(self.branch, text="EXIT", command=Exit,
                            font='Verdana 10').grid(row=6, column=0)
        self.branch.mainloop()

    def Delete_Interface_2(self):
        self.branch = Tk()
        self.branch.geometry('300x200+550+200')
        self.branch.title("Management_System")
        self.x = self.entryRoll.get()
        self.x = int(self.x)
        mycursor.execute("SELECT * FROM tkdb.tktb where Roll=%s", (self.x,))
        self.dt = mycursor.fetchone()
        self.labNum1 = Label(self.branch, text="Roll No.",
                             font='Verdana 12').grid(row=1, column=0)
        self.labNum2 = Label(self.branch, text="First Name",
                             font='Verdana 12').grid(row=2, column=0)
        self.labNum3 = Label(self.branch, text="Last Name",
                             font='Verdana 12').grid(row=3, column=0)
        self.entryRoll = Entry(self.branch, width=20, font=(
            'Arial'), disabledbackground='grey')
        self.entryRoll.insert(END, self.dt[0])
        self.entryRoll.grid(row=1, column=1)
        self.entryFname = Entry(self.branch, width=20, font=('Arial'))
        self.entryFname.insert(END, self.dt[1])
        self.entryFname.grid(row=2, column=1)
        self.entryLname = Entry(self.branch, width=20, font=('Arial'))
        self.entryLname.insert(END, self.dt[2])
        self.entryLname.grid(row=3, column=1)
        self.mssglab = Label(self.branch)
        self.mssglab.grid(row=7, column=1)
        Exit = partial(self.Exit, self.branch)
        Delete_Data = partial(self.Delete_Data, self.mssglab)
        self.bttn = Button(self.branch, text="DELETE", command=Delete_Data,
                           font='Verdana 10').grid(row=5, column=1)
        self.bttn1 = Button(self.branch, text="EXIT", command=Exit,
                            font='Verdana 10').grid(row=6, column=1)
        self.branch.mainloop()

    def Delete_Data(self, label):
        mycursor.execute(delete, (self.x,))
        conn.commit()
        self.Clear_Data()
        label.config(text='Record Deleted!!!', font=('Arial', 12))

    def Exit(self, root):
        root.after(0, root.destroy())

    def Clear_Data(self):
        self.entryRoll.delete(0, END)
        self.entryFname.delete(0, END)
        self.entryLname.delete(0, END)


obj = Management_System()
obj.Interface()
