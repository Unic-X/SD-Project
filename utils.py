import customtkinter,datetime
import re,json,time
from fpdf import FPDF

def read_file(f:str):
    with open(f,"r+") as file:
        return json.load(file)


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
    time_label.after(1000,lambda : update_time(time_label)) 

def total_attendace(data,current_user):
    a = data["users"][current_user]["attendance"]
    
    total_days = (datetime.date(datetime.datetime.now().year,datetime.datetime.now().month+1,1)-datetime.date(datetime.datetime.now().year,datetime.datetime.now().month,1)).days
    
    return round((a[datetime.datetime.now().month-1]/total_days)*100,1)

def samosa(location,**kwargs):
    x=kwargs["x"]
    basic=kwargs["basic"]
    da=kwargs["da"]
    com_allow = kwargs["com_allow"]
    perks = kwargs["perks"]
    empID = kwargs["empID"]
    tax = kwargs["tax"]
    epf = kwargs["epf"]
    lic = "N.A"
    acc_number = kwargs["acc_number"]
    gross=basic+da+com_allow+perks
    total_deduction=epf+tax





    def create_table(table_data, title='', data_size = 10, title_size=12, align_data='L', align_header='L', cell_width='even', x_start='x_default',emphasize_data=[], emphasize_style=None, emphasize_color=(0,0,0)):

        default_style = pdf.font_style
        if emphasize_style == None:
            emphasize_style = default_style

        def get_col_widths():
            col_width = cell_width
            if col_width == 'even':
                col_width = pdf.epw / len(data[0]) - 1  
            elif col_width == 'uneven':
                col_widths = []

                for col in range(len(table_data[0])):
                    longest = 0 
                    for row in range(len(table_data)):
                        cell_value = str(table_data[row][col])
                        value_length = pdf.get_string_width(cell_value)
                        if value_length > longest:
                            longest = value_length
                    col_widths.append(longest + 4) 
                col_width = col_widths

            elif isinstance(cell_width, list):
                col_width = cell_width  
            else:
            
                col_width = int(col_width)
            return col_width


        if isinstance(table_data, dict):
            header = [key for key in table_data]
            data = []
            for key in table_data:
                value = table_data[key]
                data.append(value)

            data = [list(a) for a in zip(*data)]

        else:
            header = table_data[0]
            data = table_data[1:]

        line_height = pdf.font_size * 2.5

        col_width = get_col_widths()
        pdf.set_font(size=title_size)

        if x_start == 'C':
            table_width = 0
            if isinstance(col_width, list):
                for width in col_width:
                    table_width += width
            else:
                table_width = col_width * len(table_data[0])

            margin_width = pdf.w - table_width

            center_table = margin_width / 2 
            x_start = center_table
            pdf.set_x(x_start)
        elif isinstance(x_start, int):
            pdf.set_x(x_start)
        elif x_start == 'x_default':
            x_start = pdf.set_x(pdf.l_margin)

        if title != '':
            pdf.multi_cell(0, line_height, title, border=0, align='j', ln=3, max_line_height=pdf.font_size)
            pdf.ln(line_height)
        pdf.set_font(size=data_size)
        y1 = pdf.get_y()
        if x_start:
            x_left = x_start
        else:
            x_left = pdf.get_x()
        x_right = pdf.epw + x_left
        if  not isinstance(col_width, list):
            if x_start:
                pdf.set_x(x_start)
            for datum in header:
                pdf.multi_cell(col_width, line_height, datum, border=0, align=align_header, ln=3, max_line_height=pdf.font_size)
                x_right = pdf.get_x()
            pdf.ln(line_height)
            y2 = pdf.get_y()
            pdf.line(x_left,y1,x_right,y1)
            pdf.line(x_left,y2,x_right,y2)

            for row in data:
                if x_start:
                    pdf.set_x(x_start)
                for datum in row:
                    if datum in emphasize_data:
                        pdf.set_text_color(*emphasize_color)
                        pdf.set_font(style=emphasize_style)
                        pdf.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=pdf.font_size)
                        pdf.set_text_color(0,0,0)
                        pdf.set_font(style=default_style)
                    else:
                        pdf.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=pdf.font_size) # ln = 3 - move cursor to right with same vertical offset # this uses an object named pdf
                pdf.ln(line_height)

        else:
            if x_start:
                pdf.set_x(x_start)
            for i in range(len(header)):
                datum = header[i]
                pdf.multi_cell(col_width[i], line_height, datum, border=0, align=align_header, ln=3, max_line_height=pdf.font_size)
                x_right = pdf.get_x()
            pdf.ln(line_height)
            y2 = pdf.get_y()
            pdf.line(x_left,y1,x_right,y1)
            pdf.line(x_left,y2,x_right,y2)


            for i in range(len(data)):
                if x_start:
                    pdf.set_x(x_start)
                row = data[i]
                for i in range(len(row)):
                    datum = row[i]
                    if not isinstance(datum, str):
                        datum = str(datum)
                    adjusted_col_width = col_width[i]
                    if datum in emphasize_data:
                        pdf.set_text_color(*emphasize_color)
                        pdf.set_font(style=emphasize_style)
                        pdf.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=pdf.font_size)
                        pdf.set_text_color(0,0,0)
                        pdf.set_font(style=default_style)
                    else:
                        pdf.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=pdf.font_size) # ln = 3 - move cursor to right with same vertical offset # this uses an object named pdf
                pdf.ln(line_height)
        y3 = pdf.get_y()
        pdf.line(x_left,y3,x_right,y3)



    data = [
        [f"EMPLOYEE ID : {empID}",f"ACCOUNT NUMBER:{acc_number}"], 
        [f"Basic : {basic}", f"Tax : {tax}",],
        [f"DA : {da}", f"EPF : {epf}", ],
        [f"Company Allowance : {com_allow}", f"LIC : {lic}",],
        [f"Perks : {perks}"]
        ]



    pdf = FPDF(format=(200,100))
    pdf.add_page()
    pdf.set_font("Times", size=10)

    create_table(table_data = data,title='PAYSLIP      NAME: {}'.format(x), cell_width='even')
    pdf.ln()

    pdf.cell(94, 0, f'GROSS PAY :   {gross}',)
    pdf.cell(0,0,f"TOTAL DEDUCTION :   {total_deduction}")
    pdf.ln(7)
    pdf.cell(0,0,f"NET PAY : {gross-total_deduction}")
    pdf.output(rf"{location}/Payslip.pdf")