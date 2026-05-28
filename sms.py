con = None                # declaring globally
mycursor = None


def addstudent():
        def submitadd():
                global con,mycursor


                #Check if database if connected first of all
                if con is None or mycursor is None:
                        messagebox.showerror('Connection Error','Please connect to databse first!')

                #first of all get all the values from the entry boxes
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
                        strr = 'insert into studentdata1 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        mycursor.execute(strr,(id,name,mobile,email,gender,address,dob,addedtime,addeddate))
                        con.commit()

                        res = messagebox.askyesnocancel('Notifications','ID {} NAME {} Added Succesfully, Do you want to clear the form...'.format(id,name),parent=addroot)
                        if(res==TRUE):
                                idval.set('')
                                nameval.set('')
                                mobileval.set('')
                                emailval.set('')
                                genderval.set('')
                                addressval.set('')
                                dobval.set('')


                except pymysql.err.IntegrityError:
                        messagebox.showerror('Error','This ID already exists!', parent=addroot)

                except Exception as e:
                        messagebox.showerror('Database Error', f'Something went wrong:\n{e}', parent=addroot)
                
                strr = 'select * from studentdata1'
                mycursor.execute(strr)
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                        studenttable.insert('',END,values=vv)
                        

        addroot = Toplevel(master=DataEntryFrame)
        addroot.grab_set() # clicks out of frame will not work
        addroot.geometry('470x470+220+200')
        addroot.title('Add Entries')
        addroot.iconbitmap('plus.ico')
        addroot.config(bg='grey') 
        addroot.resizable(False,False)

        #---------Add Labels for Adding Enteries
        idlabel = Label(addroot,text='Enter ID : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        idlabel.place(x=10,y=10)

        namelabel = Label(addroot,text='Enter Name : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        namelabel.place(x=10,y=70)

        moblabel = Label(addroot,text='Enter Mobile : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        moblabel.place(x=10,y=130)

        emaillabel = Label(addroot,text='Enter Email : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        emaillabel.place(x=10,y=190)

        addressgenderlabel = Label(addroot,text='Enter Address : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        addressgenderlabel.place(x=10,y=250)

        genderlabel = Label(addroot,text='Enter Gender : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        genderlabel.place(x=10,y=310)

        doblabel = Label(addroot,text='Enter D.O.B : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        doblabel.place(x=10,y=370)

        #-------- Entry boxes for Add labels
        idval = StringVar()
        nameval = StringVar()
        mobileval = StringVar()
        emailval = StringVar()
        genderval = StringVar()
        addressval = StringVar()
        dobval = StringVar()

        identry = Entry(addroot,font=('Arial',15,'bold'),bd=5,textvariable=idval)
        identry.place(x=235,y=10)

        nameentry = Entry(addroot,font=('Arial',15,'bold'),bd=5,textvariable=nameval)
        nameentry.place(x=235,y=70)

        mobileentry = Entry(addroot,font=('Arial',15,'bold'),bd=5,textvariable=mobileval)
        mobileentry.place(x=235,y=130)

        emailentry = Entry(addroot,font=('Arial',15,'bold'),bd=5,textvariable=emailval)
        emailentry.place(x=235,y=190)

        addressentry = Entry(addroot,font=('Arial',15,'bold'),bd=5,textvariable=addressval)
        addressentry.place(x=235,y=250)

        genderentry = Entry(addroot,font=('Arial',15,'bold'),bd=5,textvariable=genderval)
        genderentry.place(x=235,y=310)

        dobentry = Entry(addroot,font=('Arial',15,'bold'),bd=5,textvariable=dobval)
        dobentry.place(x=235,y=370)

        #--- Submit button for Entries submit
        submitbtn = Button(addroot,text='SUBMIT',font=('Arial',15,'bold'),bg='light green',width=10,bd=5,activebackground='dark green',activeforeground='green',command=submitadd)
        submitbtn.place(x=310,y=418)

def searchstudent():
        def search():

                global con,mycursor

                if con is None or mycursor is None:
                        messagebox.showerror('Connection Error','Please connect to databse first!')
                        return

                id = idval.get()
                name = nameval.get()
                mobile = mobileval.get()
                email = emailval.get()
                gender = genderval.get()
                address = addressval.get()
                dob = dobval.get()
                addeddate = time.strftime("%d/%m/%y")

                if(id != ''):       # if id is not empty
                        strr = 'select * from studentdata1 where id = %s'       # search using id 
                        mycursor.execute(strr,(id))
                        datas = mycursor.fetchall()
                        studenttable.delete(*studenttable.get_children())
                        for i in datas:
                                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                                studenttable.insert('',END,values=vv)

                elif(name != ''):       # if name is not empty
                        strr = 'select * from studentdata1 where name = %s'       # search using name 
                        mycursor.execute(strr,(name))
                        datas = mycursor.fetchall()
                        studenttable.delete(*studenttable.get_children())
                        for i in datas:
                                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                                studenttable.insert('',END,values=vv)

                elif(mobile != ''):       # if mobile is not empty
                        strr = 'select * from studentdata1 where mobile = %s'       # search using mobile 
                        mycursor.execute(strr,(mobile))
                        datas = mycursor.fetchall()
                        studenttable.delete(*studenttable.get_children())
                        for i in datas:
                                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                                studenttable.insert('',END,values=vv)



                elif(email != ''):       # if email is not empty
                        strr = 'select * from studentdata1 where email = %s'       # search using Email 
                        mycursor.execute(strr,(email))
                        datas = mycursor.fetchall()
                        studenttable.delete(*studenttable.get_children())
                        for i in datas:
                                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                                studenttable.insert('',END,values=vv)

                elif(address != ''):       # if address field is not empty
                        strr = 'select * from studentdata1 where address = %s'       # search using address 
                        mycursor.execute(strr,(address))
                        datas = mycursor.fetchall()
                        studenttable.delete(*studenttable.get_children())
                        for i in datas:
                                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                                studenttable.insert('',END,values=vv)    

                elif(gender != ''):       # if gender field is not empty
                        strr = 'select * from studentdata1 where gender = %s'       # search using Gender 
                        mycursor.execute(strr,(gender))
                        datas = mycursor.fetchall()
                        studenttable.delete(*studenttable.get_children())
                        for i in datas:
                                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                                studenttable.insert('',END,values=vv)


                elif(dob != ''):       # if dob field is not empty
                        strr = 'select * from studentdata1 where dob = %s'       # search using dob 
                        mycursor.execute(strr,(dob))
                        datas = mycursor.fetchall()
                        studenttable.delete(*studenttable.get_children())
                        for i in datas:
                                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                                studenttable.insert('',END,values=vv) 
                


                elif(addeddate != ''):       # if added_date is not empty
                        strr = 'select * from studentdata1 where addeddate = %s'       # search using added_Date 
                        mycursor.execute(strr,(addeddate))
                        datas = mycursor.fetchall()
                        studenttable.delete(*studenttable.get_children())
                        for i in datas:
                                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                                studenttable.insert('',END,values=vv)            



        searchroot = Toplevel(master=DataEntryFrame)
        searchroot.grab_set() # clicks out of frame will not work
        searchroot.geometry('470x540+220+200')
        searchroot.title('Search Entries')
        searchroot.iconbitmap('search.ico')
        searchroot.config(bg='grey') 
        searchroot.resizable(False,False)

        #---------Add Labels for Adding Enteries
        idlabel = Label(searchroot,text='Enter ID : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        idlabel.place(x=10,y=10)

        namelabel = Label(searchroot,text='Enter Name : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        namelabel.place(x=10,y=70)

        moblabel = Label(searchroot,text='Enter Mobile : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        moblabel.place(x=10,y=130)

        emaillabel = Label(searchroot,text='Enter Email : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        emaillabel.place(x=10,y=190)

        addressgenderlabel = Label(searchroot,text='Enter Address : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        addressgenderlabel.place(x=10,y=250)

        genderlabel = Label(searchroot,text='Enter Gender : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        genderlabel.place(x=10,y=310)

        doblabel = Label(searchroot,text='Enter D.O.B : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        doblabel.place(x=10,y=370)

        datelabel = Label(searchroot,text='Enter Date : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        datelabel.place(x=10,y=430)

        #-------- Entry boxes for Add labels
        idval = StringVar()
        nameval = StringVar()
        mobileval = StringVar()
        emailval = StringVar()
        genderval = StringVar()
        addressval = StringVar()
        dobval = StringVar()
        dateval = StringVar()

        identry = Entry(searchroot,font=('Arial',15,'bold'),bd=5,textvariable=idval)
        identry.place(x=235,y=10)

        nameentry = Entry(searchroot,font=('Arial',15,'bold'),bd=5,textvariable=nameval)
        nameentry.place(x=235,y=70)

        mobileentry = Entry(searchroot,font=('Arial',15,'bold'),bd=5,textvariable=mobileval)
        mobileentry.place(x=235,y=130)

        emailentry = Entry(searchroot,font=('Arial',15,'bold'),bd=5,textvariable=emailval)
        emailentry.place(x=235,y=190)

        addressentry = Entry(searchroot,font=('Arial',15,'bold'),bd=5,textvariable=addressval)
        addressentry.place(x=235,y=250)

        genderentry = Entry(searchroot,font=('Arial',15,'bold'),bd=5,textvariable=genderval)
        genderentry.place(x=235,y=310)

        dobentry = Entry(searchroot,font=('Arial',15,'bold'),bd=5,textvariable=dobval)
        dobentry.place(x=235,y=370)

        dateentry = Entry(searchroot,font=('Arial',15,'bold'),bd=5,textvariable=dateval)
        dateentry.place(x=235,y=430)

        #--- Submit button for Entries submit
        submitbtn = Button(searchroot,text='SUBMIT',font=('Arial',15,'bold'),bg='light green',width=10,bd=5,activebackground='dark green',activeforeground='green',command=search)
        submitbtn.place(x=310,y=480)


def deletestudent():
        cc = studenttable.focus()          # tells place (ROW) where u clicked to detele 
        content = studenttable.item(cc)     # Recover Data from that place 
        pp = content['values'][0]
        strr = 'delete from studentdata1 where id = %s'
        mycursor.execute(strr,(pp))
        con.commit()
        messagebox.showinfo('Alert','ID {} deleted Sucessfully'.format(pp))
        strr = 'select * from studentdata1'        
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)


def updatestudent():
        def update():
                id = idval.get()
                name = nameval.get()
                mobile = mobileval.get()
                email = emailval.get()
                gender = genderval.get()
                address = addressval.get()
                dob = dobval.get()
                date = dateval.get()
                time = timeval.get()

                strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,gender=%s,address=%s,dob=%s,date=%s,time=%s where id=%s'
                mycursor.execute(strr,(name,mobile,email,gender,address,dob,date,time,id))
                con.commit()
                messagebox.showinfo("Success",'ID {} modified Sucessfully...'.format(id),parent=updateroot)
                strr = 'select * from studentdata1'        
                mycursor.execute(strr)
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                        studenttable.insert('',END,values=vv)



                


        updateroot = Toplevel(master=DataEntryFrame)
        updateroot.grab_set() # clicks out of frame will not work
        updateroot.geometry('470x585+220+160')
        updateroot.title('Search Entries')
        updateroot.iconbitmap('update.ico')
        updateroot.config(bg='grey') 
        updateroot.resizable(False,False)

        #---------Add Labels for Adding Enteries
        idlabel = Label(updateroot,text='Enter ID : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        idlabel.place(x=10,y=10)

        namelabel = Label(updateroot,text='Enter Name : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        namelabel.place(x=10,y=70)

        moblabel = Label(updateroot,text='Enter Mobile : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        moblabel.place(x=10,y=130)

        emaillabel = Label(updateroot,text='Enter Email : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        emaillabel.place(x=10,y=190)

        genderlabel = Label(updateroot,text='Enter Gender : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        genderlabel.place(x=10,y=250)

        addresslabel = Label(updateroot,text='Enter Address : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        addresslabel.place(x=10,y=310)

        doblabel = Label(updateroot,text='Enter D.O.B : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        doblabel.place(x=10,y=370)

        datelabel = Label(updateroot,text='Enter Date : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        datelabel.place(x=10,y=430)

        timelabel = Label(updateroot,text='Enter Time : ',bg='gold2',font=('Arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor=W)
        timelabel.place(x=10,y=490)

        #-------- Entry boxes for Add labels
        idval = StringVar()
        nameval = StringVar()
        mobileval = StringVar()
        emailval = StringVar()
        genderval = StringVar()
        addressval = StringVar()
        dobval = StringVar()
        dateval = StringVar()
        timeval = StringVar()

        identry = Entry(updateroot,font=('Arial',15,'bold'),bd=5,textvariable=idval)
        identry.place(x=235,y=10)

        nameentry = Entry(updateroot,font=('Arial',15,'bold'),bd=5,textvariable=nameval)
        nameentry.place(x=235,y=70)

        mobileentry = Entry(updateroot,font=('Arial',15,'bold'),bd=5,textvariable=mobileval)
        mobileentry.place(x=235,y=130)

        emailentry = Entry(updateroot,font=('Arial',15,'bold'),bd=5,textvariable=emailval)
        emailentry.place(x=235,y=190)

        addressentry = Entry(updateroot,font=('Arial',15,'bold'),bd=5,textvariable=addressval)
        addressentry.place(x=235,y=250)

        genderentry = Entry(updateroot,font=('Arial',15,'bold'),bd=5,textvariable=genderval)
        genderentry.place(x=235,y=310)

        dobentry = Entry(updateroot,font=('Arial',15,'bold'),bd=5,textvariable=dobval)
        dobentry.place(x=235,y=370)

        dateentry = Entry(updateroot,font=('Arial',15,'bold'),bd=5,textvariable=dateval)
        dateentry.place(x=235,y=430)

        timeentry = Entry(updateroot,font=('Arial',15,'bold'),bd=5,textvariable=dateval)
        timeentry.place(x=235,y=490)

        #--- Submit button for Entries submit
        submitbtn = Button(updateroot,text='SUBMIT',font=('Arial',15,'bold'),bg='light green',width=10,bd=5,activebackground='dark green',activeforeground='green',command=update)
        submitbtn.place(x=315,y=530)

        cc = studenttable.focus()
        content = studenttable.item(cc)
        pp = content['values']
        if(len(pp) != 0):
                idval.set(pp[0])    # All values must be set into the entry boxes for updation
                nameval.set(pp[1])
                mobileval.set(pp[2])
                emailval.set(pp[3])
                addressval.set(pp[4])
                genderval.set(pp[5])
                dobval.set(pp[6])
                dateval.set(pp[7])
                timeval.set(pp[8])
                


def showstudent():
        strr = 'select * from studentdata1'        
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)

def exportstudent():

        
        if con is None or mycursor is None:
                messagebox.showerror('Connection Error','Please connect to database first!')
                return

        ff = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV File","*.csv")])

        if ff == "":
                return

        gg = studenttable.get_children()

        id,name,mobile,email,gender,address,dob,addeddate,addedtime = [],[],[],[],[],[],[],[],[]

        for i in gg:
                content = studenttable.item(i)
                pp = content['values']
                id.append(pp[0])
                name.append(pp[1])
                mobile.append(pp[2])
                email.append(pp[3])
                gender.append(pp[4])
                address.append(pp[5])
                dob.append(pp[6])
                addeddate.append(pp[7])
                addedtime.append(pp[8])

        dd = ['ID','Name','Mobile','Email','gender','address','DOB','Added Date','Added Time']

        df = pandas.DataFrame(
        list(zip(id,name,mobile,email,gender,address,dob,addeddate,addedtime)),
        columns=dd
    )

        df.to_csv(ff + ".csv", index=False)

        messagebox.showinfo('Confirmation','Student Data Saved Successfully!')

    


def exitstudent():
        res = messagebox.askyesno('Notification','Do you want to Exit ?') # small popup window
        if(res==True):
                root.destroy()



####################### Connect to Database function
def connectdb():

        def submitdb():
                global con,mycursor
                host = hostval.get()     # first we will get the values from form
                user = userval.get()
                password = passwordval.get() 
                try:
                        con = pymysql.connect(host=host,user=user,password=password) 
                        mycursor = con.cursor()
                except:
                        messagebox.showerror('Error','Login credentials Incorrect please try again')
                        return
                
                try:
                        strr = 'create database if not exists studentmanagementsystem1'
                        mycursor.execute(strr)
                        strr = 'use studentmanagementsystem1'
                        mycursor.execute(strr)
                        strr = '''create table if not exists studentdata1(
        id int primary key not null,
        name varchar(20),
        mobile varchar(12),
        email varchar(30),
        address varchar(100),
        gender varchar(50),
        dob varchar(50),
        date varchar(50),
        time varchar(50)
    )'''
                        mycursor.execute(strr)
                        con.commit()
                        messagebox.showinfo('SUCCESS','Database Connected Success',parent=dbroot)
                
                except Exception as e:
                        print("Error:", e)

                

        dbroot = Toplevel()
        dbroot.grab_set()    # will hold it 
        dbroot.iconbitmap('db.ico')
        dbroot.resizable(False,False)
        dbroot.config(bg='blue')
        dbroot.geometry("470x250+800+230")
        dbroot.title("Connect to Database")
        
        #  ----Connect DB Labels
        hostlabel = Label(dbroot,text='Enter Host : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
        hostlabel.place(x=10,y=10)

        userlabel = Label(dbroot,text='Enter User : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
        userlabel.place(x=10,y=70)

        passlabel = Label(dbroot,text='Enter Password : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
        passlabel.place(x=10,y=130)

        #  ----Entery Boxes
        hostval = StringVar()  # to store entered text
        userval = StringVar()  
        passwordval = StringVar()  


        hostentery = Entry(dbroot,font=('Arial',15,'bold'),bd=5, textvariable=hostval)
        hostentery.place(x=235,y=10)

        userentery = Entry(dbroot,font=('Arial',15,'bold'),bd=5, textvariable=userval)
        userentery.place(x=235,y=70)

        passwordentery = Entry(dbroot,font=('Arial',15,'bold'),bd=5, textvariable=passwordval)
        passwordentery.place(x=235,y=130)


        #--------- Buutton to Submit and connect to Db

        submitbutton = Button(dbroot,text='SUBMIT',font=('Arial',15,'bold'),width=10,bg='gold',activebackground='gold',activeforeground='green',command=submitdb)
        submitbutton.place(x=161,y=190)


# Function to show LIVE Date and Time 
def tick():
        time_string = time.strftime("%H:%M:%S")
        date_string = time.strftime("%d:%m:%Y")
       # print(time_string,date_string)
        clock.config(text=" Date = "+date_string+"\nTime = "+time_string)
        clock.after(100,tick)


################################ TEXT SLIDING function

def IntroLabelTick():
    global ss
    
    ss = ss[1:] + ss[0]   # rotate text
    SliderLabel.config(text=ss)
    
    root.after(100, IntroLabelTick)
                            


#############################################
from tkinter import *
import time
from tkinter import Toplevel , messagebox,filedialog  # Toplevel is a popup window , window for exit,
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql                    # You first need to install it from TERMINAL
import pandas


root = Tk()

root.title("Student Management System")
root.config(bg="gold2")
root.geometry('1174x700+200+50')
root.iconbitmap('icon.ico')
root.resizable(False,False)


#############Frame for Manipulation containing buttons 

DataEntryFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

#----- Frame Intro

toplabel = Label(DataEntryFrame,text='--------------Operations-------------',width=30,font=('Arial',22,'bold'),bg='gold2')
toplabel.pack(side=TOP,expand=TRUE)

addbtn = Button(DataEntryFrame,text='ADD',width=25,font=('Arial',20,'bold'),bd=6,bg='light blue',activebackground='green',relief=RIDGE,activeforeground='gold2',command=addstudent)
addbtn.pack(side=TOP,expand=TRUE)

searchbtn = Button(DataEntryFrame,text='SEARCH',width=25,font=('Arial',20,'bold'),bd=6,bg='light blue',activebackground='green',relief=RIDGE,activeforeground='gold2',command=searchstudent)
searchbtn.pack(side=TOP,expand=TRUE)

deletebtn = Button(DataEntryFrame,text='DELETE',width=25,font=('Arial',20,'bold'),bd=6,bg='light blue',activebackground='green',relief=RIDGE,activeforeground='gold2',command=deletestudent)
deletebtn.pack(side=TOP,expand=TRUE)

updatebtn = Button(DataEntryFrame,text='UPDATE',width=25,font=('Arial',20,'bold'),bd=6,bg='light blue',activebackground='green',relief=RIDGE,activeforeground='gold2',command=updatestudent)
updatebtn.pack(side=TOP,expand=TRUE)

showbtn = Button(DataEntryFrame,text='SHOW ALL',width=25,font=('Arial',20,'bold'),bd=6,bg='light blue',activebackground='green',relief=RIDGE,activeforeground='gold2',command=showstudent)
showbtn.pack(side=TOP,expand=TRUE)

exportbtn = Button(DataEntryFrame,text='EXPORT DATA',width=25,font=('Arial',20,'bold'),bd=6,bg='light blue',activebackground='green',relief=RIDGE,activeforeground='gold2',command=exportstudent)
exportbtn.pack(side=TOP,expand=TRUE)

exitbtn = Button(DataEntryFrame,text='EXIT',width=25,font=('Arial',20,'bold'),bd=6,bg='red',activebackground='green',relief=RIDGE,activeforeground='gold2',command=exitstudent)
exitbtn.pack(side=TOP,expand=TRUE)
 
############## Frame for Data Showing 

ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)


#------------------ SHOW DATABASE DATA 
style = ttk.Style()
style.configure('Treeview.Heading',font=('Arial',20,'bold'),foreground='blue')
style.configure('Treeview',font=('Times New Roman',17,'bold'),foreground='black',background='white',rowheight=35)



scroll_x= Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y= Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('ID','NAME','MOBILE','EMAIL','GENDER','ADDRESS','D.O.B','ADDED TIME','ADDED DATE'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('ID',text='ID')
studenttable.heading('NAME',text='NAME')
studenttable.heading('MOBILE',text='MOBILE')
studenttable.heading('EMAIL',text='EMAIL')
studenttable.heading('ADDRESS',text='ADDRESS')
studenttable.heading('GENDER',text='GENDER')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('ADDED DATE',text='ADDED DATE')
studenttable.heading('ADDED TIME',text='ADDED TIME')
studenttable['show']='headings'
studenttable.column('ID',width=100)
studenttable.column('NAME',width=500)
studenttable.column('MOBILE',width=300)
studenttable.column('EMAIL',width=500)
studenttable.column('ADDRESS',width=1000)
studenttable.column('GENDER',width=180)
studenttable.column('D.O.B',width=160)
studenttable.column('ADDED DATE',width=230)
studenttable.column('ADDED TIME',width=230)





studenttable.pack(fill=BOTH,expand=1)

##################### Slider
ss = "Welcome to SMS                                            "   # add spaces for smooth loop
SliderLabel = Label(root, text=ss, font=('Arial',30,'bold'),relief=RIDGE, border=5, width=19, bg='gold')
SliderLabel.place(x=370, y=0)
IntroLabelTick()

############# CLOCK
clock = Label(root,text=ss,font=('times',14),relief=RIDGE,border=5,width=15,bg='light green')
clock.place(x=10,y=10)
tick()

################ Connect to Database 
connectbutton = Button(root,text="Connect Database",width=23,font=('times',15),relief=RIDGE,border=5,bg='sky blue',activebackground='pink',activeforeground='white',command=connectdb)
connectbutton.place(x=895,y=10)




root.mainloop()