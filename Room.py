from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkcalendar import Calendar
from time import strptime
from datetime import datetime
from tkinter import messagebox


class Room_booking:
    def __init__(self,root): 
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1045x475+230+220")
        self.root.configure(bg="Pink")
        
        ########################## Variables ##################
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_mealheads=StringVar()
        self.var_mealdetails=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_total=StringVar()
        
    
       #################### Title ###############
        lbl_title=Label(self.root,text="ROOM BOOKING WINDOW", font=("book antiqua",20,"bold"),bg="Black",fg="gold",bd=1,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1045,height=50)
        
        ##### Logo #######
        img2=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\logo.png")
        img2=img2.resize((85,45), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2, bd=0,relief=RIDGE)
        lblimg.place(x=4,y=2,width=90,height=47)
        
        ################## Label frame ###############
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("Arial Mt Bold",18,"bold"),fg="Brown",padx=2)
        labelframeleft.place(x=5,y=50,width=400,height=415)
        
        ######################################## Labels and Entry #################################################
         
        #Customer Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact : ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("Calibri Body",10))
        entry_contact.grid(row=0,column=1,sticky=W)
        
        ###########Fetch Data Button############
        btnfetch=Button(labelframeleft, text="FETCH DATA",command=self.fetch_contact,font=("Arial Mt Bold",10,"bold"),bg="blue",fg="white",width=10)
        btnfetch.place(x=300,y=0)
        
        #Check In Date
        check_in_date=Label(labelframeleft,text="Check In Date : ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        check_in_date.grid(row=1,column=0,sticky=W)
        
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("Calibri Body",10))
        txtcheck_in_date.grid(row=1,column=1)
        
        #Check Out Date
        check_out_date=Label(labelframeleft,text="Check Out Date : ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        check_out_date.grid(row=2,column=0,sticky=W)
        
        txtcheck_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("Calibri Body",10))
        txtcheck_out_date.grid(row=2,column=1)
        
        #No Of days for stay
        lbl_NoOfDays=Label(labelframeleft,text="Number of Days: ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        lbl_NoOfDays.grid(row=3,column=0,sticky=W)
        
        txt_NoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=35,font=("Calibri Body",10,"bold"),state="readonly")
        txt_NoOfDays.grid(row=3,column=1)
        
        # Meal
        lbl_cust_RoomType=Label(labelframeleft,text="Meal Plan: ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        lbl_cust_RoomType.grid(row=4,column=0,sticky=W)
        
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("Calibri Body",10),width=27,state="readonly")
        combo_RoomType["value"]=("Silver Meal Plan","Gold Meal Plan","Diamond Meal Plan","Platinum Meal Plan")
        #combo_RoomType.current(0)
        combo_RoomType.grid(row=4,column=1)
        
        # Meal heads
        Meal_heads=Label(labelframeleft,text="Meal Heads : ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        Meal_heads.grid(row=5,column=0,sticky=W)
        
        txtMeal_heads=ttk.Entry(labelframeleft,textvariable=self.var_mealheads,width=29,font=("Calibri Body",10))
        txtMeal_heads.grid(row=5,column=1)
        
        #Meal_Details
        lbl_SubTotal=Label(labelframeleft,text="Meal Details: ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        lbl_SubTotal.grid(row=6,column=0,sticky=W)
        
        txt_SubTotal=ttk.Entry(labelframeleft,textvariable=self.var_mealdetails,width=35,font=("Calibri Body",9,"bold"),state="readonly")
        txt_SubTotal.grid(row=6,column=1)
         
        #Room Type
        lbl_cust_RoomType=Label(labelframeleft,text="Room Type : ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        lbl_cust_RoomType.grid(row=7,column=0,sticky=W)
        
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("Calibri Body",10),width=27,state="readonly")
        combo_RoomType["value"]=("Single Suite","Double Suite","Luxury Suite","Premium Suite")
        #combo_RoomType.current(0)
        combo_RoomType.grid(row=7,column=1)

        #Available Room
        lbl_avlblRoom=Label(labelframeleft,text="Available Room: ",font=("Times New Roman",12,"bold"),padx=2,pady=4)
        lbl_avlblRoom.place(x=0,y=260)
        
        ########### View Button ############
        btnView=Button(labelframeleft, text="VIEW",command=self.View,font=("Arial Mt Bold",10,"bold"),bg="blue",fg="white",width=5,padx=1,pady=1)
        btnView.place(x=130,y=260)
        

        ######## Confirm Button ###########
        btnconfirm=Button(labelframeleft, text="CONFIRM",command=self.Confirm,font=("Arial Mt Bold",12,"bold"),bg="blue",fg="white",width=13,height=1)
        btnconfirm.place(x=5,y=300)
        
        ################################## Buttons #####################################
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=335,width=390,height=50)
        
        btnAdd=Button(btn_frame, text="BOOK",command=self.add_data,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=9,height=2)
        btnAdd.grid(row=0,column=0)
        
        btnUpdate=Button(btn_frame, text="UPDATE",command=self.update,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=9,height=2)
        btnUpdate.grid(row=0,column=1)
        
        btnDelete=Button(btn_frame, text="DELETE",command=self.mDelete,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=9,height=2)
        btnDelete.grid(row=0,column=2)
        
        btnReset=Button(btn_frame, text="RESET",command=self.reset,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=9,height=2)
        btnReset.grid(row=0,column=3)
        
       ###################### Right Side Image ###################
        img3=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\hotel4.jpg")
        img3=img3.resize((320,200), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg=Label(self.root,image=self.photoimg3, bg="Pink",bd=0,relief=RIDGE)
        lblimg.place(x=660,y=50,width=430,height=200)
        
       ############################ Table Frame Search Sytem ##################################
      
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("Arial Mt Bold",14,"bold"),fg="Purple",padx=2)
        Table_Frame.place(x=410,y=250,width=625,height=220)
        
        lblSearchBy=Label(Table_Frame,text="Search By : ",font=("Book antiqua",12,"bold"),bg="maroon", fg= "white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("Calibri body",12),width=12,state="readonly",)
        combo_search["value"]=("Contact","Room_Number")
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
        detail_table.place(x=0,y=45,width=620,height=150)
        
        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        
        self.room_Table=ttk.Treeview(detail_table,column=("Contact","Check_In_Date","Check_Out_Date","Number_Of_Days","Meal_Plan","Meal_Heads","Meal_Details","Room_Type","Room_Number"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
   
        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)
        
        self.room_Table.heading("Contact",text="Contact")
        self.room_Table.heading("Check_In_Date",text="Check In Date")
        self.room_Table.heading("Check_Out_Date",text="Check Out Date")
        self.room_Table.heading("Number_Of_Days",text="Number Of Days")
        self.room_Table.heading("Meal_Plan",text="Meal Plan")
        self.room_Table.heading("Meal_Heads",text="Meal Heads")
        self.room_Table.heading("Meal_Details",text="Meal Details")
        self.room_Table.heading("Room_Type",text="Room Type")
        self.room_Table.heading("Room_Number",text="Room Number")
        
        
      
        self.room_Table["show"]="headings"
        
        self.room_Table.column("Contact",width=100)
        self.room_Table.column("Check_In_Date",width=100)
        self.room_Table.column("Check_Out_Date",width=100)
        self.room_Table.column("Number_Of_Days",width=100)
        self.room_Table.column("Meal_Plan",width=130)
        self.room_Table.column("Meal_Heads",width=100)
        self.room_Table.column("Meal_Details",width=300)
        self.room_Table.column("Room_Type",width=100)
        self.room_Table.column("Room_Number",width=100)
        
        
       
        self.room_Table.pack(fill=BOTH,expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    ########################## Adding Data to the Database###################################   
     
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("!! ERROR !!","Fields Cannot Be Empty ",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_noofdays.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_mealheads.get(),
                                                                                self.var_mealdetails.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailable.get(),
                                                                                ))                                                                                   
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("!! SUCCESS !!","ROOM BOOKED SUCESSFULLY.",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)   
   
   ################ Fetch data Funtion #################
   
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()    
            
    ####### Cursor to move across the database displayed in a table manner ############
    
    def get_cursor(self,event=""):
        cursor_row=self.room_Table.focus()
        content=self.room_Table.item(cursor_row)
        row=content["values"]
        
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_noofdays.set(row[3])
        self.var_meal.set(row[4])
        self.var_mealheads.set(row[5])
        self.var_mealdetails.set(row[6])
        self.var_roomtype.set(row[7])
        self.var_roomavailable.set(row[8])
        

    ################## Updating the Data stored in Database ###############################
    
    def update(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("!! ERROR !!","Please Enter the Empty Field",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Check_Out_Date=%s,Number_Of_Days=%s,Meal_Plan=%s,Meal_Heads=%s,Meal_Details=%s,Room_Type=%s,Room_Number=%s where Contact=%s and Check_In_Date=%s",(
                                                                                                                                                                        self.var_checkout.get(),
                                                                                                                                                                        self.var_noofdays.get(),
                                                                                                                                                                        self.var_meal.get(),
                                                                                                                                                                        self.var_mealheads.get(),
                                                                                                                                                                        self.var_mealdetails.get(),
                                                                                                                                                                        self.var_roomtype.get(),
                                                                                                                                                                        self.var_roomavailable.get(),
                                                                                                                                                                        self.var_contact.get(), 
                                                                                                                                                                        self.var_checkin.get() 
                                                                                                                                                                                                 ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("!! UPDATED !!", "Room Booking Details Has Been Updated Sucessfully",parent=self.root)
      
     ############## Deleting any Data from the Database ######################
              
    def mDelete(self):
        mDelete=messagebox.askyesno("!! VERIFICATION !!","Do you Want to Delete this Room Booking Details ?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("!! DELETED !!", "Room Booking Detail Has Been Deleted Sucessfully",parent=self.root)       
        
   ######################## Reset the data entry fields back to empty ###########################  
    def reset(self):   
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_mealheads.set("")
        self.var_mealdetails.set("")
        self.var_noofdays.set("")
        self.showDataFrame.destroy()
    
     ###################### Searching any Data object from the Database using given data fields #############
          
    def  Search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.text_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
           
    ################################### All Data Fetch ################################################  
    
    def fetch_contact(self):
      if self.var_contact.get()=="":
        messagebox.showerror("!! ERROR !!","Please Enter Contact Number",parent=self.root)
      else:
        ##################### Name ####################################
        conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
        my_cursor=conn.cursor() 
        query=("select Customer_Name from customer where Mobile_Number=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
       
        if row==None:
          messagebox.showerror("!! ERROR !!","This Contact Number Is Not Found",parent=self.root)
        else:
          conn.commit()
          conn.close()
          
          self.showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
          self.showDataFrame.place(x=410,y=55,width=300,height=180)
          
          lblName=Label(self.showDataFrame,text="Name:",font=("times newn roman",12,"bold"))
          lblName.place(x=0,y=0)
          
          lbl=Label(self.showDataFrame,text=row[0],font=("times newn roman",12,"bold"),fg="Blue")
          lbl.place(x=90,y=0)
          
          ####################### Gender ################
          conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
          my_cursor=conn.cursor() 
          query=("select Gender from customer where Mobile_Number=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblGender=Label(self.showDataFrame,text="Gender:",font=("times newn roman",12,"bold"))
          lblGender.place(x=0,y=30)
          
          lbl2=Label(self.showDataFrame,text=row[0],font=("times newn roman",10,"bold"),fg="Blue")
          lbl2.place(x=90,y=30)
          
          ####################### Email ####################
          conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
          my_cursor=conn.cursor() 
          query=("select Email from customer where Mobile_Number=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblEmail=Label(self.showDataFrame,text="Email:",font=("times newn roman",12,"bold"))
          lblEmail.place(x=0,y=60)
          
          lbl3=Label(self.showDataFrame,text=row[0],font=("times newn roman",10,"italic"),fg="Blue")
          lbl3.place(x=90,y=60)
          
          ######################### Nationality #####################
          conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
          my_cursor=conn.cursor() 
          query=("select Nationality from customer where Mobile_Number=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblNationality=Label(self.showDataFrame,text="Nationality:",font=("times newn roman",12,"bold"))
          lblNationality.place(x=0,y=90)
          
          lbl4=Label(self.showDataFrame,text=row[0],font=("times newn roman",10,"bold"),fg="Blue")
          lbl4.place(x=90,y=90)  
          
          ######################## Address ###############################
          conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
          my_cursor=conn.cursor() 
          query=("select Address from customer where Mobile_Number=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lbladdress=Label(self.showDataFrame,text="Address:",font=("times newn roman",12,"bold"))
          lbladdress.place(x=0,y=120)
          
          lbl5=Label(self.showDataFrame,text=row[0],font=("times newn roman",10,"bold"),fg="Blue")
          lbl5.place(x=90,y=120) 
          
   ######################################## View Available Room Details #####################################  
    def View(self):
        if self.var_roomtype.get()=="Single Suite":
            conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select Room_Number from details where Room_Type Like '%Single Suite%'")
            row2=my_cursor.fetchall()
        elif self.var_roomtype.get()=="Double Suite":
            conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select Room_Number from details where Room_Type Like '%Double Suite%'")
            row2=my_cursor.fetchall()    
        elif self.var_roomtype.get()=="Luxury Suite":
            conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select Room_Number from details where Room_Type Like '%Luxury Suite%'")
            row2=my_cursor.fetchall()
        elif self.var_roomtype.get()=="Premium Suite":
            conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select Room_Number from details where Room_Type Like '%Premium Suite%'")
            row2=my_cursor.fetchall()
            
        labelframeView=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Available Details",font=("Arial Mt Bold",10,"bold"),fg="Purple",padx=2)
        labelframeView.place(x=200,y=320,width=200,height=60)
        
        combo_RoomNo=ttk.Combobox(labelframeView,textvariable=self.var_roomavailable,font=("Calibri Body",10),height=50,width=23,state="readonly")
        combo_RoomNo["value"]= row2
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=0,column=0)
            
 
################################# Confirm Details Function ########################################      
 
    def Confirm(self):
        if self.var_checkin.get()=="" or self.var_checkout.get()=="":
            messagebox.showerror("!! ERROR !!","Please Enter the Empty Fields",parent=self.root)
                    
                    
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()  
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if self.var_meal.get() == "Silver Meal Plan":
            self.var_mealdetails.set("BreakFast Only")
        elif self.var_meal.get() == "Gold Meal Plan":
            self.var_mealdetails.set("BreakFast, Lunch / Dinner")
        elif self.var_meal.get() == "Diamond Meal Plan":
            self.var_mealdetails.set("BreakFast , Lunch And Dinner")
        elif self.var_meal.get() == "Platinum Meal Plan":
            self.var_mealdetails.set("Diamond Plan With Snacks And Drinks ")
    
        
        
######################### Main function //DRIVER CODE ##########################           

    
if __name__== "__main__":
    root=Tk()
    obj=Room_booking(root)
    root.mainloop()