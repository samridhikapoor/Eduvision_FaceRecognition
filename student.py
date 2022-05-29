from distutils.command.bdist import bdist
from multiprocessing import parent_process
from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_std_id=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        


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

        title_lbl=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"), bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530, height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1500,height=700)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="",font=("times new roman",12,"bold"),bg="white")
        Left_frame.place(x=10,y=10,width=770,height=680)

        img_left=Image.open(r"FlexStart\assets\img\course_details.png")
        img_left=img_left.resize((700,100), Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=45,y=80,width=650,height=100)


        #current course
        current_course_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="white")
        current_course_frame.place(x=10,y=135,width=720,height=150)


        #department
        dep_label=Label(current_course_frame, text="Department", font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0, column=0, padx=2, pady=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dep,font=("times new roman",12,"bold"), width=25  , state="readonly")
        dep_combo["values"]=("Select Department", "Computer", "Information Technology", "Civil", "Mechnaical", "Electrical", "Electronics and Communication", "Biotechnology")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2,pady=10, sticky=W)

        #course
        course_label=Label(current_course_frame, text="Course",font=("times new roman",12,"bold"), bg="white")
        course_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=25  , state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=25  , state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=25  , state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student info
        class_Student_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=300,width=720,height=377)

        #studentId
        studentId_label=Label(class_Student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,stick=W) 

        #student name
        studentName_label=Label(class_Student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)  

        studentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,stick=W)

        #class division
        class_div_label=Label(class_Student_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)  

        class_div_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_div,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,stick=W)
        
        #roll no
        roll_no_label=Label(class_Student_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)  

        roll_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,stick=W)

        #gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)  

       

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18  , state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)  

        dob_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,stick=W)

        #email
        email_label=Label(class_Student_frame,text="E-mail:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)  

        email_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,stick=W)

        #phoneno
        phoneno_label=Label(class_Student_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        phoneno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)  

        phoneno_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phoneno_entry.grid(row=3,column=3,padx=10,pady=5,stick=W)

        #address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)  

        address_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,stick=W)

        #Teacher name
        teacher_label=Label(class_Student_frame,text="Teacher Nane:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)  

        teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,stick=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take a photo sample", value="Yes")
        radiobtn1.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio2,text="No photo sample", value="No")
        radiobtn2.grid(row=6,column=1)

        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=715,height=70)

        save_btn=Button(btn_frame,text="Save Data",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update Data",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete Data",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset Data",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=39,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=39,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        update_photo_btn.grid(row=0,column=1)


        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",width=750,height=680,relief=RIDGE,text="",font=("times new roman",12,"bold"))
        Right_frame.place(x=720,y=10)

        img_right=Image.open(r"FlexStart\assets\img\search_system.png")
        img_right=img_right.resize((700,100), Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=20,y=10,width=720,height=100)

        #search system
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),)
        Search_frame.place(x=5,y=135,width=735,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)  

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=15, state="readonly")
        search_combo["values"]=("Select","Roll No","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,stick=W)

        search_btn=Button(Search_frame,text="Search",width=19,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        search_btn.grid(row=0,column=3)

        resetshowAll_btn=Button(Search_frame,text="Show All",width=19,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        resetshowAll_btn.grid(row=0,column=4)

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("id","dep","course","year","sem","name","div","dob","email","phone","address","teacher","roll","gender","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("id",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


#function
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user="engage2022", password="Useme@123", host="engage2022.mysql.database.azure.com", port=3306, database="face_recognizer", ssl_disabled=True)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_std_id.get(),self.var_dep.get(),self.var_course.get(),
                self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),
                self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Students details have been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    ##fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(user="engage2022", password="Useme@123", host="engage2022.mysql.database.azure.com", port=3306, database="face_recognizer", ssl_disabled=True)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 


    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]


        self.var_std_id.set(data[0])
        self.var_dep.set(data[1])
        self.var_course.set(data[2])
        self.var_year.set(data[3])
        self.var_semester.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update this data?",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(user="engage2022", password="Useme@123", host="engage2022.mysql.database.azure.com", port=3306, database="face_recognizer", ssl_disabled=True)
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(
                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                    self.var_std_id.get(),
                                                                                                                                                                 ))
                 
                 
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()                                                                                                                                            
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

                   
    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete the details of this student?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(user="engage2022", password="Useme@123", host="engage2022.mysql.database.azure.com", port=3306, database="face_recognizer", ssl_disabled=True)
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                     if not delete:
                         return

                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully deleted the details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  
            
    
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#generate data
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user="engage2022", password="Useme@123", host="engage2022.mysql.database.azure.com", port=3306, database="face_recognizer", ssl_disabled=True)
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(
                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                    self.var_std_id.get()==id+1
                                                                                                                                                                 ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                ##load predefined face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    try:
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    except Exception as e:
                        print(e)

                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result"," Dataset Generated successfully")

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                

        

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()