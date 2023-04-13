from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Information:
    def __init__(self, root):
        self.root=root
        self.root.title("Information")
        self.root.geometry("1295x550+230+220")

        #textvariable
        self.citizen_ref=StringVar()
        self.citizen_name=StringVar()
        self.citizen_ID=StringVar()
        self.citizen_DOB=StringVar()
        self.address=StringVar()
        
        #title
        lbl_title=Label(self.root,text="Information",font=("times new roman",18,"bold"),bg="white",fg="green")
        lbl_title.place(x=0,y=0,width=1295,height=50)
        

        #label frame
        
        lableframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Citizen details",font=("times new roman",12,"bold"),padx=2)
        
        lableframeleft.place(x=5,y=50,width=425,height=490)
        ## labels and entry
        #citizen ref
        lbl_citizen_ref=Label(lableframeleft,text="Citizen ref",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_ref.grid(row=0,column=0,padx=10,pady=5,sticky="w")

        txt_citizen_ref=Entry(lableframeleft,font=("times new roman",12,"bold"),textvariable=self.citizen_ref,bg="lightyellow")

        txt_citizen_ref.grid(row=0,column=1,padx=10,pady=5,sticky="w")

         #citizen name
        lbl_citizen_name=Label(lableframeleft,text="Citizen Name",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_name.grid(row=1,column=0,padx=10,pady=5,sticky="w")

        txt_citizen_name=Entry(lableframeleft,font=("times new roman",12,"bold"),textvariable=self.citizen_name,bg="lightyellow")

        txt_citizen_name.grid(row=1,column=1,padx=10,pady=5,sticky="w")
        
        #citizen ID
        lbl_citizen_ID=Label(lableframeleft,text="Citizen ID",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_ID.grid(row=2,column=0,padx=10,pady=5,sticky="w")

        txt_citizen_ID=Entry(lableframeleft,font=("times new roman",12,"bold"),textvariable=self.citizen_ID,bg="lightyellow")

        txt_citizen_ID.grid(row=2,column=1,padx=10,pady=5,sticky="w")
        
        #citizen DOB
        lbl_citizen_DOB=Label(lableframeleft,text="DOB",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_DOB.grid(row=3,column=0,padx=10,pady=5,sticky="w")

        txt_citizen_DOB=Entry(lableframeleft,font=("times new roman",12,"bold"),textvariable=self.citizen_DOB,bg="lightyellow")

        txt_citizen_DOB.grid(row=3,column=1,padx=10,pady=5,sticky="w")
        #citizen gender with combobox
        lbl_citizen_gender=Label(lableframeleft,text="Gender",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_gender.grid(row=4,column=0,padx=10,pady=5,sticky="w")

        combo_gender=ttk.Combobox(lableframeleft,font=("arial",12,"bold"),state="readonly")
        combo_gender["value"]=("Male","Female","Other") 
        combo_gender.current(0)
        self.gender=combo_gender.get()
        def update_gender(event):
            self.gender=combo_gender.get()
        combo_gender.bind("<<ComboboxSelected>>",update_gender)
        
        
        combo_gender.grid(row=4,column=1,padx=10,pady=5,sticky="w")
        
        #citizen Footer
        combo_nationality=Label(lableframeleft,text="Nationality",font=("times new roman",12,"bold"),bg="white")
        countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda","Viet Nam" ]

        # create the combobox
        combo_nationality = ttk.Combobox(lableframeleft, font=("arial",12,"bold"), state="readonly")
        combo_nationality["values"] = countries
        combo_nationality.grid(row=6, column=1, padx=10, pady=5)
        combo_nationality.current(0)
        self.nationality=combo_nationality.get()
        def update_nationality(event=""):
            self.nationality = combo_nationality.get()
        combo_nationality.bind("<<ComboboxSelected>>",update_nationality)
        combo_nationality.grid(row=6,column=1,padx=10,pady=5,sticky="w")
        ## citizen marriage status with combobox
        lbl_citizen_marriage=Label(lableframeleft,text="Marriage Status",font=("times new roman",12,"bold"),bg="white")
        lbl_citizen_marriage.grid(row=7,column=0,padx=10,pady=5,sticky="w")

        combo_marriage=ttk.Combobox(lableframeleft,font=("arial",12,"bold"),state="readonly")
        combo_marriage["value"]=("Married","Unmarried","Divorced",)
        combo_marriage.current(0)
        self.marriage_status=combo_marriage.get()

        def update_marriage(event=""):
            self.marriage_status = combo_marriage.get()
        combo_marriage.bind("<<ComboboxSelected>>",update_marriage)
        combo_marriage.grid(row=7,column=1,padx=10,pady=5,sticky="w")
        
        
       


        ## button frame
        btn_frame=Frame(lableframeleft,bd=2,relief=RIDGE,)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        #add button
        btn_add=Button(btn_frame,text="Add",font=("arial",11,"bold"),bg="black",command=self.add_data,fg="yellow",width=10)
        btn_add.grid(row=0,column=0)
        #update button  
        btn_update=Button(btn_frame,text="Update",font=("arial",11,"bold"),bg="black",command=self.update_data,fg="yellow",width=10)
        btn_update.grid(row=0,column=1)
        #delete button
        btn_delete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",command=self.delete_data,fg="yellow",width=10)

        btn_delete.grid(row=0,column=2)
        #clear button
        btn_clear=Button(btn_frame,text="Clear",font=("arial",11,"bold"),bg="black",command=self.clear,fg="yellow",width=10)
        btn_clear.grid(row=0,column=3)
        
        ##            Table SEARCH FRAME
        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Citizen Information Details",font=("arial",12,"bold"),fg="gold",bg="white",padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)
       
        lblSearch=Label(Table_Frame,text="Search By",font=("arial",12,"bold"),bg="white",fg="black")
        lblSearch.grid(row=0,column=0,padx=2,sticky="w")
        
        combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),state="readonly",width=10)
        combo_Search["value"]=["Citizen ref","Citizen ID","Citizen Name"]
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1)

        self.search_by=combo_Search.get()
        def update_search(event=""):
            self.search_by = combo_Search.get()
        combo_Search.bind("<<ComboboxSelected>>",update_search)
        
        txt_Search=Entry(Table_Frame,font=("arial",13,"bold"),bg="lightyellow",bd=5,relief=GROOVE,width=25)
        txt_Search.grid(row=0,column=2,padx=2)
        
        btn_Search=Button(Table_Frame,text="Search By",font=("arial",11,"bold"),command=self.search_data,bg="black",fg="yellow",width=10)
        btn_Search.grid(row=0,column=3,padx=1)
        
        
        btn_ShowAll=Button(Table_Frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="yellow",width=10)
        btn_ShowAll.grid(row=0,column=4,padx=1)
        


        

       
        
        
       
        ## data table
        
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=850,height=410)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        

        self.information_table=ttk.Treeview(details_table,column=("Ref","Name","ID","DOB","Gender","Address","Nationality","Marriage"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.information_table.xview)
        scroll_y.config(command=self.information_table.yview)

        self.information_table.heading("Ref",text="Ref")
        self.information_table.heading("Name",text="Name")
        self.information_table.heading("ID",text="ID")
        self.information_table.heading("DOB",text="DOB")
        self.information_table.heading("Gender",text="Gender")
        self.information_table.heading("Address",text="Address")
        self.information_table.heading("Nationality",text="nation")
        self.information_table.heading("Marriage",text="Marriage")
        
        self.information_table["show"]="headings"
        
    
        self.information_table.column("Ref",width=100)
        
        self.information_table.column("Name",width=100)
        self.information_table.column("ID",width=100)
        self.information_table.column("DOB",width=100)
        self.information_table.column("Gender",width=100)
        self.information_table.column("Address",width=100)
        self.information_table.column("Nationality",width=100)
        self.information_table.column("Marriage",width=100)


        self.information_table.pack(fill=BOTH,expand=1)
        
        self.information_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
            

    
    def fetch_data(self):
        connect=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="mydata")
        my_cursor=connect.cursor()
        my_cursor.execute("select * from information")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.information_table.delete(*self.information_table.get_children())
            for row in rows:
                self.information_table.insert('',END,values=row)
            connect.commit()
        connect.close()

    def get_cursor(self,event=""):
        cursor_row=self.information_table.focus()
        content=self.information_table.item(cursor_row)
        row=content["values"]
        self.citizen_ref.set(row[0])
        self.citizen_name.set(row[1])
        self.citizen_ID.set(row[2])
        self.citizen_DOB.set(row[3])
        self.nationality=row[4]
        self.gender=row[5]
        self.address.set(row[6])
        self.marriage_status=row[7]

    def clear(self):
        self.citizen_ref.set("")
        self.citizen_name.set("")
        self.citizen_ID.set("")
        self.citizen_DOB.set("")
        self.address.set("")
    
    def add_data(self):
        connect=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="mydata")
        my_cursor=connect.cursor()
        my_cursor.execute("insert into information values(%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.citizen_ref.get(),
            self.citizen_name.get(),
            self.citizen_ID.get(),
            self.citizen_DOB.get(),
            self.nationality,
            self.gender,
            self.address.get(),
            self.marriage_status
        ))
        connect.commit()
        self.fetch_data()
        self.clear()
        connect.close()
    def update_data(self):
        connect=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="mydata")
        my_cursor=connect.cursor()
        my_cursor.execute("update information set  `Citizen Name`=%s,  `Citizen ID`=%s, DOB=%s, Nationality=%s,Gender=%s,Address=%s,`Marriage Status`=%s where `Citizen ref`=%s",(
            self.citizen_name.get(),
            self.citizen_ID.get(),
            self.citizen_DOB.get(),
            self.nationality,
            self.gender,
            self.address.get(),
            self.marriage_status,
            self.citizen_ref.get()
        ))
        connect.commit()
        self.fetch_data()
        self.clear()
        connect.close()
    def delete_data(self):
        selected_items = self.information_table.selection()
        if not selected_items:
            messagebox.showinfo("Error", "Please select record(s) to delete")
            return
        
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete the selected record(s)?")
        if not confirm:
            return
        
        connect = mysql.connector.connect(host="localhost", username="root", password="Mysql@123", database="mydata")
        my_cursor = connect.cursor()
        
        for item in selected_items:
            values = self.information_table.item(item, "values")
            citizen_id = values[2]
            query = "DELETE FROM information WHERE `citizen ID` = %s"
            value = (citizen_id,)
            my_cursor.execute(query, value)
            connect.commit()
        
        connect.close()
        self.fetch_data()
        self.clear()
            
    def search_data(self):
        connect = mysql.connector.connect(host="localhost", username="root", password="Mysql@123", database="mydata")
        my_cursor = connect.cursor()
        if self.search_by=="Citizen ID":
            my_cursor.execute("select * from information where `Citizen ID`=%s", (self.search_txt.get(),))
        elif self.search_by=="Citizen Name":
            my_cursor.execute("select * from information where `Citizen Name`=%s", (self.search_txt.get(),))
        elif self.search_by=="Citizen ref":
            my_cursor.execute("select * from information where `Citizen ref`=%s", (self.search_txt.get(),))
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.information_table.delete(*self.information_table.get_children())
            for row in rows:
                self.information_table.insert('', END, values=row)
            connect.commit()
        connect.close()


