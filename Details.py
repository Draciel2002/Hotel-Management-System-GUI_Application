from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strptime
from datetime import datetime
from tkinter import messagebox



class Details_Room:
    def __init__(self,root): 
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1045x475+230+220")
        self.root.configure(bg="Pink")
        
        #################### Title ###############
        lbl_title=Label(self.root,text="HOTEL DETAILS WINDOW", font=("book antiqua",20,"bold"),bg="black",fg="gold",bd=1,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1045,height=50)
        
        ##### Logo #######
        img2=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\logo.png")
        img2=img2.resize((85,45), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2, bd=0,relief=RIDGE)
        lblimg.place(x=4,y=2,width=90,height=47)
        
        ################## Hotel Room Label frame ###############
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details Modification",font=("Arial Mt Bold",14,"bold"),fg="Purple",padx=2)
        labelframeleft.place(x=5,y=50,width=535,height=415)
        
        #Floor
        lbl_floor=Label(labelframeleft,text="Floor : ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        lbl_floor.grid(row=0,column=0,sticky=W)
        
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("Calibri Body",10))
        entry_floor.grid(row=0,column=1,sticky=W)
        
        #Room Number
        lbl_RoomNo=Label(labelframeleft,text="Room Number : ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        
        self.var_RoomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=("Calibri Body",10))
        entry_RoomNo.grid(row=1,column=1,sticky=W)
        
        #Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type : ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        
        self.var_RoomType=StringVar()
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_RoomType,font=("Calibri Body",10),width=18,state="readonly")
        combo_RoomType["value"]=("Single Suite","Double Suite","Luxury Suite","Premium Suite")
        combo_RoomType.grid(row=2,column=1)
        
        #Room Charge
        lbl_TelephoneNo=Label(labelframeleft,text="Room Charge/Day(₹): ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        lbl_TelephoneNo.grid(row=3,column=0,sticky=W)
        
        self.var_RoomCharge=StringVar()
        entry_TelephoneNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomCharge,width=20,font=("Calibri Body",10))
        entry_TelephoneNo.grid(row=3,column=1,sticky=W)
        
        #Air-Conditioned
        lbl_cust_AC=Label(labelframeleft,text="Air-Conditioned: ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        lbl_cust_AC.grid(row=4,column=0,sticky=W)
        
        self.var_AC=StringVar()
        combo_AC=ttk.Combobox(labelframeleft,textvariable=self.var_AC,font=("Calibri Body",10),width=18,state="readonly")
        combo_AC["value"]=("Yes","No")
        combo_AC.grid(row=4,column=1)
        
        #Telephone_Number
        lbl_TelephoneNo=Label(labelframeleft,text="Telephone Number: ",font=("Times New Roman",11,"bold"),padx=2,pady=4)
        lbl_TelephoneNo.grid(row=5,column=0,sticky=W)
        
        self.var_Telephone=StringVar()
        entry_TelephoneNo=ttk.Entry(labelframeleft,textvariable=self.var_Telephone,width=20,font=("Calibri Body",10))
        entry_TelephoneNo.grid(row=5,column=1,sticky=W)
        
        ######################################## Meal Plan Price Details Label Frame #################################
           
        self.label2=LabelFrame(self.root,bd=2,relief=RIDGE,text="Meal Plan Details",font=("Arial Mt Bold",14,"bold"),fg="Purple",padx=2)
        self.label2.place(x=10,y=250,width=520,height=210)
        
        #View btn
        btnView=Button(self.label2,text="View Meal Details",command=self.View_Meal,font=("Arial Mt Bold",12,"bold"),bg="blue",fg="white",width=20,height=1)
        btnView.place(x=30,y=10)
        
        #Update price_btn
        btnView=Button(self.label2,text="Update Meal Price",command=self.update2,font=("Arial Mt Bold",12,"bold"),bg="blue",fg="white",width=20,height=1)
        btnView.place(x=280,y=10)
        
        lbl_mealplan=Label(self.label2,text="Select Meal Plan",font=("Book Antiqua",12,"bold"),padx=2,pady=0)
        lbl_mealplan.place(x=280,y=45)
        
        self.var_meal=StringVar()
        combo_MealType=ttk.Combobox(self.label2,textvariable=self.var_meal,font=("Calibri Body",10),width=27,state="readonly")
        combo_MealType["value"]=("Select","Silver Meal Plan","Gold Meal Plan","Diamond Meal Plan","Platinum Meal Plan")
        combo_MealType.current(0)
        combo_MealType.place(x=280,y=70)
        
        lbl_mealplan=Label(self.label2,text=" Enter Price/Day (₹)",font=("Book antiqua",12,"bold"),padx=2,pady=0)
        lbl_mealplan.place(x=280,y=100)
        
        self.var_MealPrice=StringVar()
        entry_MealPrice=ttk.Entry(self.label2,textvariable=self.var_MealPrice,width=20,font=("Calibri Body",10))
        entry_MealPrice.place(x=280,y=130)

       
        ################################## Buttons #####################################
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=400,y=0,width=113,height=135)
        
        btnAdd=Button(btn_frame, text="ADD",command=self.add_data,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=10,height=1)
        btnAdd.grid(row=0,column=0)
        
        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=10,height=1)
        btnUpdate.grid(row=1,column=0)
        
        btnDelete=Button(btn_frame, text="DELETE",command=self.mDelete,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=10,height=1)
        btnDelete.grid(row=2,column=0)
        
        btnReset=Button(btn_frame, text="RESET",command=self.reset,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=10,height=1)
        btnReset.grid(row=3,column=0)
        
        ############################ Table Frame Search Sytem ##################################
      
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Room Details",font=("Arial Mt Bold",14,"bold"),fg="Purple",padx=2)
        Table_Frame.place(x=565,y=50,width=475,height=415)
        
        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        
        self.room_Table=ttk.Treeview(Table_Frame,column=("Floor","Room_Number","Room_Type","Room_Charge","Air_Conditioned","Telephone_Number"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
   
        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)
        
        self.room_Table.heading("Floor",text="Floor")
        self.room_Table.heading("Room_Number",text="Room Number")
        self.room_Table.heading("Room_Type",text="Room Type")
        self.room_Table.heading("Room_Charge",text="Room Charge")
        self.room_Table.heading("Air_Conditioned",text="Air Conditioned")
        self.room_Table.heading("Telephone_Number",text="Telephone Number")

      
        self.room_Table["show"]="headings"
        
        self.room_Table.column("Floor",width=100)
        self.room_Table.column("Room_Number",width=100)
        self.room_Table.column("Room_Type",width=100)
        self.room_Table.column("Room_Charge",width=100)
        self.room_Table.column("Air_Conditioned",width=100)
        self.room_Table.column("Telephone_Number",width=100)
       
        self.room_Table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
    ########################## Adding Data to the Database###################################   
     
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("!! ERROR !!","Fields Cannot Be Empty ",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_floor.get(),
                                                                                self.var_RoomNo.get(),
                                                                                self.var_RoomType.get(),
                                                                                self.var_RoomCharge.get(),
                                                                                self.var_AC.get(),
                                                                                self.var_Telephone.get()
                                                                            ))                                                                                   
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("!! SUCCESS !!","NEW ROOM ADDED SUCESSFULLY.",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)   
    
    ################ Fetch data Funtion #################
   
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()   
        
    ####### Curson to move across the database displayed in a table manner ############
    
    def get_cursor(self,event=""):
        cursor_row=self.room_Table.focus()
        content=self.room_Table.item(cursor_row)
        row=content["values"]
        
        self.var_floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])
        self.var_RoomCharge.set(row[3])
        self.var_AC.set(row[4])
        self.var_Telephone.set(row[5])
        
    ################## Updating the Data stored in Database ###############################
    
    def update(self):
        if self.var_floor.get()=="" or self.var_RoomNo.get()=="" or self.var_Telephone.get()=="":
            messagebox.showerror("!! ERROR !!","Please Enter the Empty Field",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,Room_Type=%s,Room_Charge=%s,Air_Conditioned=%s,Telephone_Number=%s where Room_Number=%s",(
                                                                                                                        self.var_floor.get(),
                                                                                                                        self.var_RoomType.get(),      
                                                                                                                        self.var_RoomCharge.get(),                                                                                                                 
                                                                                                                        self.var_AC.get(),
                                                                                                                        self.var_Telephone.get(),
                                                                                                                        self.var_RoomNo.get()
                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("!! UPDATED !!", "New Room Details Has Been Updated Sucessfully",parent=self.root)
      
    ############## Deleting any Data from the Database ######################
              
    def mDelete(self):
        mDelete=messagebox.askyesno("!! VERIFICATION !!","Do you Want to Delete this Hotel Room  Details ?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            query="delete from details where Room_Number=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("!! DELETED !!", "Hotel Room Details Has Been Deleted Sucessfully",parent=self.root)       
    
    ##################### Resetting the Data enrty Fields ##############
    def reset(self):
        self.var_floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")
        self.var_RoomCharge.set("")
        self.var_AC.set("")
        self.var_Telephone.set("")
        self.var_meal.set("")
        self.var_MealPrice.set("")
        self.Table_View.destroy()
        
    ############################### View Meal Price data table ########################
    def View_Meal(self):
        self.Table_View=LabelFrame(self.label2,bd=1,relief=RIDGE,text="View Meal Details",font=("Arial Mt Bold",12,"bold"),fg="Purple",padx=1)
        self.Table_View.place(x=5,y=50,width=260,height=130)
        
        scroll_x=ttk.Scrollbar(self.Table_View,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.Table_View,orient=VERTICAL)
        
        self.View_Table=ttk.Treeview(self.Table_View,column=("Meal_Plan","Meal_Price","Meal_Description"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
   
        scroll_x.config(command=self.View_Table.xview)
        scroll_y.config(command=self.View_Table.yview)
        
        self.View_Table.heading("Meal_Plan",text="Meal Plan")
        self.View_Table.heading("Meal_Price",text="Meal Price(₹)")
        self.View_Table.heading("Meal_Description",text="Meal_Description")
        
        self.View_Table["show"]="headings"
        
        self.View_Table.column("Meal_Plan",width=150)
        self.View_Table.column("Meal_Price",width=100)
        self.View_Table.column("Meal_Description",width=300)
        self.View_Table.pack(fill=BOTH,expand=1)
        
        self.fetch_data1()
        
        ################ Fetch Meal data Funtion #################
   
    def fetch_data1(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from meal")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.View_Table.delete(*self.View_Table.get_children())
            for i in rows:
                self.View_Table.insert("",END,values=i)
            conn.commit()
        conn.close() 
        
        ################## Updating the Meal Price ###############################
    
    def update2(self):
        if self.var_meal.get()=="Select" or self.var_MealPrice.get()=="":
            messagebox.showerror("!! ERROR !!","Please enter the values to be updated",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update meal set Meal_Price=%s where Meal_Plan=%s",(
                                                                                    self.var_MealPrice.get(),
                                                                                    self.var_meal.get()     
                                                                                        ))
            conn.commit()
            self.fetch_data1()
            conn.close()
            messagebox.showinfo("!! UPDATED !!", "New  Price Details Has Been Updated Sucessfully",parent=self.root)  
        
               
######################### Main function //DRIVER CODE ##########################     

if __name__== "__main__":
    root=Tk()
    obj=Details_Room(root)
    root.mainloop()