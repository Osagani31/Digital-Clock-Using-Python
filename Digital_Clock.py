from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')          
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')          
    date = time.strftime('%d-%m-%Y')  

   
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)

    
    clock.after(200, date_time)


clock = Tk()
clock.title('Digital Clock')
clock.geometry('1000x400')
clock.config(bg='black')


lab_hr = Label(clock, text="00", font=('Times New Roman', 60, "bold"), fg="white", bg="black")
lab_hr.place(x=120, y=50, height=110, width=100)
lab_hr_txt = Label(clock, text="Hour", font=('Times New Roman', 20, "bold"), fg="white", bg="black")
lab_hr_txt.place(x=120, y=190, height=40, width=100)


lab_min = Label(clock, text="00", font=('Times New Roman', 60, "bold"), fg="white", bg="black")
lab_min.place(x=340, y=50, height=110, width=100)
lab_min_txt = Label(clock, text="Min.", font=('Times New Roman', 20, "bold"), fg="white", bg="black")
lab_min_txt.place(x=340, y=190, height=40, width=100)


lab_sec = Label(clock, text="00", font=('Times New Roman', 60, "bold"), fg="white", bg="black")
lab_sec.place(x=560, y=50, height=110, width=100)
lab_sec_txt = Label(clock, text="Sec.", font=('Times New Roman', 20, "bold"), fg="white", bg="black")
lab_sec_txt.place(x=560, y=190, height=40, width=100)


lab_am = Label(clock, text="AM", font=('Times New Roman', 50, "bold"), fg="white", bg="black")
lab_am.place(x=780, y=50, height=110, width=100)
lab_am_txt = Label(clock, text="AM/PM", font=('Times New Roman', 20, "bold"), fg="white", bg="black")
lab_am_txt.place(x=780, y=190, height=40, width=100)


lab_date = Label(clock, text="00-00-0000", font=('Times New Roman', 30, "bold"), fg="white", bg="black")
lab_date.place(x=370, y=270, height=50, width=260)


date_time()

clock.mainloop()
