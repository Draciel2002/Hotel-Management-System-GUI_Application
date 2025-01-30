from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")
        
        img1=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\hotel1.jpg")
        img1=img1.resize((1550,690), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1, bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=690)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=150,width=300,height=400)
        
        ############## Frame Logo ########################
        img2=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\logo.png")
        img2=img2.resize((290,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg1=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=500,y=150,width=300,height=140)
        
        get_str=Label(frame,text="LOGIN MENU",font=("Arial MT Bold",20,"bold"),fg="red",bg="black")
        get_str.place(x=70,y=135)
        
        ################Labels and Entry fields #######################
         
        username_lbl=Label(frame,text="Username:  ",font=("Arial MT Bold",12,"bold"),fg="gold",bg="black")
        username_lbl.place(x=2,y=200)
        
        self.txtUser=ttk.Entry(frame,font=("times new roman",12))
        self.txtUser.place(x=120,y=200,width=170)
        
        password_lbl=Label(frame,text="Password:  ",font=("Arial MT Bold",12,"bold"),fg="gold",bg="black")
        password_lbl.place(x=2,y=260)
        
        self.password=ttk.Entry(frame,font=("times new roman",12),show="*")
        self.password.place(x=120,y=260,width=170)
        
        ############# Icon Images ########################
        img3=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\username.jpeg")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg1=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg1.place(x=600,y=350,width=20,height=25)
        
        img4=Image.open(r"C:\Users\MAYANK JHA\OneDrive\Desktop\Python Projects\Hotel Management System\Image\password.png")
        img4=img4.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lblimg1=Label(image=self.photoimg4,bg="black",borderwidth=0)
        lblimg1.place(x=597,y=410,width=25,height=25)
        
        ############## Buttons ##################
        # login
        loginbtn=Button(frame,text="LOGIN",command=self.login,font=("Arial MT Bold",12,"bold"),bd=3,relief=RIDGE,fg="red",bg="gold",activeforeground="red",activebackground="gold")
        loginbtn.place(x=160,y=340,width=120,height=35)
        
        #register
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=0,y=330,width=150)

        #Forget Password
        passbtn=Button(frame,text="Forget Password",command=self.forget_password_win,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        passbtn.place(x=0,y=360,width=150)
    
    
    #Register Function
    def  register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)   
    
    #Login Function
    def login(self):
        if self.txtUser.get()=="" or self.password.get()=="": 
            messagebox.showerror("!! ERROR !!","All Fields Required")        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s",(
                                                                                    self.txtUser.get(),
                                                                                    self.password.get()
                                                                                ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("!! ERROR !!","Invalid Credentials Given")
            else:
                open_main=messagebox.askyesno("VERIFY","Do You want to login as Admin ?")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
    ##################################### Reset password Function ####################
    def reset_pass(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("!! ERROR !!","Select the security question",parent=self.root2)
        elif self.Sa_entry.get()=="":
             messagebox.showerror("!! ERROR !!","Please enter the answer",parent=self.root2)
        elif self.new_password.get()=="":
             messagebox.showerror("!! ERROR !!","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s and SecurityQ=%s and SecurityA=%s")
            value=(self.txtUser.get(),self.combo_security.get(),self.Sa_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                 messagebox.showerror("!! ERROR !!","Please Enter Correct Security Question and Answer",parent=self.root2)
            else:
                query=("update register set Password=%s where email=%s")
                value=(self.new_password.get(),self.txtUser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("!! SUCCESS !!","Your Password has been reset sucessfully. Please Login with the new Password",parent=self.root)
                self.root2.destroy()
            
            
                
        
 
 ########################################## Forget Password Window ################################   
    def forget_password_win(self):
        if self.txtUser.get()=="":
            messagebox.showerror("!! ERROR !!","Please Enter the Email address to reset password") 
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@Akkianmayank2002",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.txtUser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("!! ERROR !!","Please Enter valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+500+170")
                self.root2.configure(bg="black")
                
                lbl1=Label(self.root2,text="RESET PASSWORD",font=("times new roman",25,"bold"),fg="red",bg="black")
                lbl1.place(x=0,y=0,relwidth=1)
                
                Sq=Label(self.root2,text=" Select Security Question ",font=("Book Antiqua",15,"bold"),fg="White", bg="black")
                Sq.place(x=20,y=80)
            
                self.combo_security=ttk.Combobox(self.root2,font=("Cambria",12),state="readonly")
                self.combo_security["values"]=("Select","Your Birthplace","Your Pet Name","Your Nickname")
                self.combo_security.place(x=20,y=110,width=300)
                self.combo_security.current(0)
                
                Sa=Label(self.root2,text="Security Answer",font=("Book Antiqua",15,"bold"),fg="White", bg="black")
                Sa.place(x=20,y=150)
                
                self.Sa_entry=ttk.Entry(self.root2,font=("Cambria",12))
                self.Sa_entry.place(x=20,y=180,width=300)
                
                New_password=Label(self.root2,text="Enter New Password",font=("Book Antiqua",13,"bold"),fg="White", bg="black")
                New_password.place(x=20,y=220)
                
                self.new_password=ttk.Entry(self.root2,font=("Cambria",12))
                self.new_password.place(x=20,y=250,width=300)
                
                btn=Button(self.root2,text="RESET",command=self.reset_pass,font=("Book Antiqua",15,"bold"),fg="red",bg="gold",activebackground="gold",activeforeground="red")
                btn.place(x=130,y=300)
                
                  
       
            
                    
  
  
  
        

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
        b1=Button(frame,image=self.photoimg4,command=self.return_login,borderwidth=0,cursor="hand2",bg="black",activebackground="black")
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
                messagebox.showinfo("!! SUCCESS !!","Registered Sucessfully.",parent=self.root)
    
    def return_login(self):
        self.root.destroy()
                
                     
        
if __name__ == "__main__":
    main()
