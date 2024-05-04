from tkinter import *
import sqlite3
from PIL import ImageTk, Image
import numpy as np
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

root = Tk()
root.title("Bunnisher's Aviation Marketing")

cap_image = ImageTk.PhotoImage(Image.open("1st.jpg"))
cap_image_label = Label(image=cap_image)
cap_image_label.grid(row=0, column=1)


def submit():

    conn = sqlite3.connect('aviation_marketing.db')

    c = conn.cursor()

    c.execute("INSERT INTO marketing VALUES (:dates, :aircraft, :location, :emailcount, :status, :customer, :customerphone, :customeremail)",

              {

                  'dates': dates.get(),

                  'aircraft': aircraft.get(),

                  'location': location.get(),

                  'emailcount': emailcount.get(),

                  'status': status.get(),

                  'customer': customer.get(),

                  'customerphone': customerphone.get(),

                  'customeremail': customeremail.get(),

              })

    conn.commit()

    conn.close()

    # Clear the Text Boxes

    dates.delete(0, END)
    aircraft.delete(0, END)
    location.delete(0, END)
    emailcount.delete(0, END)
    status.delete(0, END)
    customer.delete(0, END)
    customerphone.delete(0, END)
    customeremail.delete(0, END)


def query():
    top = Toplevel()
    top.title("Aviation Marketing")
    topLabel = Label(top, text="Aviation Marketing")
    topLabel.grid(row=1, column=0)
    
    cap_image = ImageTk.PhotoImage(Image.open("1st.jpg"))
    cap_image_label = Label(image=cap_image)
    cap_image_label.grid(row=0, column=1)
    

    conn = sqlite3.connect('aviation_marketing.db')

    c = conn.cursor()
    c.execute("SELECT *, oid FROM marketing")
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(top, text=print_records)
    query_label.grid(row=14, column=0, columnspan=2)

    csv_button = Button(top, text="Save to Excel", command=lambda: write_to_csv(records))
    csv_button.grid(row=1, column=3, pady=10)

    conn.commit()

    conn.close()

#Write to CSV Excel
def write_to_csv(records):
    with open('Aviation_Marketing1.csv', 'w', newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in records:
            w.writerow(record)

#update a record

def update():
    top_update = Toplevel()
    top_update.title("Update Marketing")
    top_update_label = Label(top_update, text="Update Marketing")
    top_update_label.grid(row=1, column=0)

    cap_image2 = ImageTk.PhotoImage(Image.open("1st.jpg"))
    cap_image2_label = Label(image=cap_image2)
    cap_image2_label.grid(row=0, column=1)

    conn = sqlite3.connect('aviation_marketing.db')

    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("SELECT * FROM marketing WHERE oid = " + record_id)
    records = c.fetchall()

    global dates_top_update
    global aircraft_top_update
    global location_top_update
    global emailcount_top_update
    global status_top_update
    global customer_top_update
    global customerphone_top_update
    global customeremail_top_update




    dates_top_update = Entry(top_update, width=30)
    dates_top_update.grid(row=2, column=1, padx=20, pady=(10, 0))
    aircraft_top_update = Entry(top_update, width=30)
    aircraft_top_update.grid(row=3, column=1)
    location_top_update = Entry(top_update, width=30)
    location_top_update.grid(row=4, column=1)
    emailcount_top_update = Entry(top_update, width=30)
    emailcount_top_update.grid(row=5, column=1)
    status_top_update = Entry(top_update, width=30)
    status_top_update.grid(row=6, column=1)
    customer_top_update = Entry(top_update, width=30)
    customer_top_update.grid(row=7, column=1)
    customerphone_top_update = Entry(top_update, width=30)
    customerphone_top_update.grid(row=8, column=1)
    customeremail_top_update = Entry(top_update, width=30)
    customeremail_top_update.grid(row=9, column=1)

    dates_label_top_update = Label(top_update, text="Date:")
    dates_label_top_update.grid(row=2, column=0, pady=(10, 0))
    aircraft_label_top_update = Label(top_update, text="Aircraft:")
    aircraft_label_top_update.grid(row=3, column=0)
    location_label_top_update = Label(top_update, text="Location:")
    location_label_top_update.grid(row=4, column=0)
    emailcount_label_top_update = Label(top_update, text="Email Count:")
    emailcount_label_top_update.grid(row=5, column=0)
    status_label_top_update = Label(top_update, text="Status:")
    status_label_top_update.grid(row=6, column=0)
    customer_label_top_update = Label(top_update, text="Customer:")
    customer_label_top_update.grid(row=7, column=0)
    customerphone_label_top_update = Label(top_update, text="Customer Phone:")
    customerphone_label_top_update.grid(row=8, column=0)
    customeremail_label_top_update = Label(top_update, text="Customer Email:")
    customeremail_label_top_update.grid(row=9, column=0)


    for record in records:
        dates_top_update.insert(0, record[0])
        aircraft_top_update.insert(0, record[1])
        location_top_update.insert(0, record[2])
        emailcount_top_update.insert(0, record[3])
        status_top_update.insert(0, record[4])
        customer_top_update.insert(0, record[5])
        customerphone_top_update.insert(0, record[6])
        customeremail_top_update.insert(0, record[7])

    save_btn = Button(top_update, text="Save", command=save)
    save_btn.grid(row=10, column=1, pady=10)



    conn.commit()

    conn.close()

def save():
    conn = sqlite3.connect('aviation_marketing.db')

    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE marketing SET
        dates = :dates, 
        aircraft = :aircraft,
        location = :location,
        emailcount = :emailcount,
        status = :status,
        customer = :customer,
        customerphone = :customerphone,
        customeremail = :customeremail

        WHERE oid = :oid""",
              {'dates': dates_top_update.get(),
               'aircraft': aircraft_top_update.get(),
               'location': location_top_update.get(),
               'emailcount': emailcount_top_update.get(),
               'status': status_top_update.get(),
               'customer': customer_top_update.get(),
               'customerphone': customerphone_top_update.get(),
               'customeremail': customeremail_top_update.get(),
               'oid': record_id
               })

    conn.commit()

    conn.close()







#Delete a record

def delete():

    conn = sqlite3.connect('aviation_marketing.db')

    c = conn.cursor()

    c.execute("DELETE from marketing WHERE oid= " + delete_box.get())

    delete_box.delete(0, END)

    conn.commit()

    conn.close()

# Entries

dates = Entry(root, width=30)
dates.grid(row=2, column=1, padx=20, pady=(10,0))
aircraft = Entry(root, width=30)
aircraft.grid(row=3, column=1)
location = Entry(root, width=30)
location.grid(row=4, column=1)
emailcount = Entry(root, width=30)
emailcount.grid(row=5, column=1)
status = Entry(root, width=30)
status.grid(row=6, column=1)
customer = Entry(root, width=30)
customer.grid(row=7, column=1)
customerphone = Entry(root, width=30)
customerphone.grid(row=8, column=1)
customeremail = Entry(root, width=30)
customeremail.grid(row=9, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1)

# Labels



dates_label = Label(root, text="Dates:")
dates_label.grid(row=2, column=0, pady=(10,0))
aircraft_label = Label(root, text="Aircraft:")
aircraft_label.grid(row=3, column=0)
location_label = Label(root, text="Location:")
location_label.grid(row=4, column=0)
emailcount_label = Label(root, text="Email Count:")
emailcount_label.grid(row=5, column=0)
status_label = Label(root, text="Status:")
status_label.grid(row=6, column=0)
customer_label = Label(root, text="Customer:")
customer_label.grid(row=7, column=0)
customerphone_label = Label(root, text="Customer Phone:")
customerphone_label.grid(row=8, column=0, pady=5)
customeremail_label = Label(root, text="Customer Email:")
customeremail_label.grid(row=9, column=0, pady=5)
delete_box_label = Label(root, text="Delete Record:")
delete_box_label.grid(row=10, column=0, pady=5)


submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=11, column=1, pady=10)
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=12, column=0, pady=10)
select_btn = Button(root, text="Select Record", command=update)
select_btn.grid(row=12, column=1, pady=10)
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=12, column=2, pady=10)
button4 = Button(root, text="Shut er Down", command=root.destroy)
button4.grid(row=15, column=1, pady=10)

root.mainloop()
