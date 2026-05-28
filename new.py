from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import time
import sqlite3
import pandas

# ---------------- DATABASE ----------------
con = sqlite3.connect("student.db")
mycursor = con.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS studentdata1(
id INTEGER PRIMARY KEY,
name TEXT,
mobile TEXT,
email TEXT,
gender TEXT,
address TEXT,
dob TEXT,
date TEXT,
time TEXT
)
""")

con.commit()


# ---------------- ADD STUDENT ----------------
def addstudent():

    def submitadd():

        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        gender = genderval.get()
        address = addressval.get()
        dob = dobval.get()

        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%y")

        try:
            mycursor.execute(
                "INSERT INTO studentdata1 VALUES (?,?,?,?,?,?,?,?,?)",
                (id, name, mobile, email, gender, address, dob, addeddate, addedtime)
            )
            con.commit()

            messagebox.showinfo("Success", "Student Added Successfully")

            showstudent()

        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "ID already exists")

    addroot = Toplevel()
    addroot.geometry('470x470')
    addroot.title('Add Student')

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    genderval = StringVar()
    addressval = StringVar()
    dobval = StringVar()

    Label(addroot, text="ID").pack()
    Entry(addroot, textvariable=idval).pack()

    Label(addroot, text="Name").pack()
    Entry(addroot, textvariable=nameval).pack()

    Label(addroot, text="Mobile").pack()
    Entry(addroot, textvariable=mobileval).pack()

    Label(addroot, text="Email").pack()
    Entry(addroot, textvariable=emailval).pack()

    Label(addroot, text="Gender").pack()
    Entry(addroot, textvariable=genderval).pack()

    Label(addroot, text="Address").pack()
    Entry(addroot, textvariable=addressval).pack()

    Label(addroot, text="DOB").pack()
    Entry(addroot, textvariable=dobval).pack()

    Button(addroot, text="Submit", command=submitadd).pack(pady=10)


# ---------------- SHOW STUDENT ----------------
def showstudent():

    mycursor.execute("SELECT * FROM studentdata1")
    datas = mycursor.fetchall()

    studenttable.delete(*studenttable.get_children())

    for i in datas:
        studenttable.insert('', END, values=i)


# ---------------- DELETE ----------------
def deletestudent():

    selected = studenttable.focus()
    content = studenttable.item(selected)
    row = content['values']

    if not row:
        return

    mycursor.execute("DELETE FROM studentdata1 WHERE id=?", (row[0],))
    con.commit()

    showstudent()


# ---------------- UPDATE ----------------
def updatestudent():

    selected = studenttable.focus()
    content = studenttable.item(selected)
    row = content['values']

    if not row:
        return

    def update():

        mycursor.execute("""
        UPDATE studentdata1
        SET name=?,mobile=?,email=?,gender=?,address=?,dob=?,date=?,time=?
        WHERE id=?
        """, (
            nameval.get(),
            mobileval.get(),
            emailval.get(),
            genderval.get(),
            addressval.get(),
            dobval.get(),
            dateval.get(),
            timeval.get(),
            idval.get()
        ))

        con.commit()
        showstudent()

    updateroot = Toplevel()
    updateroot.geometry("450x500")

    idval = StringVar(value=row[0])
    nameval = StringVar(value=row[1])
    mobileval = StringVar(value=row[2])
    emailval = StringVar(value=row[3])
    genderval = StringVar(value=row[4])
    addressval = StringVar(value=row[5])
    dobval = StringVar(value=row[6])
    dateval = StringVar(value=row[7])
    timeval = StringVar(value=row[8])

    Label(updateroot, text="ID").pack()
    Entry(updateroot, textvariable=idval).pack()

    Label(updateroot, text="Name").pack()
    Entry(updateroot, textvariable=nameval).pack()

    Label(updateroot, text="Mobile").pack()
    Entry(updateroot, textvariable=mobileval).pack()

    Label(updateroot, text="Email").pack()
    Entry(updateroot, textvariable=emailval).pack()

    Label(updateroot, text="Gender").pack()
    Entry(updateroot, textvariable=genderval).pack()

    Label(updateroot, text="Address").pack()
    Entry(updateroot, textvariable=addressval).pack()

    Label(updateroot, text="DOB").pack()
    Entry(updateroot, textvariable=dobval).pack()

    Label(updateroot, text="Date").pack()
    Entry(updateroot, textvariable=dateval).pack()

    Label(updateroot, text="Time").pack()
    Entry(updateroot, textvariable=timeval).pack()

    Button(updateroot, text="Update", command=update).pack(pady=10)


# ---------------- EXPORT CSV ----------------
def exportstudent():

    ff = filedialog.asksaveasfilename(defaultextension=".csv")

    if ff == "":
        return

    mycursor.execute("SELECT * FROM studentdata1")
    rows = mycursor.fetchall()

    df = pandas.DataFrame(rows,
        columns=['ID','Name','Mobile','Email','Gender','Address','DOB','Added Date','Added Time'])

    df.to_csv(ff, index=False)

    messagebox.showinfo("Success", "Data Exported")


# ---------------- EXIT ----------------
def exitstudent():

    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()


# ---------------- MAIN WINDOW ----------------
root = Tk()

root.title("Student Management System")
root.geometry("1100x650")


# BUTTON FRAME
DataEntryFrame = Frame(root)
DataEntryFrame.pack(side=LEFT, fill=Y)

Button(DataEntryFrame, text="ADD", width=20, command=addstudent).pack(pady=10)
Button(DataEntryFrame, text="DELETE", width=20, command=deletestudent).pack(pady=10)
Button(DataEntryFrame, text="UPDATE", width=20, command=updatestudent).pack(pady=10)
Button(DataEntryFrame, text="SHOW", width=20, command=showstudent).pack(pady=10)
Button(DataEntryFrame, text="EXPORT", width=20, command=exportstudent).pack(pady=10)
Button(DataEntryFrame, text="EXIT", width=20, command=exitstudent).pack(pady=10)


# TABLE FRAME
ShowDataFrame = Frame(root)
ShowDataFrame.pack(side=RIGHT, fill=BOTH, expand=True)

scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)

studenttable = Treeview(
    ShowDataFrame,
    columns=('ID','NAME','MOBILE','EMAIL','GENDER','ADDRESS','DOB','DATE','TIME'),
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set
)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

for col in ('ID','NAME','MOBILE','EMAIL','GENDER','ADDRESS','DOB','DATE','TIME'):
    studenttable.heading(col, text=col)

studenttable['show'] = 'headings'

studenttable.pack(fill=BOTH, expand=1)


showstudent()

root.mainloop()