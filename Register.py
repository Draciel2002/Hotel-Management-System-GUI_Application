from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("REGISTER")
        self.root.geometry("1550x800+0+0")
        
        ###################### Variables ###################
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_SecurityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_Pass=StringVar()
        self.var_confPass=StringVar()
        
        ####################################### Background Image ####################################
        img1=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\hotel5.jpg")
        img1=img1.resize((1550,690), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1, bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=690)
        
        ############################# Main frame ############################
        frame=Frame(self.root,bg="black")
        frame.place(x=300,y=120,width=800,height=500)
        
         ####################################### Left Logo Image ####################################
        img2=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\logo.png")
        img2=img2.resize((150,130), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(frame,image=self.photoimg2, bd=2,relief=RIDGE)
        lblimg.place(x=5,y=5,width=150,height=130)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("Arial MT Bold",25,"bold"),fg="Red", bg="black")
        register_lbl.place(x=300,y=10)
        
        ########################## Labels and entry fields ######################3
        #row1
        fname=Label(frame,text="First Name : ",font=("Book Antiqua",15,"bold"),fg="White", bg="black")
        fname.place(x=160,y=80)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Cambria",12))
        fname_entry.place(x=280,y=85,width=200)
        
        lname=Label(frame,text="Last Name : ",font=("Book Antiqua",15,"bold"),fg="White", bg="black")
        lname.place(x=490,y=80)
        
        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("Cambria",12))
        lname_entry.place(x=605,y=85,width=180)
        
        #row2
        Contact=Label(frame,text="Contact Number : ",font=("Book Antiqua",15,"bold"),fg="White", bg="black")
        Contact.place(x=20,y=150)
        
        Contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("Cambria",12))
        Contact_entry.place(x=190,y=155,width=200)
        
        Email=Label(frame,text="Email : ",font=("Book Antiqua",15,"bold"),fg="White", bg="black")
        Email.place(x=410,y=150)
        
        Email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("Cambria",12))
        Email_entry.place(x=480,y=155,width=300)
        
        #row3
        Sq=Label(frame,text=" Select Security Question ",font=("Book Antiqua",15,"bold"),fg="White", bg="black")
        Sq.place(x=20,y=200)
      
        self.combo_security=ttk.Combobox(frame,textvariable=self.var_SecurityQ,font=("Cambria",12),state="readonly")
        self.combo_security["values"]=("Select","Your Birthplace","Your Pet Name","Your Nickname")
        self.combo_security.place(x=20,y=230,width=300)
        self.combo_security.current(0)
        
        Sa=Label(frame,text="Security Answer",font=("Book Antiqua",15,"bold"),fg="White", bg="black")
        Sa.place(x=480,y=200)
        
        Sa_entry=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("Cambria",12))
        Sa_entry.place(x=480,y=230,width=300)
        
        #row4
        Pass=Label(frame,text="Password",font=("Book Antiqua",15,"bold"),fg="White", bg="black")
        Pass.place(x=20,y=270)
        
        Pass_entry=ttk.Entry(frame,textvariable=self.var_Pass,font=("Cambria",12))
        Pass_entry.place(x=20,y=300,width=300)
        
        CPass=Label(frame,text="Confirm Password",font=("Book Antiqua",15,"bold"),fg="White", bg="black")
        CPass.place(x=480,y=270)
        
        CPass_entry=ttk.Entry(frame,textvariable=self.var_confPass,font=("Cambria",12))
        CPass_entry.place(x=480,y=300,width=300)
        
        ################################# Check Button ##############################
        self.var_check=IntVar()
        self.check_btn=Checkbutton(frame,variable=self.var_check,text="I agree to above given details to be right.",font=("Calibri",12),onvalue=1,offvalue=0,fg="black",bg="white",activeforeground="white",activebackground="black")
        self.check_btn.place(x=20,y=340)
        
        ######################## Buttons ##########################
        img5=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\Submit.jpeg")
        img5=img5.resize((140,40),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img5)
        b1=Button(frame,command=self.register_data,image=self.photoimg3,borderwidth=0,cursor="hand2",bg="black",activebackground="black")
        b1.place(x=10,y=420,width=300)
        
        img6=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\Login button.png")
        img6=img6.resize((140,40),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img6)
        b1=Button(frame,image=self.photoimg4,borderwidth=0,cursor="hand2",bg="black",activebackground="black")
        b1.place(x=500,y=420,width=300)
        
        
    ########################################## Function Declaration #############################################
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_SecurityQ.get()=="Select" or self.var_SecurityA.get()=="" or self.var_Pass.get()=="" or self.var_confPass.get()=="":
            messagebox.showerror("!! ERROR !!","All Fields are Required")
        elif self.var_Pass.get()!=self.var_confPass.get():
             messagebox.showerror("!! ERROR !!","Password and Confirm password must be same.")
        elif self.var_check.get()==0:
            messagebox.showerror("!! ERROR !!","Please Click on Agree to the above details")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email =%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("!! ERROR !!","User Already Exists, Please try another Email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_fname.get(),
                                                                                self.var_lname.get(),
                                                                                self.var_contact.get(),
                                                                                self.var_email.get(),
                                                                                self.var_SecurityQ.get(),
                                                                                self.var_SecurityA.get(),
                                                                                self.var_Pass.get()           
                                                                                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("!! SUCCESS !!","Registered Sucessfully. Please Login with Email as Username",parent=self.root)
            
               
        
############################################# Main/Driver Code #############################
           
if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()