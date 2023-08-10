from tkinter import *
import check_in
import check_out
import show_customer_info
import room_info
import order
import housekeeper
import bill
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
top=Tk()
top.geometry("400x400")
from PIL import Image,ImageTk
c=Canvas(top,bg="grey16",height=400,width=400)
a=top.resizable(0,0)
filename=PhotoImage(file="C:\\Users\\acer\\Dropbox\\My PC (LAPTOP-DCSL3KC5)\\Desktop\\ok.png")
background_Label=Label(top,image=filename)
background_Label.place(x=0,y=0,relwidth=1,relheight=1)
c.pack()
top.title("Home Page".center(20))
Thirdwheelresort= Label(top,text="Third Wheel Resort",fg="red",font="bold")
Thirdwheelresort.place(x=110,y=20)
username= Label(top,text ="Customers ID")
username.place(x=10 ,y=70)
password= Label(top,text="Room Code")
password.place (x=15 ,y=110)
forgotpassword=Label(top,text="fogot your password?""-->")
forgotpassword.place(x=40,y=150)
e1=Entry(top)
e1.place(x=90,y=70)
e2=Entry(top)
e2.place(x=90, y=110)


def createTable():
   con=sqlite3.connect("Hotel.db")
   cur=con.cursor()
   cur.executescript('''
CREATE TABLE if not exists "user" (
	"id"	INTEGER NOT NULL,
	"fullname"	TEXT NOT NULL,
	"contactnumber"	TEXT,
	"email"	TEXT,
	"gender"	TEXT,
	"username"	TEXT NOT NULL,
	"roomid"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
                              CREATE TABLE if not exists "customers" (
	"Name"	TEXT,
	"Surname"	TEXT,
	"Address"	TEXT,
	"Number"	TEXT,
	"Room_number"	INTEGER,
	"Cost"	INTEGER,
	"Dates"	TEXT
);
                              CREATE TABLE if not exists "keepers" (
	"Keeper"	INTEGER,
	"Room_no"	TEXT
);
                              CREATE TABLE if not exists "orders" (
	"Que"	INTEGER,
	"Meal"	TEXT,
	"Drink"	TEXT,
	"Addition"	TEXT,
	"Price"	INTEGER
);

''')
   con.commit()
   con.close()

createTable()

def signupUser(fullname,contactnumber,email,gender,username,roomid):
    
    con= sqlite3.connect("Hotel.db")
    cur = con.cursor()
    cur.execute("INSERT INTO user (fullname,contactnumber,email,gender,username,roomid) VALUES(?,?,?,?,?,?)",(fullname,contactnumber,email,gender,username,roomid))
    con.commit()
    con.close()
    

def loginUser(username,roomid):   
   con= sqlite3.connect("Hotel.db")
   cur = con.cursor()
   cur.execute("SELECT * from  user WHERE username = ? AND roomid = ?",(username,roomid))
   data = cur.fetchone()
   if(data is None):
      raise Exception ("Invalid customer id or room id")
   con.commit()
   con.close()

def ok():
    window=Tk()
    window.title("Sign up".center(20))
    window.geometry("400x400")
    from PIL import Image
    z=Canvas(window,bg="black",height=400,width=400)
    a=window.resizable(0,0)
    z.pack()
    Thirdwheelresort= Label(window,text="Select a username and Room Code:",fg="red",bg="black")
    Thirdwheelresort.place(x=110,y=20)
    username= Label(window,text ="Username",fg="red",bg="black")
    username.place(x=10 ,y=70)
    contact=Label(window,text="Room Code",fg="red",bg="black")
    contact.place(x=12,y=110)
    password= Button(window,text="Finish",fg="red",bg="black")
    password.place (x=15 ,y=150)
    e1=Entry(window)
    e1.place(x=100,y=70)
    e2=Entry(window)
    e2.place(x=100,y=110)

def add():
    window=Tk()
    window.title("Sign up".center(20))
    window.geometry("400x400")
    from PIL import Image,ImageTk
    z=Canvas(window,bg="black",height=400,width=400)
    a=window.resizable(0,0)
    z.pack()
    Thirdwheelresort= Label(window,text="Third Wheel Resort",fg="red",font="bold",bg="black")
    Thirdwheelresort.place(x=110,y=20)
    fullname= Label(window,text ="Full Name:",fg="red",bg="black")
    fullname.place(x=10 ,y=70)
    contactnumber=Label(window,text="Contact NO.",fg="red",bg="black")
    contactnumber.place(x=12,y=110)
    password= Label(window,text="E-mail",fg="red",bg="black")
    password.place (x=15 ,y=150)
    gender=Label(window,text="Gender",fg="red",bg="black")
    gender.place(x=15,y=190)
    detail=Label(window,text="Please choose a username and roomid for future use :",fg="red",bg="black")
    detail.place(x=10,y=220)
    username=Label(window,text="Username",fg="red",bg="black")
    username.place(x=15,y=250)
    roomid=Label(window,text="Room id",fg="red",bg="black")
    roomid.place(x=15,y=290)
    e1=Entry(window)
    e1.place(x=90,y=70)
    e2=Entry(window)
    e2.place(x=90, y=110)
    e3=Entry(window)
    e3.place(x=90,y=150)
    e4=Entry(window)
    e4.place(x=90,y=190)
    e5=Entry(window)
    e5.place(x=90,y=250)
    e6=Entry(window)
    e6.place(x=90,y=290)
    register=Button(window,text='Register',fg='yellow',bg='red',command=lambda :signupUser(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()))
    register.place(x=100,y=320)  
    window.mainloop()
def mem():  
  top=Tk()
  top.geometry("400x400")
  n=Canvas(top,bg="black",height=400,width=400)
  a=top.resizable(0,0)
  n.pack()
  top.title("Membership".center(20))
  Thirdwheelresort= Label(top,text="Third Wheel Resort",fg="red",bg="black",font="bold")
  Thirdwheelresort.place(x=110,y=20)
  username= Label(top,text ="Card name",fg="red",bg="black")
  username.place(x=10 ,y=70)
  contact=Label(top,text="Card No.",fg="red",bg="black")
  contact.place(x=12,y=110)
  password= Label(top,text="CVC",fg="red",bg="black")
  password.place (x=15 ,y=150)
  gender=Label(top,text="Expiry Date",fg="red",bg="black")
  gender.place(x=15,y=190)
  membership=Label(top,text="monthly membership=$5 and yearly membership=$50",fg="red",bg="black")
  membership.place(x=50,y=300)
  pay=Button(top,text="pay",fg="red",bg="yellow",font="bold")
  pay.place(x=130,y=230)
  e1=Entry(top)
  e1.place(x=90,y=70)
  e2=Entry(top)
  e2.place(x=90, y=110)
  e3=Entry(top)
  e3.place(x=90,y=150)
  e4=Entry(top)
  e4.place(x=90,y=190)
  f=e1.get()
  g=e2.get()
  h=e3.get()
  i=e4.get()
  top.mainloop()

def home_ui():

    def run_out():
        root.destroy()
    

    root = Tk()
    root.title("Third Wheel Resort")
    root.geometry("950x950")
    
    top = Frame(root)
    top.pack(side="top")

    bottom = Frame(root)
    bottom.pack(side="top")

    label = Label(top, font=('arial', 50, 'bold italic'), text="----------WELCOME----------", fg="#34A2FE",
                  anchor="center")
    label.grid(row=0, column=3)

    # Check in button
    check_in_button = Button(bottom, text="CHECK IN", font=("Times", "20", "bold"), bg="#15d3ba", relief=RIDGE,
                             height=2,
                             width=45, fg="black", anchor="center", command=check_in.check_in_ui)
    check_in_button.grid(row=0, column=2, padx=10, pady=10)

    # Check out button
    check_out_button = Button(bottom, text="CHECK OUT", font=("Times", "20", "bold"), bg="#15d3ba",
                              relief=RIDGE,
                              height=2, width=45, fg="black", anchor="center", command=check_out.check_out_ui)
    check_out_button.grid(row=1, column=2, padx=10, pady=10)

    # Room info button
    get_info_button = Button(bottom, text="INFORMATION OF ALL GUESTS", font=("Times", "20", "bold"),
                             bg="#15d3ba",
                             relief=RIDGE,
                             height=2, width=45, fg="black", anchor="center", command=show_customer_info.customer_info)
    get_info_button.grid(row=2, column=2, padx=10, pady=10)

    # Guest info button
    room_info_button = Button(bottom, text="INFORMATION OF ROOMS", font=("Times", "20", "bold"), bg="#15d3ba",
                              relief=RIDGE,
                              height=2, width=45, fg="black", anchor="center", command=room_info.room_info_ui)
    room_info_button.grid(row=3, column=2, padx=10, pady=10)

    # Order sth button
    order_button = Button(bottom, text="ORDERS (FOOD / DRINK)", font=("Times", "20", "bold"), bg="#15d3ba",
                          relief=RIDGE,
                          height=2, width=45, fg="black", anchor="center", command=order.order_ui)
    order_button.grid(row=4, column=2, padx=10, pady=10)

    # Call housecleaning button
    house_cleaning_button = Button(bottom, text="CALL HOUSECLEANING", font=("Times", "20", "bold"),
                                   bg="#15d3ba",
                                   relief=RIDGE,
                                   height=2, width=45, fg="black", anchor="center", command=housekeeper.house_keeper_ui)
    house_cleaning_button.grid(row=5, column=2, padx=10, pady=10)

    # Billing button
    billing_button = Button(bottom, text="CHECK / PAY THE BILL", font=("Times", "20", "bold"), bg="#15d3ba",
                            relief=RIDGE,
                            height=2, width=45, fg="black", anchor="center", command=bill.bill_ui)
    billing_button.grid(row=6, column=2, padx=10, pady=10)

    # Exit button
    exit_button = Button(bottom, text="EXIT", font=('', 20), bg="#15d3ba",
                         relief=RIDGE,
                         height=2, width=45, fg="red", anchor="center", command=run_out)
    exit_button.grid(row=7, column=2, padx=10, pady=10)

    root.mainloop()


def func():
    u=e1.get()
    p=e2.get() 
    c=u+' '+p
    try:
      loginUser(u,p)
      
      messagebox.showinfo("Login Success","Welcome to our resort")   
      if __name__=="__main__":
       home_ui()
      top.destroy()
    except BaseException as ex:
      messagebox.showerror(title="Error",message=str(ex))   
    

      


def fpas():
    window=Tk()
    window.geometry("400x400")
    m=Canvas(window,bg="grey16",height=400,width=400)
    a=window.resizable(0,0)
    m.pack()
    window.title("Password Reset".center(20))    
    if "value"==0:
        print("Phone")
    else:
        print("E-mail")
    r1=Radiobutton(window,text="Phone",value=0,bg="grey16",fg="white")
    r1.pack(anchor=W)
    r1.place(x=10,y=120)
    r2=Radiobutton(window,text="E-mail",value=2,bg="grey16",fg="white")
    r2.pack(anchor=W)
    r2.place(x=10,y=150)  
  
    nice=Label(window,text="Third Wheel Resort",fg="white",bg="grey16",font="bold")
    nice.place(x=10,y=20)  
    info=Label(window,text="Please use a method to get a code and recover your account:",bg="grey16",fg="white")
    info.place(x=10,y=70)
    reset=Button(window,text="Reset",fg="yellow",bg="grey16",command=fpas,border=0)
    reset.place(x=10,y=240)
    window.mainloop()
a=Button(top,text="login",fg="yellow",bg="red",command=func)
a.place (x=80 , y= 250)
b=Button(top,text="Sign up",fg="yellow",bg="blue",command=add)
b.place(x=120,y=250)
c=Button(top,text="Want a membership?",fg="red",command=mem,border=0)
c.place(x=80,y=280)
d=Button(top,text="GET A CODE",fg="red",command=fpas,border=0)
d.place(x=175,y=150)
top.mainloop()





    