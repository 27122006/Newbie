import mysql.connector
from tkinter import *

class Marriage:
    def __init__(self, master):
        self.master = master
        self.master.title("Marriage Information")

        # create labels and entry widgets for capturing marriage information
        self.citizen_id_label = Label(self.master, text="Citizen ID:")
        self.citizen_id_label.grid(row=0, column=0)
        self.citizen_id_entry = Entry(self.master)
        self.citizen_id_entry.grid(row=0, column=1)

        self.spouse_id_label = Label(self.master, text="Spouse ID:")
        self.spouse_id_label.grid(row=1, column=0)
        self.spouse_id_entry = Entry(self.master)
        self.spouse_id_entry.grid(row=1, column=1)

        self.marriage_date_label = Label(self.master, text="Marriage Date:")
        self.marriage_date_label.grid(row=2, column=0)
        self.marriage_date_entry = Entry(self.master)
        self.marriage_date_entry.grid(row=2, column=1)

        # create button to save marriage information
        self.save_button = Button(self.master, text="Save", command=self.save_marriage_info)
        self.save_button.grid(row=3, column=1)

    def save_marriage_info(self):
        # get the marriage information from the entry widgets
        citizen_id = self.citizen_id_entry.get()
        spouse_id = self.spouse_id_entry.get()
        marriage_date = self.marriage_date_entry.get()

        # connect to the SQL database
        connect=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="mydata")
        my_cursor=connect.cursor()  
        my_cursor.execute("insert into marriage values(%s,%s,%s)",(citizen_id,spouse_id,marriage_date))
        connect.commit()
        connect.close()

        # clear the entry widgets
        self.citizen_id_entry.delete(0, END)
        self.spouse_id_entry.delete(0, END)
        self.marriage_date_entry.delete(0, END)

        # close the database connection
        connect.close()

