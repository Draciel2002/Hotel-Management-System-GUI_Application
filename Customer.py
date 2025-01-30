from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_win:
    def __init__(self,root): 
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1045x475+230+220")
        self.root.configure(bg="Pink")
        
        ##################Variables##########################
        self.var_Cust_ID=StringVar()
        x=random.randint(1000,9999)
        self.var_Cust_ID.set(str(x))
        
        self.var_Cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_address=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        
        #################### Title ###############
        lbl_title=Label(self.root,text="CUSTOMER MODIFICATION WINDOW", font=("book antiqua",20,"bold"),bg="black",fg="gold",bd=1,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1045,height=50)
        
        ##### Logo #######
        img2=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\logo.png")
        img2=img2.resize((85,45), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2, bd=0,relief=RIDGE)
        lblimg.place(x=4,y=2,width=90,height=47)
        
        ################## Label frame ###############
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("Arial Mt Bold",14,"bold"),fg="Purple",padx=2)
        labelframeleft.place(x=5,y=50,width=400,height=415)
        
        ################## Labels and Entry #############
        #Customer reference
        lbl_cust_id=Label(labelframeleft,text="Customer ID : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_cust_id.grid(row=0,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_Cust_ID,width=29,font=("Calibri Body",10),state="readonly")
        entry_ref.grid(row=0,column=1)
        
        #Customer Name
        lbl_cust_ref=Label(labelframeleft,text="Customer Name : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_Cust_name,width=29,font=("Calibri Body",10))
        entry_ref.grid(row=1,column=1)
        
        #gender combobox
        lbl_cust_ref=Label(labelframeleft,text="Gender : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=2,column=0,sticky=W)
        
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("Calibri Body",10),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Others")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)
        
        #Address
        lbl_cust_ref=Label(labelframeleft,text="Address : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=3,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("Calibri Body",10))
        entry_ref.grid(row=3,column=1)
        
        #mobile number
        lbl_cust_ref=Label(labelframeleft,text="Mobile Number : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=4,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("Calibri Body",10))
        entry_ref.grid(row=4,column=1)
        
        #email
        lbl_cust_ref=Label(labelframeleft,text="Email : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=5,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("Calibri Body",10))
        entry_ref.grid(row=5,column=1)
        
        #Nationality
        lbl_cust_ref=Label(labelframeleft,text="Nationality : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=6,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_nationality,width=29,font=("Calibri Body",10))
        entry_ref.grid(row=6,column=1)
       

        #Id Proof Type combobox
        lbl_cust_ref=Label(labelframeleft,text="ID Proof Type : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=7,column=0,sticky=W)
        
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("Calibri Body",10),width=27,state="readonly")
        combo_id["value"]=("Aadhaar Card","Driving Lisence","Passport","VoterID","Any-Goverment ID")
        combo_id.current(0)
        combo_id.grid(row=7,column=1)
        
        #Id Number
        lbl_cust_ref=Label(labelframeleft,text="ID Number : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=8,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("Calibri Body",10))
        entry_ref.grid(row=8,column=1)
        
        
        ################################## Buttons #####################################
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=320,width=390,height=50)
        
        btnAdd=Button(btn_frame, text="ADD",command=self.add_data,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=9,height=2)
        btnAdd.grid(row=0,column=0)
        
        btnUpdate=Button(btn_frame, text="UPDATE",command=self.update,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=9,height=2)
        btnUpdate.grid(row=0,column=1)
        
        btnDelete=Button(btn_frame, text="DELETE",command=self.mDelete,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=9,height=2)
        btnDelete.grid(row=0,column=2)
        
        btnReset=Button(btn_frame, text="RESET",command=self.reset,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=9,height=2)
        btnReset.grid(row=0,column=3)
        
        ############################ Table Frame Search Sytem ##################################
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("Arial Mt Bold",14,"bold"),fg="Purple",padx=2)
        Table_Frame.place(x=435,y=50,width=600,height=415)
        
        lblSearchBy=Label(Table_Frame,text="Search By : ",font=("Book antiqua",12,"bold"),bg="maroon", fg= "white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("Calibri body",12),width=12,state="readonly",)
        combo_search["value"]=("Customer_ID","Mobile_Number","ID_Number")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.text_search=StringVar()
        text_Search=ttk.Entry(Table_Frame,textvariable=self.text_search,width=18,font=("Calibri Body",12))
        text_Search.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_Frame, text="SEARCH",command=self.Search,font=("Arial Mt Bold",10,"bold"),bg="maroon",fg="white",width=9,padx=2,pady=3)
        btnSearch.grid(row=0,column=3)
        
        btnShowall=Button(Table_Frame, text="DISPLAY ALL",command=self.fetch_data,font=("Arial Mt Bold",10,"bold"),bg="maroon",fg="white",width=12,padx=2,pady=3)
        btnShowall.grid(row=0,column=4)
        
        
      ################################### Show Data Table #################################
        
        detail_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=45,width=590,height=320)
        
        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(detail_table,column=("Customer_ID","Customer_Name","Gender","Address","Mobile_Number","Email","Nationality","ID_Proof","ID_Number"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("Customer_ID",text="Customer ID")
        self.Cust_Details_Table.heading("Customer_Name",text="Customer Name")
        self.Cust_Details_Table.heading("Gender",text="Gender")
        self.Cust_Details_Table.heading("Address",text="Address")
        self.Cust_Details_Table.heading("Mobile_Number",text="Mobile Number")
        self.Cust_Details_Table.heading("Email",text="Email")
        self.Cust_Details_Table.heading("Nationality",text="Nationality")
        self.Cust_Details_Table.heading("ID_Proof",text="ID Proof")
        self.Cust_Details_Table.heading("ID_Number",text="ID Number")
          
        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("Customer_ID",width=100)
        self.Cust_Details_Table.column("Customer_Name",width=200)
        self.Cust_Details_Table.column("Gender",width=100)
        self.Cust_Details_Table.column("Address",width=300)
        self.Cust_Details_Table.column("Mobile_Number",width=100)
        self.Cust_Details_Table.column("Email",width=200)
        self.Cust_Details_Table.column("Nationality",width=100)
        self.Cust_Details_Table.column("ID_Proof",width=100)
        self.Cust_Details_Table.column("ID_Number",width=150)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    ####### Adding Data to a Database ##############  
      
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_id_number.get()=="":
            messagebox.showerror("!! ERROR !!","Fields Cannot Be Empty ",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_Cust_ID.get(),
                                                                                        self.var_Cust_name.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_id_proof.get(),
                                                                                        self.var_id_number.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("!! SUCCESS !!","Customer Has Been Added Sucessfully.",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)
                
    ######### Fetching the data back from the database to Display on Screen ###############
            
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    ####### Curson to move across the database displayed in a table manner ############
    
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]
        
        self.var_Cust_ID.set(row[0]),
        self.var_Cust_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_address.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_nationality.set(row[6]),
        self.var_id_proof.set(row[7]),
        self.var_id_number.set(row[8])
     
    ################## Updating the Data stored in Database ###############################
    
    def update(self):
        if self.var_mobile.get()=="" or self.var_id_number.get()=="":
            messagebox.showerror("!! ERROR !!","Please Enter the Empty Field",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Customer_Name=%s,Gender=%s,Address=%s,Mobile_Number=%s,Email=%s,Nationality=%s,ID_Proof=%s,ID_Number=%s where Customer_ID=%s",(
                                                                                                                                                            
                                                                                                                                                                self.var_Cust_name.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                                self.var_id_proof.get(),
                                                                                                                                                                self.var_id_number.get(),
                                                                                                                                                                self.var_Cust_ID.get()   
                                                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("!! UPDATED !!", "Customer Details Has Been Updated Sucessfully",parent=self.root)
            
    ############## Deleting any Data from the Database ######################
              
    def mDelete(self):
        mDelete=messagebox.askyesno("!! VERIFICATION !!","Do you Want to Delete this Customer Details ?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Customer_ID=%s"
            value=(self.var_Cust_ID.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("!! DELETED !!", "Customer Details Has Been Deleted Sucessfully",parent=self.root)
    
    ########## Reseting the Sreen for new Data fields entry in database ##########
    
    def reset(self):
        #self.var_Cust_ID.set(""), 
        self.var_Cust_name.set(""),
        #self.var_gender.set(""),
        self.var_address.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set("")
        
        x=random.randint(1000,9999)      #After Reset again randomly generate the unique Customer ID
        self.var_Cust_ID.set(str(x))
        
    ###################### Searching any Data object from the Database using given data fields #############
          
    def  Search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.text_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
         
                          
######################### Main function //DRIVER CODE ##########################      
        
 
if __name__== "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()
