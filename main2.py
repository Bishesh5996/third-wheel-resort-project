from tkinter import *
import check_in
import check_out
import show_customer_info
import room_info
import order
import housekeeper
import bill
from PIL import Image,ImageTk
top=Tk()
top.geometry("400x400")
c=Canvas(top,bg="grey16",height=200,width=200)
a=top.resizable(2,5)
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
d=Button(top,text="GET A CODE",fg="red")
d.place(x=175,y=150)
e1=Entry(top)
e1.place(x=90,y=70)
e2=Entry(top)
e2.place(x=90, y=110)
def func():
  u=e1.get()
  p=e2.get()
  c=u+' '+p
  if u=="Manisha" and p=="1234" or u=="Bishesh" and p=="5996":
    print("Welcome to our resort")
    
    if __name__ == '__main__':
     home_ui()
    top.destroy()
  else:
    print("You are not registered to the network try again with a valid costumer id and room code")
def add():
  top=Tk()
  top.geometry("400x400")
  top.title("Sign up ".center(20))
  Thirdwheelresort= Label(top,text="Third Wheel Resort",fg="red",font="bold")
  Thirdwheelresort.place(x=110,y=20)
  username= Label(top,text ="Full Name:")
  username.place(x=10 ,y=70)
  contact=Label(top,text="Contact NO.")
  contact.place(x=12,y=110)
  password= Label(top,text="E-mail")
  password.place (x=15 ,y=150)
  gender=Label(top,text="Gender")
  gender.place(x=15,y=190)

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
  b=Button(top,text="Sign up",fg="yellow",bg="blue",command=add)
  b.place(x=120,y=250)
  n=f+' '+g+' '+h+' '+i
  f=input("Full Name")
  g=int(input("Contact")) 
  h=input("E-mail") 
  i=input("Gender")
  
  top.mainloop()
def mem():  
  top=Tk()
  top.geometry("400x400")
  top.title("Membership".center(20))
  Thirdwheelresort= Label(top,text="Third Wheel Resort",fg="red",font="bold")
  Thirdwheelresort.place(x=110,y=20)
  username= Label(top,text ="Card name")
  username.place(x=10 ,y=70)
  contact=Label(top,text="Card No.")
  contact.place(x=12,y=110)
  password= Label(top,text="CVC")
  password.place (x=15 ,y=150)
  gender=Label(top,text="Expiry Date")
  gender.place(x=15,y=190)
  membership=Label(top,text="monthly membership=$5 and yearly membership=$50",fg="black")
  membership.place(x=50,y=300)

  pay=Button(top,text="pay",fg="black",font="bold")
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
  
a=Button(top,text="login",fg="yellow",bg="red",command=func)
a.place (x=80 , y= 250)
b=Button(top,text="Sign up",fg="yellow",bg="blue",command=add)
b.place(x=120,y=250)
c=Button(top,text="Want a membership?",fg="red",command=mem)
c.place(x=80,y=280)

class Hotel:
    def ok(self, root):
        self.root = root
        pad = 3
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
            
        self.bg = PhotoImage(file = "sea.png")
        # Show image using label
        label1 = Label( root, image = self.bg)
        label1.place(x = 0, y = 0)
                
        top = Frame(self.root)
        top.pack(side="top")
        
        # display message
        self.label =Label(top,text="WELCOME TO THE ROYAL SEA RESORT",relief=RAISED,borderwidth=10,height=3,width=40,bg='BLACK',fg='orange',font='algerian 20 bold')
        self.label.grid(row=0, column=3)

        # create check in button
        self.check_in_button = Button( text="CHECK IN", font=('', 20), bg='orange',fg='black',height=2,width=30, relief=RIDGE,
                                      anchor="center",
                                      command=check_in.check_in_ui)  # call check_in_ui_fun from check_in_ui.py file
        self.check_in_button.place(x=100,y=150)

        # create check out button
        self.check_out_button = Button( text="CHECK OUT", font=('', 20), bg='orange', relief=RIDGE, height=2,
                                       width=30, fg="black", anchor="center",
                                       command=check_out.check_out_ui)  # call check_out_ui function from check_out.py file
        self.check_out_button.place(x=700,y=150)

        # create show list button
        self.room_info_button = Button(text="INFORMATION OF ROOMS", font=('', 20), bg='orange', relief=RIDGE,
                                       height=2,
                                       width=30, fg="black", anchor="center",
                                       command=room_info.room_info_ui)  # call get_info_ui function from get_info.py file
        self.room_info_button.place(x=100,y=300)

        # create get information of all the guest
        self.get_info_button = Button(text="INFORMATION OF ALL GUEST", font=('', 20), bg='orange',
                                      relief=RIDGE,
                                      height=2, width=30, fg="black", anchor="center",
                                      command=show_customer_info.customer_info)
        # call customer_info_ui function from customer_info.py file
        self.get_info_button.place(x=700,y=300)

        # button to exit the program
        self.exit_button = Button( text="EXIT", font=('', 20), bg='orange', relief=RIDGE,height=2, width=50,
                                  fg="black",
                                  anchor="center", command=quit)
        self.exit_button.place(x=250,y=450)

def home_ui():
    root = Tk()
    application = Hotel()
    root.mainloop()

if __name__ == '__main__':
    home_ui()