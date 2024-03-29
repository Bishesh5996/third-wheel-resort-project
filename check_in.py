from tkinter import *
import sqlite3
from tkinter import messagebox
from datetime import date
import datetime
from PIL import Image,ImageTk

def check_in_ui():
    root = Tk()
    root.title("THIRD WHEEL RESORT CHECK IN")
    root.geometry("500x500")
    

    # Destroy the window
    def close_it():
        root.destroy()

    # Create submit function for databases
    def submit():
        
        if not f_name.get() or not l_name.get() or not address.get() or not number.get() or not room_number.get():
            messagebox.showwarning("Warning", "Please fill all the information")
            root.destroy()
            return

        if room_number.get() == '101' or room_number.get() == '102' or room_number.get() == '103' or room_number.get() == '201' or room_number.get() == '202' or room_number.get() == '203' \
                or room_number.get() == '301' or room_number.get() == '302' or room_number.get() == '303' or room_number.get() == '401' or room_number.get() == '402' or room_number.get() == '403':
            # Create a db or connect to one
            conn = sqlite3.connect("Hotel.db")

            # Create a cursor
            c = conn.cursor()
            # Query the database
            c.execute("SELECT Room_number FROM customers")
            room_taken = c.fetchall()
            is_room_empty = 0
            for room in room_taken:
                if str(room_number.get()) == str(room[0]):
                    is_room_empty = 1
                    continue
            if is_room_empty == 0:
                if str(room_number.get()) == '101' or str(room_number.get()) == '102' or str(
                        room_number.get()) == '103':
                    cost = 50
                elif str(room_number.get()) == '201' or str(room_number.get()) == '202' or str(
                        room_number.get()) == '203':
                    cost = 75
                elif str(room_number.get()) == '301' or str(room_number.get()) == '302' or str(
                        room_number.get()) == '303':
                    cost = 75
                elif str(room_number.get()) == '401' or str(room_number.get()) == '402' or str(
                        room_number.get()) == '403':
                    cost = 150
                else:
                    cost = 0

                today = date.today()
                last_day = datetime.date.today() + datetime.timedelta(days=int(day_count.get()))

                dates = ''
                dates += str(today) + '---' + str(last_day)

                print(today)
                print(last_day)

                # Insert into table
                c.execute("INSERT INTO customers VALUES (:f_name, :l_name, :address, :number, :room_number, :cost, :days)",
                          {
                              'f_name': f_name.get(),
                              'l_name': l_name.get(),
                              'address': address.get(),
                              'number': number.get(),
                              'room_number': room_number.get(),
                              'cost': cost* int(day_count.get()),
                              'days': dates
                          })

                # Commit change
                conn.commit()

                # close connection
                conn.close()

                # Clear the text boxes
                f_name.delete(0, END)
                l_name.delete(0, END)
                address.delete(0, END)
                number.delete(0, END)
                room_number.delete(0, END)
                day_count.delete(0, END)

                messagebox.showinfo("information", "Check in done successfully")
                root.destroy()
            else:
                messagebox.showerror("Warning", "room is not empty")
                # Clear the text boxes
                f_name.delete(0, END)
                l_name.delete(0, END)
                address.delete(0, END)
                number.delete(0, END)
                room_number.delete(0, END)
                day_count.delete(0, END)
        else:
            messagebox.showerror("Warning", "You've entered the wrong room number")
            # Clear the text boxes
            f_name.delete(0, END)
            l_name.delete(0, END)
            address.delete(0, END)
            number.delete(0, END)
            room_number.delete(0, END)
            day_count.delete(0, END)
            root.destroy()
    
   
   


    # Create tet boxes
    f_name = Entry(root, width=40,)
    f_name.grid(row=0, column=1, padx=10)
    l_name = Entry(root, width=40,)
    l_name.grid(row=1, column=1)
    address = Entry(root, width=40)
    address.grid(row=2, column=1)
    number = Entry(root, width=40)
    number.grid(row=3, column=1)
    room_number = Entry(root, width=40)
    room_number.grid(row=4, column=1)
    day_count = Entry(root, width=40)
    day_count.grid(row=5, column=1)

    # Create Box labels
    f_name_label = Label(root, text="First Name",fg="red",)
    f_name_label.grid(row=0, column=0)
    l_name_label = Label(root, text="Last Name",fg="red",)
    l_name_label.grid(row=1, column=0)
    address_label = Label(root, text="Address",fg="red")
    address_label.grid(row=2, column=0)
    number_label = Label(root, text="Phone No",fg="red")
    number_label.grid(row=3, column=0)
    room_number_label = Label(root, text="Room No",fg="red")
    room_number_label.grid(row=4, column=0)
    day_count_label = Label(root, text="How many Days",fg="red")
    day_count_label.grid(row=5, column=0)

    # Create a submit button
    submit_btn = Button(root, text="Add record to Database", command=submit,bg="blue")
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Exit button
    exit_button = Button(root, text="EXIT", font=('', 10), bg="#15d3ba",
                         relief=RIDGE,
                         height=1, width=15, fg="red", anchor="center", command=close_it)
    exit_button.grid(row=7, column=1, padx=10, pady=10)
    
    
    root.mainloop()


if __name__ == '__main__':
   check_in_ui()