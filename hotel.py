from tkinter import*
from PIL import Image,ImageTk
from Customer import Cust_win
from Room import Room_booking
from Details import Details_Room
from bill import Billing_Data
from time import strftime
import datetime as dt


class HotelManagementSystem:
    def __init__(self,root): 
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
       

        ###### 1st iamge ########
        img1=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\hotel2.jpg")
        img1=img1.resize((1550,140), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1, bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        ##### Logo #######
        img2=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\logo.png")
        img2=img2.resize((260,160), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2, bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
        
        #################### Title ################
        self.lbl_title=Label(self.root,text="HOTEL  MANAGEMENT  SYSTEM", font=("algerian",40),bg="gold",fg="black",bd=4,relief=RIDGE)
        self.lbl_title.place(x=0,y=140,width=1550,height=50)
        self.time()
        
        ############################ Date #####################
        date=dt.datetime.now()
        labeldate = Label(self.lbl_title, text=f"{date:%A, %B %d, %Y}", font=("typewriter",10,"bold"),bg="gold",fg="blue",anchor=W)
        labeldate.place(x=5,y=20)

        ############### Frame ####################
        main_frame=Frame(self.root, bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        ################# Menu ###################
        lbl_menu=Label(main_frame,text="ADMIN MENU", font=("times new roman",20,"bold"),bg="black",fg="red",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        
        ############### Button Frame ####################
        btn_frame=Frame(main_frame, bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
        
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="BOOKING",command=self.booking_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="BILL",width=22,command=self.billing_details,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
        
        ###################### Right side Image ###############
        img3=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\hotel3.jpg")
        img3=img3.resize((1330,590), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg1=Label(main_frame,image=self.photoimg3, bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1330,height=590)
        
        ###################### Down Images #####################
        img4=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\Food.jpg")
        img4=img4.resize((225,280), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lblimg1=Label(main_frame,image=self.photoimg4, bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=222,width=228,height=280)
        
        ######################### Self credit ######################
        lbl_credit=Label(main_frame,text="Created by:-\n MAYANK  JHA", font=("Monotype Corsiva",15,"bold"),bg="black",fg="red",bd=4,relief=SUNKEN)
        lbl_credit.place(x=0,y=390,width=230,height=160)
     
     
#################### Window Routing Functions ####################   
    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_win(self.new_window)
        
    def booking_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_booking(self.new_window)
        
    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = Details_Room(self.new_window)  
        
    def billing_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Billing_Data(self.new_window) 
        
    #------------------TIME--------------#
    def time(self):
        self.time1=strftime('%H:%M:%S %p')
        lbltime = Label(self.lbl_title, font=( 'typewriter' ,10, 'bold' ),text=self.time1,bg="gold",fg="blue",anchor=W)
        lbltime.place(x=5,y=0)
        lbltime.after(1000,self.time)  
        
############################ Logout Function #############################################    
    def logout(self):
        self.root.destroy()  
        
######################### Main function // DRIVER CODE ########################## 
 
if __name__== "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()