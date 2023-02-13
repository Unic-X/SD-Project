import customtkinter,json,os
from PIL import ImageTk,Image
from utils import *
import matplotlib, numpy
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

os.chdir("assets/")

with open("users.json","r+") as file:
    data = json.load(file)

class Users:
    def check_login(self,frame):
        username = frame.uentry.get().strip()
        password = frame.pentry.get().strip()
        if username not in data["users"].keys():
            print(f"No user named {username} found")
        else:
            real_password = data["users"][username]["password"]
            if password == real_password:
                print("Correct login")
                if data["users"][username]["isadmin"] == True:
                    frame.destroy()
                    user=Admin(self.window,username)
                    user.manage_user()
                else:
                    frame.destroy()
                    self.username = username
                    self.home_page(i=0)
            else:
                print("Incorrect login please check password or username")

    def login_page(self):
        self.window = customtkinter.CTk()
        frame = customtkinter.CTkToplevel(self.window)
        frame.geometry("600x440")
        frame.title("Login")
        bg_image = ImageTk.PhotoImage(Image.open("pattern.png"))
        bg = customtkinter.CTkLabel(master=frame,image=bg_image,text="")
        bg.pack()
        frame.l_frame = customtkinter.CTkFrame(master=bg,height=360,width=360,corner_radius=15)
        frame.l_frame.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)
        frame.label_1 = customtkinter.CTkLabel(master=frame.l_frame,text="Login into your account",font=("Century Gothic",20))
        frame.label_1.place(x=70,y=10)
        frame.uentry = customtkinter.CTkEntry(master=frame.l_frame,placeholder_text="Username",width=220)
        frame.uentry.place(relx=0.2,y=125)
        frame.pentry = customtkinter.CTkEntry(master=frame.l_frame,placeholder_text="Password",width=220)
        frame.pentry.place(relx=0.2,y=180)
        frame.l_button = customtkinter.CTkButton(master=frame.l_frame,width=220,text="Login",corner_radius=6,command=lambda : self.check_login(frame))
        frame.l_button.place(relx=0.2,y=250)
        frame.mainloop()

    def home_page(self,i=0):
        #Define window of the page
        self.window.title("Employee Payroll")
        self.window.iconbitmap("deshpremikiryu-modified.ico")
        self.text_font = customtkinter.CTkFont("Proxima Nova Rg",18)
        self.text_font_bold = customtkinter.CTkFont("Proxima Nova Rg",20,"bold")
        self.font = customtkinter.CTkFont("Proxima Nova Rg",12,'bold')
        self.window.geometry("900x600")

        #Define grid inside the window
        self.window.grid_columnconfigure(1,weight=1)
        self.window.grid_rowconfigure(0,weight=1)

        #Add left frame inside the row 0 col 0 cell
        self.l_frame = customtkinter.CTkFrame(master=self.window)
        self.l_frame.grid(row=0,column=0,rowspan=4,padx=20,pady=20,sticky="nsew")

        #Added MANAGE label
        self.window.manage_ = customtkinter.CTkLabel(master=self.l_frame,text="MANAGE",font=self.font)
        self.window.manage_.place(y=30,relx=0.1)

        #Added ATTENDANCE button
        self.window.but_attend = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Attendance",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",image=customtkinter.CTkImage(Image.open("calendar-solid.png")),command=self.attendace)
        self.window.but_attend.place(y=60)

        #Added EMPLOYEE button 
        self.window.but_emp = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Change Password",corner_radius=0,image=customtkinter.CTkImage(Image.open("a.png"),size=(20,20)),fg_color="#333333",hover_color="#2e2e2e",
                              command= self.change_password
                                )
        self.window.but_emp.place(y=100)

        #Added DEDUCTION button
        self.window.but_deduction = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Deduction",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",image=customtkinter.CTkImage(Image.open("documents-solid.png")))
        self.window.but_deduction.place(y=140)

        #Added Printables label
        self.window.printables = customtkinter.CTkLabel(master=self.l_frame,text="PRINTABLES",font=self.font)
        self.window.printables.place(y=185,relx=0.1)

        #Added PAYROLL button
        self.window.but_payroll = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Payroll   ",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",image=customtkinter.CTkImage(Image.open("coins-solid.png")))
        self.window.but_payroll.place(y=215)

        #Added SCHEDULE button
        #self.window.but_schedule = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Schedule",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",image=customtkinter.CTkImage(Image.open("clock-solid.png")))
        #self.window.but_schedule.place(y=255)

        #Added Home page button
        if i==0:
            self.window.home_page = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Home Page",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",command=self.home_page)
            self.window.home_page.place(y=295)
        else:
            self.window.home_page = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Home Page",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",command=lambda : self.home_page(1))
            self.window.home_page.place(y=295)

        #Added right frame 
        self.r_frame = customtkinter.CTkFrame(master=self.window)
        self.r_frame.grid(row=0,column=1,rowspan=4,padx=20,pady=20,sticky="nsew")

        if i==1:
            manage = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="samaj",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",command=self.manage_user)
            manage.place(y=400)

        #Added dashboard label inside right frame
        self.dashboard = customtkinter.CTkLabel(master=self.r_frame,text="Dashboard")
        self.dashboard.configure(padx=20,font=self.text_font_bold)

        #Grid inside right frame with 3 coloumns and 3 rows
        self.r_frame.grid_columnconfigure((0,1,2,3),weight=1)
        self.r_frame.grid_rowconfigure((1,2,3),weight=1)

        #Place dashboard label to the (0,0) of right frame
        self.dashboard.grid(row=0,column=0,padx=7.5,pady=20,sticky="nw")

        #Add total_working_employee frame
        total_employee = customtkinter.CTkFrame(master=self.r_frame,fg_color="#6c7f91",corner_radius=0)
        total_employee.grid(row=1,column=0,sticky="new",padx=20)

        #Details
        total_employee_ = customtkinter.CTkLabel(master=total_employee,text="Total Employees",font=self.text_font)
        total_employee_.place(relx=0.1,rely=0.25)
        users = len(data["users"])
        total_employee_label = customtkinter.CTkLabel(master=total_employee,text=f"{users}",font=self.text_font_bold)
        total_employee_label.place(relx=0.1,rely=0.1)

        #Add attendance percentage frame 
        percentage = customtkinter.CTkFrame(master=self.r_frame,fg_color="#019258",corner_radius=0)
        percentage.grid(row=1,column=1,sticky="new")

        #Details
        percentage_label = customtkinter.CTkLabel(master=percentage,text=f"{total_attendace(data,self.username)}",font=self.text_font_bold)
        percentage_label.place(relx=0.1,rely=0.1)
        percentage_label_ = customtkinter.CTkLabel(master=percentage,text="Attendance %",font=self.text_font)
        percentage_label_.place(relx=0.1,rely=0.25)

        #Add current time frame
        time = customtkinter.CTkFrame(master=self.r_frame,fg_color="#fd9c0a",corner_radius=0)
        time.grid(row=1,column=2,sticky="new",padx=20)

        #Details
        time_label = customtkinter.CTkLabel(master=time,text="",font=self.text_font_bold)
        time_label.place(relx=0.1,rely=0.1)
        update_time(time_label)
        current_time_label = customtkinter.CTkLabel(master=time,text="Current Time",font=self.text_font)
        current_time_label.place(relx=0.1,rely=0.25)

        basic = int(data["users"][self.username]["basic"])
        taxable = basic+basic*0.792
        net_pay = (basic+basic*0.792)-(taxable*0.3+basic*0.06)
        print(net_pay)
        #Late Frame Right most
        total_pay_f = customtkinter.CTkFrame(master=self.r_frame,fg_color="#e85832",corner_radius=0)
        total_pay_f.grid(row=1,column=3,sticky="new")


        total_pay = customtkinter.CTkLabel(master=total_pay_f,text=f"₹{net_pay}",font=self.text_font_bold)
        total_pay.place(relx=0.1,rely=0.1)
        total_pay_ = customtkinter.CTkLabel(master=total_pay_f,text="Monthly Total Pay",font=self.text_font)
        total_pay_.place(relx=0.1,rely=0.25)

        details = customtkinter.CTkFrame(master=self.r_frame)
        details.grid(row=2,column=0,sticky="nsew",rowspan=4,columnspan=4)

        name_account = customtkinter.CTkLabel(details,width=2000,bg_color="#474545",text="Name: {}     Account Number:{}".format(data["users"][self.username]["name"],data["users"][self.username]["acc"]),anchor="w",font=self.text_font)
        name_account.place(x=0,y=40)
        name_account.configure(padx=40)

        total_deduction = customtkinter.CTkLabel(details,font=self.text_font,text="Total Monthly Deduction: {}      Basic Pay: {}".format(taxable*0.3+basic*0.06,basic),anchor="w")
        total_deduction.place(x=0,y=100)
        total_deduction.configure(padx=40)

        total_allowance = customtkinter.CTkLabel(details,font=self.text_font,text="Total Monthly Allowance(Including DA): {}      Perks: {}".format(basic*0.38,basic*0.412),anchor="w")
        total_allowance.place(x=0,y=140)
        total_allowance.configure(padx=40)

        if i==0:
            self.window.mainloop()

    def attendace(self):
        self.r_frame.destroy()

        #Create a new window with the same name
        
        self.r_frame = customtkinter.CTkFrame(master=self.window)
        self.r_frame.grid(row=0,column=1,rowspan=4,padx=20,pady=20,sticky="nsew")

        self.r_frame.grid_columnconfigure((0,1,2,3),weight=1)
        self.r_frame.grid_rowconfigure(1,weight=1)

        attendance = customtkinter.CTkLabel(master=self.r_frame,text="Attendance")
        attendance.configure(padx=20,font=self.text_font_bold)
        attendance.grid(row=0,column=0,padx=7.5,pady=20,sticky="nw")

        attendance_graph = customtkinter.CTkFrame(master=self.r_frame)
        
        attendance_graph.grid(row=1,column=0,padx=7.5,pady=20,sticky="nsew",columnspan=4) 

        f = Figure(figsize=(10,20), dpi=100,facecolor="#2a2b2a",)
        ax = f.add_subplot(111)
        ax.set_facecolor("orange")
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.xaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='y', colors='white')
        print(tuple(data["users"][self.username]["attendance"]))
        data_ = tuple(data["users"][self.username]["attendance"])
        ind = numpy.arange(len(data_))  # the x locations for the groups
        width = .75
        ax.set_xticklabels(["January", "February", 'March', "April", "May", 'June', "July", "August", "September", "October", 'November' , "December"])
        rects1 = ax.bar(ind, data_, width)

        canvas = FigureCanvasTkAgg(f, master=attendance_graph)
        canvas.draw()
        
        canvas.get_tk_widget().pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=1)

    def change_password(self):
        print(self.username)
        print(data["users"][self.username]["password"])
        #UI Element
        self.top_level = customtkinter.CTkToplevel()
        self.top_level.title("Change Password")
        image = ImageTk.PhotoImage(Image.open("alo.png"))
        bg = customtkinter.CTkLabel(master=self.top_level,image=image,text="")
        bg.pack()
        self.top_level.geometry("600x440") 

        self.top_l_frame = customtkinter.CTkFrame(master=self.top_level,height=360,width=360,corner_radius=15)
        self.top_l_frame .place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)

        label_1 = customtkinter.CTkLabel(master=self.top_l_frame ,text="Change Password",font=("Century Gothic",20))
        label_1.place(x=70,y=10)

        current_password_label = customtkinter.CTkLabel(master=self.top_l_frame ,text="Current Password")
        current_password_label.place(relx=0.2,y=70)

        uentry = customtkinter.CTkEntry(master=self.top_l_frame ,placeholder_text="",width=220)
        uentry.place(relx=0.2,y=105)

        new_password_label = customtkinter.CTkLabel(master=self.top_l_frame ,text="New Password")
        new_password_label.place(relx=0.2,y=145)

        new_password = customtkinter.CTkEntry(master=self.top_l_frame ,placeholder_text="",width=220)
        new_password.place(relx=0.2,y=180)   
        
        confirm_password_label = customtkinter.CTkLabel(master=self.top_l_frame ,text="Confirm Password")
        confirm_password_label.place(relx=0.2,y=220)

        confirm_password = customtkinter.CTkEntry(master=self.top_l_frame ,placeholder_text="",width=220)
        confirm_password.place(relx=0.2,y=255) 

        l_button = customtkinter.CTkButton(master=self.top_l_frame ,width=220,text="Change Password",corner_radius=6,command=lambda : self.check_entered_pass(uentry,new_password,confirm_password))
        l_button.place(relx=0.2,y=300)
        
        
        #Check if current password is right
    def check_entered_pass(self,uentry,uentry2,uentry3):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
        match_password = re.match(pattern, uentry2.get())
        print(uentry2.get()==uentry3.get())
        print(match_password!=None)
        print(data["users"][self.username]["password"].strip() == uentry.get().strip())
        if (data["users"][self.username]["password"] == uentry.get().strip()) and (match_password!=None) and (uentry2.get()==uentry3.get()):
            print("hi")
            self.top_l_frame.destroy()
            self.top_l_frame2 = customtkinter.CTkFrame(master=self.top_level,height=360,width=360,corner_radius=15)
            self.top_l_frame2.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)
            valid_pass = customtkinter.CTkLabel(master=self.top_l_frame2,text="Password changed",text_color="Green",font=("Century Gothic",20))
            password_changed_image = customtkinter.CTkImage(Image.open("checkmark.png"),size=(60,60))
            image_frame = customtkinter.CTkLabel(master=self.top_l_frame2,image=password_changed_image,text="")
            image_frame.place(relx=0.4,rely=0.5)
            valid_pass.place(relx=0.25,rely=0.3)
        else:
            ...
class Admin(Users):
    def __init__(self,window,username):
        self.window = window
        self.username = username
        super().__init__()

    def manage_user(self):
        font = customtkinter.CTkFont("Proxima Nova Rg",18,'bold')
        text_font = customtkinter.CTkFont("Proxima Nova Rg",18)
        text_font_bold = customtkinter.CTkFont("Proxima Nova Rg",20,"bold")

        self.home_page(1)
        manage = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="samaj",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",command=self.manage_user)
        manage.place(y=400)
        self.window.home_page.configure(text="Home Page", command = lambda: self.home_page(1))
        self.r_frame.destroy()
        self.r_frame = customtkinter.CTkFrame(master=self.window)
        self.r_frame.grid(row=0,column=1,rowspan=4,padx=20,pady=20,sticky="nsew")
        self.r_frame.grid_columnconfigure((0,1,2,3),weight=1)
        self.r_frame.grid_rowconfigure(1,weight=1)
        manage_users_frame = customtkinter.CTkFrame(master=self.r_frame)
        manage_users_frame.grid(row=1,column=0,padx=7.5,pady=10,sticky="nsew",columnspan=4)
        manage_user_label = customtkinter.CTkLabel(master=self.r_frame,text="Manage Users")
        manage_user_label.configure(padx=20,font=self.text_font_bold)
        manage_user_label.grid(row=0,column=0,padx=7.5,pady=10,sticky="nw")
        
        def option_callback2(choice):
            if choice=="1" and int(current_basic.cget("text"))<10000:
                change_basic.configure(textvariable=10000)


        def option_callback(choice):
            username = data["users"][choice]["name"]
            account_number = data["users"][choice]["acc"]
            basic = data["users"][choice]["basic"]
            employee_id.configure(text=f"Employee Name: {username}      Account Number: {account_number}")
            current_basic.configure(text=basic)
            calculated_da.configure(text=basic*0.38)
            company_allowance.configure(text=basic*0.16)
            perks.configure(text=basic*0.252)
            taxable = basic+basic*0.792
            total_tax = taxable*0.3
            itax.configure(text=total_tax)
            cpf.configure(text=basic*0.06)
            deductions.configure(text=taxable*0.3+basic*0.06)
            gross_pay_total = basic+basic*0.792
            gross_pay.configure(text=gross_pay_total)
            net_salary.configure(text=(basic+basic*0.792)-(taxable*0.3+basic*0.06))
        #SELECT USER 
        select_user = customtkinter.CTkLabel(master=manage_users_frame,text="Select Employee:",font=text_font)
        select_user.place(x=30,y=20)
        list_users = customtkinter.CTkOptionMenu(master=manage_users_frame,font=text_font_bold,
                                                    values=[username for username in data["users"].keys()],command=option_callback)

        list_users.place(x=30,y=50)

        def save_changes():
            employeeid = list_users.get()
            new_basic = int(change_basic.get())
            data["users"][employeeid]["basic"]=new_basic
            with open("users.json","w") as file:
                json.dump(data,file,indent=4)
            option_callback(employeeid)

        def confirmation_window():

            new_window = customtkinter.CTkToplevel()

            new_window.title("Confirm Changes")
            new_window.geometry("400x240")
            new_window.protocol("WM_DELETE_WINDOW", lambda: ...)


            new_window.resizable(width=False,height=False)
            warning_label = customtkinter.CTkLabel(master=new_window,text="Changes are being finalized \n please confirm the changes to continue",height=40)
            warning_label.place(relx=0.22,rely=0.25)
            cancel_changes = customtkinter.CTkButton(master=new_window,text="Cancel Changes",command=lambda :new_window.destroy())
            accept_changes = customtkinter.CTkButton(master=new_window,text="Accept Changes",command=save_changes)
            cancel_changes.place(relx=0.15,rely=0.5)
            accept_changes.place(relx=0.55,rely=0.5)


        #ACC NUMBER
        employee_id = customtkinter.CTkLabel(master=manage_users_frame,text=f"Employee Name: {0}    Account Number: {0}"
                                            ,font=text_font,bg_color="#474545",anchor="w",width=2000,height=40)
        employee_id.place(x=0,y=90)
        employee_id.configure(padx=40)

        #CHANGE GRADE SCALE
        
        change_grade = customtkinter.CTkLabel(master=manage_users_frame,text="Change Grade Scale:",font=text_font)
        grade_list = customtkinter.CTkOptionMenu(master=manage_users_frame,font=text_font_bold,values=["3","2","1"],width=80,command=option_callback2)
        grade_list.place(x=30,y=170)
        change_grade.place(x=30,y=140)
        
        #CHANGE BASIC PAY
        change_basic_label = customtkinter.CTkLabel(master=manage_users_frame,text="Basic:",font=text_font)
        change_basic = customtkinter.CTkEntry(master=manage_users_frame,font=text_font,placeholder_text="Change Basic Pay",width=120)
        change_basic_label.place(x=225,y=140)
        change_basic.place(x=225,y=170)
        current_basic_label = customtkinter.CTkLabel(master=manage_users_frame,text="Current Basic:",font=text_font)
        current_basic_label.place(x=350,y=140)
        basic = data["users"][self.username]
        print(basic)
        current_basic = customtkinter.CTkLabel(master=manage_users_frame,text="0000",font=text_font,bg_color="#202120",corner_radius=20)
        current_basic.place(x=460,y=140)
        #CALCULATED DA
        da_label = customtkinter.CTkLabel(master=manage_users_frame,text="DA:",font=text_font)
        da_label.place(x=30,y=215)
        calculated_da = customtkinter.CTkButton(master=manage_users_frame,text="0000",font=text_font,state="disabled",width=100)
        calculated_da.place(x=65,y=215)
        
        #COMPANY ALLOWANCE
        company_allowance_label = customtkinter.CTkLabel(master=manage_users_frame,text="CAllowance:",font=text_font)
        company_allowance_label.place(x=180,y=215)
        company_allowance = customtkinter.CTkLabel(master=manage_users_frame,text="0",font=font)
        company_allowance.place(x=280,y=215)

        #PERKS
        perks_label = customtkinter.CTkLabel(master=manage_users_frame,text="Perks:",font=text_font)
        perks_label.place(x=400,y=215)
        perks= customtkinter.CTkLabel(master=manage_users_frame,text="0",font=font)
        perks.place(x=450,y=215)

        #DEDUCTIONS
        deductions = customtkinter.CTkLabel(master=manage_users_frame,text=f"Calculated Deductions"
                                            ,font=text_font,bg_color="#474545",anchor="w",width=2000,height=40)
        deductions.place(x=0,y=260)
        deductions.configure(padx=40)

        #CPF
        cpf_label = customtkinter.CTkLabel(master=manage_users_frame,text="CPF:",font=text_font)
        cpf_label.place(x=30,y=310)
        cpf= customtkinter.CTkLabel(master=manage_users_frame,text="0",font=font,text_color="#e3685e")
        cpf.place(x=70,y=310)

        #ITAX
        itax_label = customtkinter.CTkLabel(master=manage_users_frame,text="ITAX:",font=text_font)
        itax_label.place(x=170,y=310)
        itax= customtkinter.CTkLabel(master=manage_users_frame,text="0",font=font,text_color="#e3685e")
        itax.place(x=215,y=310)

        #LIC
        lic_label = customtkinter.CTkLabel(master=manage_users_frame,text="LIC:",font=text_font)
        lic_label.place(x=290,y=310)
        lic= customtkinter.CTkLabel(master=manage_users_frame,text="N.A",font=font,text_color="#6ec555")
        lic.place(x=325,y=310)

        #TOTAL DEDUCTIONS
        deductions_label = customtkinter.CTkLabel(master=manage_users_frame,text="Total Deduction:",font=text_font)
        deductions_label.place(x=30,y=350)
        deductions= customtkinter.CTkLabel(master=manage_users_frame,text="0",font=font,text_color="#e3685e")
        deductions.place(x=160,y=350)

        #GROSS PAY
        gross_pay_label = customtkinter.CTkLabel(master=manage_users_frame,text="Gross Pay:",font=text_font)
        gross_pay_label.place(x=290,y=350)
        gross_pay= customtkinter.CTkLabel(master=manage_users_frame,text="0",font=font,text_color="#6ec555")
        gross_pay.place(x=380,y=350)

        #IN HAND SALARY
        net_salary_calc = customtkinter.CTkLabel(master=manage_users_frame,text=f"Net Salary"
                                            ,font=text_font,bg_color="#474545",anchor="w",width=2000,height=40)
        net_salary_calc.place(x=0,y=390)
        net_salary_calc.configure(padx=40)
        
        #Total Working Days
        working_days_label = customtkinter.CTkLabel(master=manage_users_frame,text="Working Days:",font=text_font)
        working_days_label.place(x=30,y=440)
        working_days= customtkinter.CTkLabel(master=manage_users_frame,text="0",font=font)
        working_days.place(x=145,y=440)

        #NET SALARY
        net_salary_label = customtkinter.CTkLabel(master=manage_users_frame,text="Net Salary:",font=text_font)
        net_salary_label.place(x=190,y=440)
        net_salary= customtkinter.CTkLabel(master=manage_users_frame,text="0",font=font)
        net_salary.place(x=280,y=440)

        save_button = customtkinter.CTkButton(master=manage_users_frame,text="Save Changes",font=font,fg_color="#4b873a",command=lambda : confirmation_window())
        save_button.place(x=440,y=440)

        self.window.mainloop()
    
user = Users()
user.login_page()