from tkinter import *
from tkinter.font import Font
from PIL import Image,ImageTk
from tkinter import Tk, ttk, StringVar, NORMAL, DISABLED, IntVar, messagebox
from random import randint
import time
#from mysql.connector import connection
   
global var7

def acno ():
    z=open('acc_no.txt','r+')
    r=z.readlines()
    acc=int(r[0])+1
    z.close()
    t=open('acc_no.txt','w')
    t.write(str(acc))
    t.close()
    return acc

name,f_name,deposit,prof,sex,age=' ' ,' ' ,0,' ',' ',0

#acc
def new():
    import tkinter as am
#    s=Tk()
   
    Frame_1= Toplevel(a)
#    Frame_1 = Frame(w)
#    Frame_1.grid()
    Frame_1.configure(background="SlateBlue4")
    Frame_1.minsize(500,500)
    Frame_1.maxsize(500,500)
    
    #icon
    img = PhotoImage(file='train.png')
    a.call('wm', 'iconphoto', Frame_1._w, img)
    
    #variable
    global name,f_name,deposit,prof,sex,age
    n1,n2,n3,n4,n5,n6=am.StringVar(),am.StringVar(),am.IntVar(),am.StringVar(),am.StringVar(),am.IntVar()
    
    #------empty label----------
    Label(Frame_1, text='CREATE NEW ACCOUNT', font=("EngraversGothic BT", 30 ),bg="SlateBlue4",fg="white").place(x=50,y=10)

    #----label for name------
    Label(Frame_1, text="your name ", font=("EngraversGothic BT", 21 ),bg="SlateBlue4",fg="white").place(x=180,y=60)
    #------empty label----------
    Label(Frame_1,bg="SlateBlue4",fg="white").place(x=50,y=70)

    #---label for father name-----
    Label(Frame_1, text="father's name ", font=("EngraversGothic BT", 21),bg="SlateBlue4",fg="white").place(x=157,y=124)

    #------empty label----------
    Label(Frame_1,bg="SlateBlue4",fg="white").place(x=50,y=130)

    #---label for cnic-----
    Label(Frame_1, text="enter opening balance ", font=("EngraversGothic BT",21),bg="SlateBlue4",fg="white").place(x=101,y=188)
    #------empty label----------
    Label(Frame_1,bg="SlateBlue4",fg="white").place(x=101,y=193)

    #-----label for username------
    Label(Frame_1, text="profession ", font=("EngraversGothic BT",21),bg="SlateBlue4",fg="white").place(x=175,y=249)

    #------empty label----------
    Label(Frame_1,bg="SlateBlue4",fg="white").place(x=150,y=230)

    #-----label for account type------
    Label(Frame_1, text="sex(m/f)",font=("EngraversGothic BT",21),bg="SlateBlue4",fg="white").place(x=190,y=306)
    Label(Frame_1, text="age ", font=("EngraversGothic BT",21),bg="SlateBlue4",fg="white").place(x=214,y=361)
   
    #-----entries for name-----
#    logging.debug('creating entries....')
    name= Entry(Frame_1,bg="white",textvariable=n1, width=20, font="none 12")
    name.place(x=147,y=98)
    
    f_name = Entry(Frame_1, bg="white",textvariable=n2, width=20, font="none 12")
    f_name.place(x=150,y=162)
    deposit= Entry(Frame_1, bg="white",textvariable=n3, width=20, font="none 12")
    deposit.place(x=150,y=225)

    prof = Entry(Frame_1,bg="white",textvariable=n4, width=20, font="12")
    prof.place(x=150,y=285)

    #-----entry for username-----
    sex=Entry(Frame_1, bg="white",textvariable=n5, width=20, font="none 12")
    sex.place(x=150,y=341)
    age=Entry(Frame_1, bg="white",textvariable=n6, width=20, font="none 12")
    age.place(x=150,y=395)

    #------empty label----------
    Label(Frame_1,bg="SlateBlue4",fg="white").place(x=420,y=450)
    Label(Frame_1,bg="SlateBlue4",fg="white").place(x=420,y=450)

    #----button for next-----
    next_bt = Button(Frame_1, text="NEXT", bg="white",activebackground="SlateBlue4",activeforeground="white", fg="SlateBlue4", font=("EngraversGothic BT",12), padx=15,pady=7, bd=2, command=click)
    next_bt.place(x=250,y=440)

    #----button for exit-----
    exit_bt = Button(Frame_1, text="EXIT",command=Frame_1.destroy,activebackground="SlateBlue4",activeforeground="white", bg='white', fg='SlateBlue4', font=("EngraversGothic BT",12), padx=16,pady=7, bd=2)
    exit_bt.place(x=160,y=440)

    #------empty label----------
    Label(Frame_1,bg="SlateBlue4",fg="white").grid(row=15, sticky=EW)

def click(event=None):
    global name,f_name,deposit,prof,sex,age
    a,b,c,d,e,f=str(name.get()),str(f_name.get()),int(deposit.get()),str(prof.get()),str(sex.get()),str(age.get())
    from mysql.connector import connection
    cnx = connection.MySQLConnection(user='root',password='amit3464',
                                     host='localhost',database='amit')
    Cursor = cnx.cursor()
    Qry = ("INSERT INTO accounting "\
           "VALUES (%s, %s,%s, %s,%s,%s,%s)")
    data = (acno(),a,b,e,f,d,c)
    Cursor.execute(Qry,data)
    # Make sure data is committed to the database
    cnx.commit()
    Cursor.close()
    cnx.close()
  
'''
#Account
from mysql.connector import connection
cnx=connection.MySQLConnection(user='root',password='amit3464',host='localhost',database='amit')
cur=cnx.cursor()

sql = """create table accounting(
                  customer_account_no integer(13) primary key,
                  customer_name varchar(50),
                  c_f_name varchar(50),
                  sex varchar(1),
                  age integer(2),
                  profession varchar(50),
                  balance integer)"""
cur.execute(sql)
cnx.close()
'''

def Book():

    #---------------------window_1-----------------------------------

    w1 = Toplevel(a)
    w1.geometry("700x500+0+0")
    w1.title("TICKET KIOSK")
    w1.configure(background="SlateBlue4")

    #------------------------variables-------------------------------

    #global_variables
    global From_Destination
    global To_Destination
    global Ticket_Qty
    global Total
    global Ticket_Price
    #defining
    var0 = StringVar()
    var1 = StringVar()
    var2 = StringVar()
    
    #icon
    img = PhotoImage(file='train.png')
    a.call('wm', 'iconphoto', w1._w, img)

    
    From_Destination = StringVar()
    To_Destination = StringVar()
    Ticket_Qty = StringVar()
    Total = StringVar()
    Ticket_Price = StringVar()
    #setting
    var0.set("")
    var1.set("")
    var2.set("")
    Ticket_Qty.set("")
    From_Destination.set("")
    To_Destination.set("")
    Total.set("")
    Ticket_Price.set("")

    #------------------------functions()-----------------------------

    def Are_you_sure() :
        m1 = "\n\n"+"-"*57+"\n"+" "*32+"ULTI METRO\n"+"\nDestination : "+To_Destination.get()+"\nTransaction Mode : Online"+"\n\nUnit_Price"+" "*22+"Qty"+" "*10+"Price\n"+"-"*57+"\n"+Ticket_Price.get()+" "*31+Ticket_Qty.get()+" "*12+Total.get()
        m2 = messagebox.askyesno("Confirmation","These are the details of your ticket"+m1)
        if m2 == True :
            w1.destroy()
            Payment()
        else :
             messagebox.showinfo("Canceled","Proceeding back to Ticket Kiosk")
    def Tic_chk():
        Ticket_Qty.set(var2.get())
        return int(var2.get())

    def Destination_chk():
        if var1.get() == 'Alambagh' :
            To_Destination.set("Alambagh")
            return 13
        elif var1.get() == 'Krishnagar' :
            To_Destination.set("Krishnagar")
            return 18
        elif var1.get() == 'Aishbagh' :
            To_Destination.set("Aishbagh")
            return 23
        elif var1.get() == 'Transport Nagar' :
            To_Destination.set("Transport Nagar")
            return 30
        elif var1.get() == 'Amausi Airport' :
            To_Destination.set("Amausi Airport")
            return 34

    def Confirm():
        if var1.get() == "" :
            messagebox.showerror("Error code : RFC2616","Destination not selected!")
            return
        elif var2.get() == "" :
            messagebox.showerror("Error code : RFC2617","Number of tickets cannot be empty!")
            return
        elif var2.get() == "0" :
            messagebox.showerror("Error code : RFC26170","Number of tickets cannot be zero!")
            return
        elif var2.get().isalpha()  :
            messagebox.showerror("Error code : RFC2617A","Please enter Integer values!")
            return
        else :
            From_Destination.set("Charbagh")
            c1 = Destination_chk()
            c2 = Tic_chk()
            per_km = 2.13
            tcost = per_km*c1
            ftcost = c2*tcost
            Ticket_Price.set(str('%6.2f'%(tcost)))
            Total.set(str('%6.2f'%(ftcost)))
            Are_you_sure()

    #------------------------widgets:Destination---------------------

    l1 = Label(w1,font=("EngraversGothic BT",35,"bold"),text="Select Destination",bg="SlateBlue4",fg="white",justify="center",bd=10)
    l1.grid(row = 0,column = 2,columnspan = 3)

    l2 = Label(w1,font=("EngraversGothic BT",29),anchor ="w",text="Starting from :",bd=10,bg="SlateBlue4",fg="white")
    l2.grid(row = 2,column = 2)
    cb2 = ttk.Combobox(w1,textvariable=var0,state="readonly",font=("EngraversGothic BT",17),width=15)
    cb2['value']=('Charbagh')
    cb2.current(0)
    cb2.grid(row = 2,column = 3)

    l3 = Label(w1,font=("EngraversGothic BT",29),anchor ="w",text="Going to :",bd=10,bg="SlateBlue4",fg="white")
    l3.grid(row = 4,column = 2)
    cb3 = ttk.Combobox(w1,textvariable=var1,state="readonly",font=("EngraversGothic BT",17,"bold"),width=15)
    cb3['value']=('','Alambagh','Krishnagar','Aishbagh','Transport Nagar','Amausi Airport')
    cb3.current(0)
    cb3.grid(row = 4,column = 3)

    ti=Label(w1,font=("EngraversGothic BT",29),anchor ="w",text="Tickets :",bd=10,bg="SlateBlue4",fg="white",justify="center")
    ti.grid(row = 6,column = 2,columnspan = 2)
    ent1 = Entry(w1,font=("EngraversGothic BT",15),textvariable=var2,bd=2,width=3,justify="right")
    ent1.grid(row = 6,column = 3)

    btnConfirm = Button(w1,padx=2,pady=2,command=Confirm,bd=2,fg="black",text="Confirm",font=("EngraversGothic BT",17,"bold"),width=8,height=1,justify="center")
    btnConfirm.grid(row=8,column=2,columnspan = 2)

    #------------------------Area correction------------------

    ac1 = Label(w1,font=("ariel",10,"bold"),anchor="w",text="       ",bg="SlateBlue4")
    ac1.grid(row = 1,column = 0,sticky = W)
    ac2 = Label(w1,font=("ariel",10,"bold"),anchor="w",text="       ",bg="SlateBlue4")
    ac2.grid(row = 2,column = 1,sticky = W)
    ac3 = Label(w1,font=("ariel",10,"bold"),anchor="w",text="       ",bg="SlateBlue4")
    ac3.grid(row = 3,column = 0,sticky = W)
    ac4 = Label(w1,font=("ariel",10,"bold"),anchor="w",text="       ",bg="SlateBlue4")
    ac4.grid(row = 4,column = 1,sticky = W)
    ac5 = Label(w1,font=("ariel",10,"bold"),anchor="w",text="       ",bg="SlateBlue4")
    ac5.grid(row = 5,column = 0,sticky = W)
    ac6 = Label(w1,font=("ariel",10,"bold"),anchor="w",text="       ",bg="SlateBlue4")
    ac6.grid(row = 7,column = 0,sticky = W)

    #------------------------Mainloop-------------------------

    w1.mainloop()

    #------------------------End------------------------------
    
def Payment():

    #---------------------window_2-----------------------------------

    w2 = Toplevel(a)
    w2.geometry("800x500+0+0")
    w2.title("TICKET KIOSK")
    w2.configure(background="SlateBlue4")

    img = PhotoImage(file='train.png')
    a.call('wm', 'iconphoto', w2._w, img)

    #------------------------variables-----------------------

    #global_variables
    global From_Destination
    global To_Destination
    global Ticket_Qty
    global Total
    global Ticket_Price
    #defining
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    #setting
    var3.set("0")
    var4.set("0")
    var5.set("")
    var6.set("")

    #------------------------functions()-----------------------------

    def chkbtn_value_chk2():
        if var3.get() == "1":
            var4.set("0")
            var5.set("")
            var6.set("")
            ent5e.configure(state = DISABLED)
            ent6e.configure(state = DISABLED)
        elif var3.get() == "0":
            var5.set("")
            var6.set("")
            ent5e.configure(state = NORMAL)
            ent6e.configure(state = NORMAL)

    def chkbtn_value_chk3():
        if var4.get() == "1":
            var3.set("0")
            var5.set("")
            var6.set("")
            ent5e.configure(state = NORMAL)
            ent6e.configure(state = NORMAL)
        elif var4.get() == "0":
            var5.set("")
            var6.set("")
            ent5e.configure(state = DISABLED)
            ent6e.configure(state = DISABLED)

    def Confirm_Booking():
        if var3.get() == "0" and var4.get() == "0":
            messagebox.showerror("Error code : RFC1617E","You have not selected your Payment method!")
        else:
            ask1 = messagebox.askyesno("Are you sure?","Proceed to book ticket?")
            if ask1 == True:
                if var3.get() == "1":
                    ask2 = messagebox.askyesno("Are you sure?","Proceeding to Payment")
                    if ask2 == True:
                        messagebox.showinfo("Payment in Progress","Please put the required bills in the cash slot")
                        messagebox.showinfo("Payment Completed","Payment Successful")
                        w2.destroy()
                        Main_Menu()
                    else:
                        messagebox.showinfo("Payment Canceled","Proceeding back to booking page")
                elif var4.get() == "1":
                    if var5.get() == "":
                        messagebox.showerror("Error code : 700E57","You have not entered your Account no!")
                    elif var6.get() == "":
                        messagebox.showerror("Error code : 701E83","You have not entered your Password!")
                    elif var5.get().isalpha() == True:
                        messagebox.showerror("Error code : 705A26","Please enter your Account no in integers!")
                    elif var6.get().isalpha() == True:
                        messagebox.showerror("Error code : 709A14","Please enter your Password in integers!")
                    elif len(str(var5.get())) >= 10 :
                        messagebox.showerror("Error code : 702L39","Your Account No is way too long!")
                    elif len(str(var5.get())) <= 10 :
                        messagebox.showerror("Error code : 702L31","Your Account No is way too short!")
                    else:
                        if len(str(var6.get())) >= 10 :
                            messagebox.showerror("Error code : 703L39","Your Password is way top long!")
                        if len(str(var6.get())) <= 10 :
                            messagebox.showerror("Error code : 703L31","Your Password is way to0 short!")
                        else:
                            ask2 = messagebox.askyesno("Are you sure?","Proceeding to Payment")
                            if ask2 == True:
                                messagebox.showinfo("Payment in Progress","Processing Payment Request")
                                if my.is_connected == False:
                                    messagebox.showerror("Connection Error!","Error in connection to the server \n Please try again later")
                                else:
                                    query1  = "select Passwd from test2 where Account_no = {}".format(var5.get())
                                    cur.execute(query1)
                                    d1 = cur.fetchall()
                                    if d1 == []:
                                        messagebox.showerror("Error code : 404","Error! Account not found")
                                    else :
                                        if var14.get() == d1[0][0]:
                                            query2 = "select Balance from test2 where Account_no = {}".format(var5.get())
                                            cur.execute(query2)
                                            d2 = cur.fetchall()
                                            if d2[0][-1] <= float(Total.get()):
                                                messagebox.showerror("Error code : 34A2","Insuficent Balance")
                                            else :
                                                b1 = d2[0][0]
                                                b1 = b1 - float(Total.get())
                                                query3 = "update test2 set Balance = {} where Account_no = {}".format(b1,var6.get())
                                                cur.execute(query3)
                                                my.commit()
                                                my.close()
                                                messagebox.showinfo("Payment Completed","Payment Successful")
                                                w2.destroy()
                                                Main_Menu()
                                        else:
                                            messagebox.showerror("Error code : 90A3","Error! Password does not match")
                            else:
                                messagebox.showinfo("Payment Canceled","Proceeding back to booking page")
            else :
                return

    #------------------------bottomleft2:widgets:Payment-------------------------

    l1 = Label(w2,font=("EngraversGothic BT",38,"bold"),text="Payment Method",bd=10,justify="center",bg="SlateBlue4",fg="white")
    l1.grid(row = 0,column = 0,columnspan = 5)

    shk2 = Checkbutton(w2,bd=10,command=chkbtn_value_chk2,variable=var3,onvalue="1",offvalue="0",bg="SlateBlue4",fg="black")
    shk2.grid(row = 2,column = 1)
    l2 = Label(w2,font=("EngraversGothic BT",29),text="Cash",bd=10,bg="SlateBlue4",fg="white")
    l2.grid(row = 2,column = 2)

    shk3 = Checkbutton(w2,bd=10,command=chkbtn_value_chk3,variable=var4,onvalue="1",offvalue="0",bg="SlateBlue4",fg="black")
    shk3.grid(row = 2,column = 4)
    l3 = Label(w2,font=("EngraversGothic BT",29),text="E-Pay",bd=10,bg="SlateBlue4",fg="white")
    l3.grid(row = 2,column = 5)

    ent5l = Label(w2,font=("EngraversGothic BT",32),justify="left",text="Account No :",bd=16,bg="SlateBlue4",fg="white")
    ent5l.grid(row = 4,column = 0,columnspan = 1)
    ent5e = Entry(w2,font=("EngraversGothic BT",27),textvariable=var5,width=21,bg="white",justify="right",insertwidth=4,bd=6)
    ent5e.grid(row = 4,column = 1,columnspan = 5)

    ent6l = Label(w2,font=("EngraversGothic BT",32),justify="left",text="Password :",bd=16,bg="SlateBlue4",fg="white")
    ent6l.grid(row = 6,column = 0,columnspan = 1)
    ent6e = Entry(w2,font=("EngraversGothic BT",27),textvariable=var6,width=21,bg="white",justify="right",insertwidth=4,bd=6)
    ent6e.grid(row = 6,column = 1,columnspan = 5)

    btnConfirm = Button(w2,padx=2,pady=2,command=Confirm_Booking,bd=2,fg="black",text="Confirm",font=("EngraversGothic BT",17,"bold"),width=8,height=1,justify="center")
    btnConfirm.grid(row=8,column=2,columnspan = 2)

    #------------------------Area correction------------------
    
    ac1 = Label(w2,font=("ariel",10,"bold"),anchor="w",text="       ",bg="SlateBlue4")
    ac1.grid(row = 1,column = 0,sticky = W)
    ac2 = Label(w2,font=("ariel",10,"bold"),anchor="w",text="       ",bg="SlateBlue4")
    ac2.grid(row = 3,column = 0,sticky = W)
    ac3 = Label(w2,font=("ariel",10,"bold"),anchor="w",text="       ",bg="SlateBlue4")
    ac3.grid(row = 5,column = 0,sticky = W)
    ac4 = Label(w2,font=("ariel",10,"bold"),anchor="w",text="       ",bg="SlateBlue4")
    ac4.grid(row = 7,column = 0,sticky = W)

    #------------------------Mainloop-------------------------

    w2.mainloop()

#menu
def menu():
    r=Toplevel(a)
    #Geometry
    r.minsize(500,500)
    r.maxsize(500,500)
    r.configure(background="SlateBlue4")    
    #Font
    f1=Font(family="EngraversGothic BT",size= 16)
    f2=Font(family="EngraversGothic BT",size= 42)
    f3=Font(family="Simplifica",size=12)
    r.title("TICKET KIOSK")
    
    #Label
    l1=Label(r,text="ULTIMETRO", fg="white",font=f2,bg="SlateBlue4")
    l2=Label(r,text="Design/Code  © RAN Corp",font=f3,bg="SlateBlue4",fg="white")
    
    #Buttons
    b1=Button(r, text="MAP",padx=60,pady=39,bg="white",fg="SlateBlue4",activebackground="SlateBlue4",activeforeground="white",font=f1,command=mapp)
    b2=Button(r, text="BOOK",padx=54,pady=39,bg="white",fg="SlateBlue4",command=Book,activebackground="SlateBlue4",activeforeground="white",font=f1)
    b3=Button(r, text="ACCOUNT",padx=37,pady=39,bg="white",fg="SlateBlue4",activebackground="SlateBlue4",activeforeground="white",command=new,font=f1)
    b4=Button(r, text="CONTACT US",padx=24,pady=39, command=cont,fg="SlateBlue4",bg="white",activebackground="SlateBlue4",activeforeground="white",font=f1)
    b5=Button(r, text="QUIT", bg="white",fg="SlateBlue4",activebackground="SlateBlue4",activeforeground="white",command = r.destroy,font=f1)
    
    img = PhotoImage(file='train.png')
    a.call('wm', 'iconphoto', r._w, img)
    
    #Packing
    l1.place(x=120,y=20)
    l2.place(x=200,y=478)
    b1.place(x=60,y=110)
    b2.place(x=285,y=110)
    b3.place(x=60,y=250)
    b4.place(x=285,y=250)
    b5.place(x=231,y=390)

#map    
def mapp():
    w=Toplevel(a)
    #Geometry
    w.minsize(610,360)
    w.maxsize(610,360)
    
    img = PhotoImage(file='train.png')
    a.call('wm', 'iconphoto', w._w, img)
    
    w.title("TICKET KIOSK")
    #Photo
    photo=PhotoImage(file="img.gif")
    labe = Button(w,image=photo,command=w.destroy).pack()
    labe.image
    
#def book():
    

#def acc():


#Contact
def cont():
    c=Toplevel(a)
    #Geometry
    c.minsize(500,250)
    c.maxsize(500,250)
    c.configure(background="SlateBlue4")
    
    #Font
    f1=Font(family="EngraversGothic BT",size= 18,weight="bold")
    f2=Font(family="EngraversGothic BT",size= 14)
    f3=Font(family="EngraversGothic BT",size= 30,weight="bold")
    #Label
    l1=Label(c, text="To Contact Us",font=f3,bg="SlateBlue4",fg="white").pack()
    l2=Label(c, text="toll free number: 1800-1696-1696",fg="white",bg="SlateBlue4",font=f1).pack()
    l3=Label(c, text="write to us at: ranmetro@gmail.com",bg="SlateBlue4",fg="white",font=f1).pack()
    
    
    img = PhotoImage(file='train.png')
    a.call('wm', 'iconphoto', c._w, img)
    
    #Button
    b=Button(c, text="Return",activebackground="SlateBlue4",activeforeground="white", command= c.destroy, bg="white",fg="SlateBlue4",padx=15,pady=7,font=f2).place(x=197,y=140)

#__main__

a=Tk()

#title
a.title("TICKET KIOSK")

#icon
img = PhotoImage(file='train.png')
a.call('wm', 'iconphoto', a._w, img)

#Geometry
a.minsize(500,500)
a.maxsize(500,500)

#Photo
phto=PhotoImage(file="mm.gif")
b = Button(a,image=phto,command=menu).pack()

a.mainloop()