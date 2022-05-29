from distutils.command.bdist import bdist
from multiprocessing import parent_process
from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from sqlalchemy import column
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        img=Image.open(r"FlexStart\assets\img\bg.jpg")
        img=img.resize((10000,10000), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=10000,height=10000)

        title_lbl=Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"), bg="white",fg="dark blue")
        title_lbl.place(x=0,y=20,width=1530, height=50)

        # img_top=Image.open(r"FlexStart\assets\img\face_recognition.webp")
        # img_top=img_top.resize((900,500), Image.ANTIALIAS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top)

        # f_lbl=Label(self.root, image=self.photoimg_top,bg="light blue")
        # f_lbl.place(x=350,y=170,width=900,height=500)

        main_frame=Frame(f_lbl,bd=2,bg="light blue")
        main_frame.place(x=10,y=55,width=1500,height=700)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"),bg="white")
        Left_frame.place(x=10,y=20,width=770,height=700)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=22,width=695,height=600)

        attendanceId_label=Label(left_inside_frame,text="Attendance ID",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,stick=W) 

        rollLabel_label=Label(left_inside_frame,text="Roll ID:",font=("times new roman",12,"bold"),bg="white")
        rollLabel_label.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=8) 

        nameLabel=Label(left_inside_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,pady=8) 

        depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)

        timeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,pady=8)

        dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,pady=8)

        attendanceLabel=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=70)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=19,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=19,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="light blue",fg="dark blue")
        reset_btn.grid(row=0,column=3)

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",text="Attendance Details",width=750,height=680,relief=RIDGE,font=("times new roman",12,"bold"))
        Right_frame.place(x=720,y=20,width=770,height=680)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=22,width=760,height=445)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data has been exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")










if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
