
from tkinter import *
from domains.information import Information
from domains.Death_Declaration import DeathDeclaration
from domains.Marriage import Marriage
from domains.Birth_declaration import BirthDeclaration

class CitizenInformation:
    def __init__(self, root):
        self.root = root
        self.root.title("Citizen Information")
        self.root.geometry("1350x700+0+0")

        # title
        lbl_title = Label(self.root, text="Citizen Information", font=("times new roman", 40, "bold"), bg="white", fg="green")
        lbl_title.place(x=0, y=110, width=1450, height=50)

        #main frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)       
        main_frame.place(x=0, y=160, width=1450, height=500)  

        # menu frame
        lbl_menu=Label(main_frame, text="Menu", font=("times new roman", 20, "bold"), bg="white", fg="green")
        lbl_menu.place(x=0, y=0, width=230) 

        # button frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=50, width=230, height=450)

        cust_btn = Button(btn_frame, text="Citizen information", command=self.cust_details, font=("times new roman", 15, "bold"), bg="white", fg="green", cursor="hand2")
        cust_btn.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        cust_btn2 = Button(btn_frame, text="Marriage",command=self.marriage, font=("times new roman", 15, "bold"), bg="white", fg="green", cursor="hand2")
        cust_btn2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        cust_btn3 = Button(btn_frame, text="Birth declaration",command=self.birth, font=("times new roman", 15, "bold"), bg="white", fg="green", cursor="hand2")
        cust_btn3.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        cust_btn4 = Button(btn_frame, text="Death declaration", command=self.death, font=("times new roman", 15, "bold"), bg="white", fg="green", cursor="hand2")
        cust_btn4.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Information(self.new_window)
    def birth(self):
        self.new_window = Toplevel(self.root)
        self.app = BirthDeclaration(self.new_window)
    def death(self):
        self.new_window = Toplevel(self.root)
        self.app = DeathDeclaration(self.new_window)
    def marriage(self):
        self.new_window = Toplevel(self.root)
        self.app = Marriage(self.new_window)

root = Tk()
obj = CitizenInformation(root)
root.mainloop()



