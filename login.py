from statistics import median
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

from tkinter import*
from tkinter import ttk
from tkinter import font
import os
import tkinter
from PIL import Image, ImageTk
from developer import Developer
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from help import Help

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        img=Image.open(r"FlexStart\assets\img\bg.jpg")
        img=img.resize((10000,10000), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=10000,height=10000)

        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"FlexStart\assets\img\login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photimage1,bg="white",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started", font=("times new roman",20,"bold"),fg="dark blue",bg="white")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",20,"bold"),fg="dark blue",bg="white")
        username.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=200,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="dark blue",bg="white")
        password.place(x=40,y=250)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=290,width=270)

        #icon
        img2=Image.open(r"FlexStart\assets\img\login.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photimage2,bg="white",borderwidth=0)
        lblimg2.place(x=625,y=333,width=25,height=25)

        img3=Image.open(r"FlexStart\assets\img\lock.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photimage3,bg="white",borderwidth=0)
        lblimg3.place(x=625,y=430,width=25,height=25)

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="Dark blue")
        loginbtn.place(x=110,y=330,width=120,height=35)

        registerbtn=Button(frame,command=self.register_window,text="New User ? Register",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="dark blue",bg="white")
        registerbtn.place(x=10,y=375,width=160)

        passwordbtn=Button(frame,command=self.forgot_password_window,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="dark blue",bg="white")
        passwordbtn.place(x=10,y=400,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerrer("Error","All fields are required")
        elif self.txtuser.get()=="engage" and self.txtpass.get()=="12345":
            messagebox.showinfo("Success","Welcome to Attendance system")

        else:
            conn = mysql.connector.connect(user="engage2022", password="Useme@123", host="engage2022.mysql.database.azure.com", port=3306, database="face_recognizer", ssl_disabled=True)
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                        ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("Query","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select a Security question",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter a new password",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer to the security question",parent=self.root2)
        else:
            conn = mysql.connector.connect(user="engage2022", password="Useme@123", host="engage2022.mysql.database.azure.com", port=3306, database="face_recognizer", ssl_disabled=True)
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer to the security question",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Information","Your password has been reset. Please Login with the new password",parent=self.root2)
                self.root2.destroy()



##forgot password window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(user="engage2022", password="Useme@123", host="engage2022.mysql.database.azure.com", port=3306, database="face_recognizer", ssl_disabled=True)
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please enter a valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="dark blue",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=110)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your father's name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="dark blue")
                btn.place(x=100,y=290)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        img=Image.open(r"FlexStart\assets\img\bg.jpg")
        img=img.resize((10000,10000), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=10000,height=10000)

        frame=Frame(self.root,bg="white")
        frame.place(x=400,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark blue",bg="white")
        register_lbl.place(x=20,y=20)

        #row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        #row2
        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        #row3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your father's name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        #row4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #checkbutton
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree to the Terms and Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #button
        img=Image.open(r"FlexStart\assets\img\register.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        b1.place(x=10,y=420,width=300)

        img1=Image.open(r"FlexStart\assets\img\loginb.png")
        img1=img1.resize((200,43),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        b1.place(x=330,y=420,width=300)

    #functions
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to the terms and conditions to proceed")
        else:
            conn = mysql.connector.connect(user="engage2022", password="Useme@123", host="engage2022.mysql.database.azure.com", port=3306, database="face_recognizer", ssl_disabled=True)
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email is already registered. Please use another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get(),
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registeration Successful")

    def return_login(self):
        self.root.destroy()


class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"FlexStart\assets\img\bg.jpg")
        img=img.resize((10000,10000), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=10000,height=10000)

        img2=Image.open(r"FlexStart\assets\img\bg.jpg")
        img2=img2.resize((10000,10000), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_img=Label(self.root, image=self.photoimg2)
        bg_img.place(x=0,y=0,width=10000,height=10000)

        title_lbl=Label(bg_img, text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",35,"bold"), bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530, height=45)

        img1=Image.open(r"FlexStart\assets\img\attendance.jpg")
        img1=img1.resize((220,220), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.photoimg1,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student details",command=self.student_details,cursor="hand2", font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face
        img5=Image.open(r"FlexStart\assets\img\face_recognition.jpg")
        img5=img5.resize((220,220), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #attendance 
        img6=Image.open(r"FlexStart\assets\img\att_home.jfif")
        img6=img6.resize((220,220), Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6, cursor="hand2",command=self.attendance)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance", cursor="hand2",command=self.attendance, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #helpdesk
        img7=Image.open(r"FlexStart\assets\img\helpdesk.jfif")
        img7=img7.resize((220,220), Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk", cursor="hand2",command=self.help_data, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #train face detector
        img8=Image.open(r"FlexStart\assets\img\trainmodel.jfif")
        img8=img8.resize((220,220), Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Train the Model", cursor="hand2",command=self.train_data, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)

        #photos face button
        img9=Image.open(r"FlexStart\assets\img\camera.jfif")
        img9=img9.resize((220,220), Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Captured Photos",command=self.open_img, cursor="hand2", font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40)

        #developers page button
        img10=Image.open(r"FlexStart\assets\img\developers.jfif")
        img10=img10.resize((220,220), Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="About FACEIPHY", cursor="hand2",command=self.developer_data, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)

        #exit page button
        img11=Image.open(r"FlexStart\assets\img\exit.jfif")
        img11=img11.resize((220,220), Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11, cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit the Application", cursor="hand2",command=self.iExit, font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    #functions

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit the Application?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return





if __name__ == "__main__":
    main()