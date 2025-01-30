from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strptime
from datetime import datetime
from tkinter import messagebox



class Billing_Data:
    def __init__(self,root): 
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1045x475+230+220")
        self.root.configure(bg="Pink")
        
        img1=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\hotel6.jpg")
        img1=img1.resize((290,280),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg1=Label(self.root,image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=735,y=40,width=310,height=435)
        
        lbl_up=Label(self.root,text="THANK YOU ❤️ ", font=("book antiqua",20,"bold"),bg="black",fg="red")
        lbl_up.place(x=780,y=60,width=270,height=50)
        
        lbl_down=Label(self.root,text="VISIT AGAIN 😊 ", font=("book antiqua",20,"bold"),bg="black",fg="gold")
        lbl_down.place(x=780,y=410,width=270,height=50)
        
        
        #################### Title ###############
        lbl_title=Label(self.root,text="BILLING   DETAILS  WINDOW", font=("book antiqua",20,"bold"),bg="black",fg="gold",bd=1,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1045,height=50)
        
        ##### Logo #######
        img2=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\logo.png")
        img2=img2.resize((85,45), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg2=Label(self.root,image=self.photoimg2, bd=0,relief=RIDGE)
        lblimg2.place(x=4,y=2,width=90,height=50)
        
        ################## Billing Label self.frame ###############
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Billing Details",font=("Arial Mt Bold",15,"bold"),fg="Purple",padx=2)
        labelframeleft.place(x=2,y=50,width=735,height=425)
        
        #Customer Contact
        lbl_Contact=Label(labelframeleft,text="Enter Contact Number :",font=("Times New Roman",12,"bold"),padx=2,pady=2)
        lbl_Contact.place(x=5,y=5)
        
        self.var_Contact=StringVar()
        entry_Contact=ttk.Entry(labelframeleft,textvariable=self.var_Contact,width=18,font=("Calibri Body",10))
        entry_Contact.place(x=175,y=5)
        
        #Room Number
        lbl_RoomNo=Label(labelframeleft,text="Enter Room Number :",font=("Times New Roman",12,"bold"),padx=2,pady=2)
        lbl_RoomNo.place(x=330,y=5)
        
        self.var_RoomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=10,font=("Calibri Body",10))
        entry_RoomNo.place(x=490,y=5)
        
        #Customer Name
        lbl_name=Label(labelframeleft,text="Customer Name :  ",font=("Times New Roman",12,"bold"),padx=2,pady=2)
        lbl_name.place(x=5,y=55)
        
        self.var_CustName=StringVar()
        entry_name=ttk.Entry(labelframeleft,textvariable=self.var_CustName,width=30,font=("Calibri Body",10),state="readonly")
        entry_name.place(x=135,y=55)
        
        #CheckIn Date
        lbl_Checkin=Label(labelframeleft,text="Check-In Date :  ",font=("Times New Roman",12,"bold"),padx=2,pady=2)
        lbl_Checkin.place(x=5,y=90)
        
        self.var_Checkin=StringVar()
        entry_Checkin=ttk.Entry(labelframeleft,textvariable=self.var_Checkin,width=30,font=("Calibri Body",10),state="readonly")
        entry_Checkin.place(x=135,y=90)
        
        #CheckOut Date
        lbl_Checkout=Label(labelframeleft,text="Check-Out Date :  ",font=("Times New Roman",12,"bold"),padx=2,pady=2)
        lbl_Checkout.place(x=5,y=125)
        
        self.var_Checkout=StringVar()
        entry_Checkout=ttk.Entry(labelframeleft,textvariable=self.var_Checkout,width=30,font=("Calibri Body",10),state="readonly")
        entry_Checkout.place(x=135,y=125)
        
        #Number OF Days
        lbl_NumberOfDays=Label(labelframeleft,text="Number Of Days :",font=("Times New Roman",12,"bold"),padx=2,pady=2)
        lbl_NumberOfDays.place(x=5,y=160)
        
        self.var_NumberOfDays=StringVar()
        entry_NumberOfDays=ttk.Entry(labelframeleft,textvariable=self.var_NumberOfDays,width=30,font=("Calibri Body",10),state="readonly")
        entry_NumberOfDays.place(x=135,y=160)
        
        #Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type :  ",font=("Times New Roman",12,"bold"),padx=2,pady=2)
        lbl_RoomType.place(x=5,y=195)
        
        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=30,font=("Calibri Body",10),state="readonly")
        entry_RoomType.place(x=135,y=195)
        
        #Room Charge
        lbl_RoomCharge=Label(labelframeleft,text="Room Charge Per Day : ₹",font=("Times New Roman",12,"bold"),padx=2,pady=2)
        lbl_RoomCharge.place(x=5,y=230)
        
        self.var_RoomCharge=StringVar()
        entry_RoomCharge=ttk.Entry(labelframeleft,textvariable=self.var_RoomCharge,width=22,font=("Calibri Body",10),state="readonly")
        entry_RoomCharge.place(x=190,y=230)
        
        #Meal_Plan
        lbl_MealPlan=Label(labelframeleft,text="Meal Plan :  ",font=("Times New Roman",12,"bold"),padx=2,pady=2)
        lbl_MealPlan.place(x=5,y=265)
        
        self.var_MealPlan=StringVar()
        entry_MealPlan=ttk.Entry(labelframeleft,textvariable=self.var_MealPlan,width=30,font=("Calibri Body",10),state="readonly")
        entry_MealPlan.place(x=135,y=265)
        
        #Meal_Heads
        lbl_MealHeads=Label(labelframeleft,text="Meal Heads :  ",font=("Times New Roman",12,"bold"),padx=2,pady=2)
        lbl_MealHeads.place(x=5,y=300)
        
        self.var_MealHeads=StringVar()
        entry_MealHeads=ttk.Entry(labelframeleft,textvariable=self.var_MealHeads,width=30,font=("Calibri Body",10),state="readonly")
        entry_MealHeads.place(x=135,y=300)
        
        #Meal_Charge
        lbl_MealCharge=Label(labelframeleft,text="Meal Charge Per Head Per Day : ₹",font=("Times New Roman",12,"bold"),padx=2,pady=2)
        lbl_MealCharge.place(x=5,y=335)
        
        self.var_MealCharge=StringVar()
        entry_MealCharge=ttk.Entry(labelframeleft,textvariable=self.var_MealCharge,width=13,font=("Calibri Body",10),state="readonly")
        entry_MealCharge.place(x=250,y=335)
        


        #################################### Buttons ####################################
        # Get Details Button
        btnfetch=Button(labelframeleft, text="GET DETAILS",command=self.get_details,font=("Arial Mt Bold",12,"bold"),bg="blue",fg="white",width=11)
        btnfetch.place(x=580,y=0)
        
        #Generate Bill Button
        btnfetch=Button(labelframeleft, text="GENERATE BILL",command=self.generate_bill,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=15)
        btnfetch.place(x=360,y=50)
        
        #Generate Reciept Button
        btnfetch=Button(labelframeleft, text="GENERATE RECIEPT",command=self.generate_reciept,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=17)
        btnfetch.place(x=530,y=50)
        
        #Reset Button
        btnfetch=Button(labelframeleft, text="RESET",command=self.reset,font=("Arial Mt Bold",12,"bold"),bg="green",fg="white",width=17)
        btnfetch.place(x=460,y=320)
        
    ################################# Get Details Function ##########################################
    def get_details(self):
        if self.var_Contact.get()=="" or self.var_RoomNo.get()=="":
            messagebox.showerror("!! ERROR !!","Please Enter the Empty fields  to get Details",parent=self.root)
        else:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Akkianmayank2002",database="management")
                my_cursor=conn.cursor() 
                
                #Customer_Name
                query1=("select Customer_Name from customer where Mobile_Number=%s")
                value1=(self.var_Contact.get(),)
                my_cursor.execute(query1,value1)
                row1=my_cursor.fetchone()
                if row1==None:
                  messagebox.showerror("!! ERROR !!","No Such Data Found",parent=self.root)
                self.var_CustName.set(row1[0])
                  
                #CheckIn Date
                query2=("select Check_In_Date from room where Room_Number=%s and Contact=%s")
                value2=(self.var_RoomNo.get(),self.var_Contact.get(),)
                my_cursor.execute(query2,value2)
                row2=my_cursor.fetchone()
                if row2==None:
                  messagebox.showerror("!! ERROR !!","No Such Data Found",parent=self.root)
                  self.reset()
                self.var_Checkin.set(row2[0])
                
                #CheckOut Date
                query3=("select Check_Out_Date from room where Room_Number=%s and Contact=%s")
                value3=(self.var_RoomNo.get(),self.var_Contact.get(),)
                my_cursor.execute(query3,value3)
                row3=my_cursor.fetchone()
                if row3==None:
                  messagebox.showerror("!! ERROR !!","No Such Data Found",parent=self.root)    
                self.var_Checkout.set(row3[0])
                
                #Number of Days
                query4=("select Number_Of_Days from room where Room_Number=%s and Contact=%s")
                value4=(self.var_RoomNo.get(),self.var_Contact.get(),)
                my_cursor.execute(query4,value4)
                row4=my_cursor.fetchone()
                if row4==None:
                  messagebox.showerror("!! ERROR !!","No Such Data Found",parent=self.root)
                self.var_NumberOfDays.set(row4[0])
                
                #Room Type
                query5=("select Room_Type from room where Room_Number=%s and Contact=%s")
                value5=(self.var_RoomNo.get(),self.var_Contact.get(),)
                my_cursor.execute(query5,value5)
                row5=my_cursor.fetchone()
                if row5==None:
                  messagebox.showerror("!! ERROR !!","No Such Data Found",parent=self.root)
                self.var_RoomType.set(row5[0])
                
                #Room Charge
                query6=("select Room_Charge from details where Room_Number=%s")
                value6=(self.var_RoomNo.get(),)
                my_cursor.execute(query6,value6)
                row6=my_cursor.fetchone()
                if row6==None:
                  messagebox.showerror("!! ERROR !!","No Such Data Found",parent=self.root)
                self.var_RoomCharge.set(row6[0])
                
                #Meal Plan
                query7=("select Meal_Plan from room where Room_Number=%s and Contact=%s")
                value7=(self.var_RoomNo.get(),self.var_Contact.get(),)
                my_cursor.execute(query7,value7)
                row7=my_cursor.fetchone()
                if row7==None:
                  messagebox.showerror("!! ERROR !!","No Such Data Found",parent=self.root)
                self.var_MealPlan.set(row7[0])
                
                #Meal Heads
                query8=("select Meal_Heads from room where Room_Number=%s and Contact=%s")
                value8=(self.var_RoomNo.get(),self.var_Contact.get(),)
                my_cursor.execute(query8,value8)
                row8=my_cursor.fetchone()
                if row8==None:
                  messagebox.showerror("!! ERROR !!","No Such Data Found",parent=self.root)
                self.var_MealHeads.set(row8[0])
                
                #Meal Charge
                query9=("select Meal_Price from meal where Meal_Plan=%s")
                value9=(self.var_MealPlan.get(),)
                my_cursor.execute(query9,value9)
                row9=my_cursor.fetchone()
                if row9==None:
                  messagebox.showerror("!! ERROR !!","No Such Data Found",parent=self.root)
                self.var_MealCharge.set(row9[0])

  ################################# Generate Bill Function ########################################## 
    def generate_bill(self):  
            if self.var_RoomCharge.get()=="" or self.var_MealCharge.get()=="":
              messagebox.showwarning("!! NO DETAILS !!","Get Customer Details to Generate Bill",parent=self.root) 
            else:
                self.labelframeBill=LabelFrame(self.root,bd=2,relief=RIDGE,text="< | BILL | >",font=("Engravers MT",15,"bold"),fg="red",padx=2)
                self.labelframeBill.place(x=380,y=170,width=315,height=210)
              
                #Total Stay_Charge
                lbl_totalstayCharge=Label(self.labelframeBill,text="LODGING CHARGE: ₹",font=("Times New Roman",12,"bold"),padx=2,pady=2)
                lbl_totalstayCharge.place(x=5,y=10)
                
                self.var_StayCharge=StringVar()
                entry_totalstayCharge=ttk.Entry(self.labelframeBill,textvariable=self.var_StayCharge,width=13,font=("Calibri Body",10),state="readonly")
                entry_totalstayCharge.place(x=180,y=10)
                
                x1=float(self.var_NumberOfDays.get())
                y1=float(self.var_RoomCharge.get())
                z1=float(x1*y1)
                total1=str("%.2f"%(z1))
                self.var_StayCharge.set(total1)
   
                #Total Meal_Charge
                lbl_totalMealCharge=Label(self.labelframeBill,text="MEAL CHARGE: ₹",font=("Times New Roman",12,"bold"),padx=2,pady=2)
                lbl_totalMealCharge.place(x=5,y=40)
                
                self.var_TotMealCharge=StringVar()
                entry_totalMealCharge=ttk.Entry(self.labelframeBill,textvariable=self.var_TotMealCharge,width=13,font=("Calibri Body",10),state="readonly")
                entry_totalMealCharge.place(x=180,y=40)
                
                x2=float(self.var_MealCharge.get())
                y2=float(self.var_MealHeads.get())
                a2=float(self.var_NumberOfDays.get())
                z2=float(x2*y2*a2)
                total2=str("%.2f"%(z2))
                self.var_TotMealCharge.set(total2)
                
                #Subtotal
                lbl_Subtotal=Label(self.labelframeBill,text="SUBTOTAL: ₹",font=("Times New Roman",12,"bold"),padx=2,pady=2)
                lbl_Subtotal.place(x=5,y=70)
                
                self.var_Subtotal=StringVar()
                entry_Subtotal=ttk.Entry(self.labelframeBill,textvariable=self.var_Subtotal,width=13,font=("Calibri Body",10),state="readonly")
                entry_Subtotal.place(x=180,y=70)
                
                a2=float(self.var_NumberOfDays.get())
                z3=float(z1+z2)
                total3=str("%.2f"%(z3))
                self.var_Subtotal.set(total3)
                
                #Tax
                lbl_Tax=Label(self.labelframeBill,text="TAX(CGST+SGST): ₹",font=("Times New Roman",12,"bold"),padx=2,pady=2)
                lbl_Tax.place(x=5,y=100)
                
                self.var_Tax=StringVar()
                entry_Tax=ttk.Entry(self.labelframeBill,textvariable=self.var_Tax,width=13,font=("Calibri Body",10),state="readonly")
                entry_Tax.place(x=180,y=100)
                
                if z3 < 5000:
                   z4=float((z3)*0.03) # tax rate at 3% below 5000
                elif z3 < 15000:
                   z4=float((z3)*0.06) # tax rate at 6% below 15000
                else:
                  z4=float((z3)*0.12) # tax rate at 12% otherwise
                           
                total4=str("%.2f"%(z4))
                self.var_Tax.set(total4)
                
                #Total Bill
                lbl_TotalBill=Label(self.labelframeBill,text="TOTAL BILL: ₹",font=("Times New Roman",14,"bold"),padx=2,pady=2)
                lbl_TotalBill.place(x=5,y=150)

                self.var_TotalBill=StringVar()
                entry_TotalBill=ttk.Entry(self.labelframeBill,textvariable=self.var_TotalBill,width=15,font=("Calibri Body",13),state="readonly")
                entry_TotalBill.place(x=160,y=150)
                
                z5=float(z3+z4)
                total5=str("%.2f"%(z5))
                self.var_TotalBill.set(total5)
  
  ################################# Generate Reciept Function ########################################## 
    def generate_reciept(self):
      if self.var_RoomCharge.get()=="" or self.var_MealCharge.get()=="" or self.var_RoomCharge.get()=="":
              messagebox.showwarning("!! NO DETAILS !!","Generate Bill to Generate Money reciept",parent=self.root) 
      else:
      
        self.frame=Frame(self.root,bg="gold")
        self.frame.place(x=740,y=50,width=300,height=425)
        
        ############## Frame Logo ########################
        img3=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\logo.png")
        img3=img3.resize((290,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        self.lblimg3=Label(self.root,image=self.photoimg3,bg="black",borderwidth=0)
        self.lblimg3.place(x=740,y=50,width=300,height=140)
        
        get_str=Label(self.frame,text="MONEY RECIEPT",font=("Arial MT Bold",12,"bold"),fg="red",bg="black")
        get_str.place(x=75,y=140)
        
        #Name
        lblName=Label(self.frame,text="Name:",font=("times newn roman",12,"bold"),bg="gold")
        lblName.place(x=0,y=170)
          
        lbl=Label(self.frame,text=self.var_CustName.get(),font=("times newn roman",12,"bold"),fg="blue",bg="gold")
        lbl.place(x=150,y=170)
        
        #Check-in
        lblName=Label(self.frame,text="Check In Date:",font=("times newn roman",12,"bold"),bg="gold")
        lblName.place(x=0,y=190)
          
        lbl=Label(self.frame,text=self.var_Checkin.get(),font=("times newn roman",12,"bold"),fg="blue",bg="gold")
        lbl.place(x=150,y=190)
        
        #Check-Out
        lblName=Label(self.frame,text="Check Out Date:",font=("times newn roman",12,"bold"),bg="gold")
        lblName.place(x=0,y=210)
          
        lbl=Label(self.frame,text=self.var_Checkout.get(),font=("times newn roman",12,"bold"),fg="blue",bg="gold")
        lbl.place(x=150,y=210)
        
        #Room Number
        lblName=Label(self.frame,text="Room Number:",font=("times newn roman",12,"bold"),bg="gold")
        lblName.place(x=0,y=230)
          
        lbl=Label(self.frame,text=self.var_RoomNo.get(),font=("times newn roman",12,"bold"),fg="blue",bg="gold")
        lbl.place(x=150,y=230)
        
        #Contact Number
        lblName=Label(self.frame,text="Contact Number:",font=("times newn roman",12,"bold"),bg="gold")
        lblName.place(x=0,y=250)
          
        lbl=Label(self.frame,text=self.var_Contact.get(),font=("times newn roman",12,"bold"),fg="blue",bg="gold")
        lbl.place(x=150,y=250)
        
        lbl=Label(self.frame,text="----------------------- Bill --------------------------",font=("times newn roman",12,"bold"),fg="red",bg="gold")
        lbl.place(x=0,y=280)
        
        #Lodging
        lblName=Label(self.frame,text="Lodging Charge: ₹",font=("times newn roman",12,"bold"),bg="gold")
        lblName.place(x=0,y=300)
          
        lbl=Label(self.frame,text=self.var_StayCharge.get(),font=("times newn roman",12,"bold"),fg="red",bg="gold")
        lbl.place(x=150,y=300)
        
        #Food
        lblName=Label(self.frame,text="Meal Charge: ₹",font=("times newn roman",12,"bold"),bg="gold")
        lblName.place(x=0,y=320)
          
        lbl=Label(self.frame,text=self.var_TotMealCharge.get(),font=("times newn roman",12,"bold"),fg="red",bg="gold")
        lbl.place(x=150,y=320)
        
        #Subtotal
        lblName=Label(self.frame,text="Subtotal: ₹",font=("times newn roman",12,"bold"),bg="gold")
        lblName.place(x=0,y=340)
          
        lbl=Label(self.frame,text=self.var_Subtotal.get(),font=("times newn roman",12,"bold"),fg="red",bg="gold")
        lbl.place(x=150,y=340)
        
        #Tax
        lblName=Label(self.frame,text="Tax(CGST+SGST): ₹",font=("times newn roman",12,"bold"),bg="gold")
        lblName.place(x=0,y=360)
          
        lbl=Label(self.frame,text=self.var_Tax.get(),font=("times newn roman",12,"bold"),fg="red",bg="gold")
        lbl.place(x=150,y=360)
        
        #Total
        lblName=Label(self.frame,text="Total Bill: ₹",font=("times newn roman",12,"bold"),bg="gold")
        lblName.place(x=0,y=380)
          
        lbl=Label(self.frame,text=self.var_TotalBill.get(),font=("times newn roman",12,"bold"),fg="red",bg="gold")
        lbl.place(x=150,y=380)
             
    ################################# Reset Function ########################################## 
    def reset(self): 
        self.var_Contact.set("")
        self.var_RoomNo.set("")
        self.var_CustName.set("")
        self.var_Checkin.set("")
        self.var_Checkout.set("")
        self.var_NumberOfDays.set("")
        self.var_RoomType.set("")
        self.var_RoomCharge.set("")
        self.var_MealPlan.set("")
        self.var_MealHeads.set("")
        self.var_MealCharge.set("")
        self.labelframeBill.destroy() 
        self.frame.destroy()
        self.lblimg1.destroy()
         

######################### Main function //DRIVER CODE ##########################     
if __name__== "__main__":
    root=Tk()
    obj=Billing_Data(root)
    root.mainloop()