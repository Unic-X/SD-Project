import customtkinter
import re,json,time,mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port = "1234",
  user="admin",
  password="arman",
  database = "samaj"
)

cursor = mydb.cursor()

def read_file(f:str):
    with open(f,"r+") as file:
        return json.load(file)

def find_password(userid:str)->str:
    cursor.execute("USE samaj;")
    cursor.execute(f"SELECT PASSWORD FROM USER WHERE ID={userid}")
    password = cursor.fetchone()
    return password
    


"""def check_login(l_frame,frame:CT.CTkEntry,username_entry:str): # must contain "pentry" textbox 
    entry = frame.get()
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
    real_password = find_password(username_entry) #TO GET REAL PASSWORD OF THE USER
    match_password = re.match(pattern, entry)
    if match_password and real_password==entry:
        return True
    else:
        frame.delete(0,100)
        invalid_pass = CT.CTkLabel(master=l_frame,text="Password must include one uppercase letter,\n special character,number",text_color="Red",font=("Century Gothic",10))
        invalid_pass.place(relx=0.21,y=210)
        return False"""

def update_time(time_label:customtkinter.CTkLabel):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    time_label.configure(text=f"{current_time} IST")
    time_label.after(1000,update_time)
