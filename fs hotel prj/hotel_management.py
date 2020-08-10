import tkinter as tk
from tkinter import Frame,Button,Label,Entry,PhotoImage,Text,WORD,StringVar,IntVar,Toplevel
from tkinter.ttk import Combobox
import re
window=tk.Tk()
window.title('HOTEL MANAGEMENT SYSTEM')
window.geometry('500x500')
window.wm_attributes('-fullscreen','true')
window.geometry('500x500')
frame=Frame(window)
hot_id=0

f=open("hotel_file.txt",'r+')
for line in f:
    hot_id+=1
pic=PhotoImage(file='C:\\Users\\raj\\Downloads\\hotelbook.png')
photo=Label(image=pic)
photo.pack()
# f=open('customer_file.txt','a+')

def win1():
    top=Toplevel()
    top.title('Add Hotel Room Details')
    key=Create(top)
    top.geometry('500x500')
    button = Button(top, text="exit", command=top.destroy,fg='black',bg='white')
    button.place(x=100,y=360)
    top.mainloop()

def win2():
    top = Toplevel()
    top.title('Search Hotel Room Details')
    key = Search(top)
    top.geometry('500x500')
    button = Button(top, text="exit", command=top.destroy,fg='black',bg='white')
    button.place(x=100,y=170)
    top.mainloop()
def win3():
    top = Toplevel()
    top.title('Delete Hotel Room Details')
    key = Delete(top)
    top.geometry('500x500')
    button = Button(top, text="exit", command=top.destroy,fg='black',bg='white')
    button.place(x=100,y=170)
    top.mainloop()

def win4():
    top = Toplevel()
    top.title('Update Hotel Room Details')
    key = Edit(top)
    top.geometry('500x500')
    button = Button(top, text="exit", command=top.destroy,fg='black',bg='white')
    button.place(x=100,y=300)
    top.mainloop()

def win5():
    top = Toplevel()
    top.title('Display Hotel Room Details')
    key = Display(top)
    top.geometry('500x500')
    button = Button(top, text="exit", command=top.destroy,fg='black',bg='white')
    button.place(x=100,y=340)
    top.mainloop()


button1=Button(height=4,width=40,fg='black',bg='cyan')
button1['text']='Add Booking Details'
button1['command']=win1
button1.place(x=100,y=90)

button1=Button(height=4,width=40,fg='black',bg='cyan')
button1['text']='Search Booking Details'
button1['command']=win2
button1.place(x=1000,y=90)

button1=Button(height=3,width=30,fg='black',bg='cyan')
button1['text']='Delete Booking Details'
button1['command']=win3
button1.place(x=1075,y=300)

button1=Button(height=3,width=30,fg='black',bg='cyan')
button1['text']='Edit Booking Details'
button1['command']=win4
button1.place(x=100,y=300)

button1=Button(height=4,width=40,fg='black',bg='cyan')
button1['text']='Display Booking Details'
button1['command']=win5
button1.place(x=500,y=450)

button1=Button(height=2,width=20,fg='white',bg='cyan')
button1['text']='Exit'
button1['command']=quit
button1.place(x=575,y=550)

class Create(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.nodays=IntVar()
        self.ronum = Label(self)
        self.ronum['text']='Enter Room Number:'
        self.ronum.grid(column=0,row=3)
        self.rnum=Entry(self)
        self.rnum.grid(column=1,row=3)
        self.rotype = Label(self)
        self.rotype['text'] = 'Enter Room Type:'
        self.rotype.grid(column=0,row=4)
        self.rtype = Entry(self)
        self.rtype.grid(column=1,row=4)
        self.custname = Label(self)
        self.custname['text'] = 'Enter Customer Name:'
        self.custname.grid(column=0, row=5)
        self.cname = Entry(self)
        self.cname.grid(column=1, row=5)
        self.entrydate = Label(self)
        self.entrydate['text'] = 'Enter Entry Date:'
        self.entrydate.grid(column=0,row=6)
        self.edate = Entry(self)
        self.edate.grid(column=1,row=6)
        self.exitdate = Label(self)
        self.exitdate['text'] = 'Enter Exit Date:'
        self.exitdate.grid(column=0, row=7)
        self.exdate = Entry(self)
        self.exdate.grid(column=1, row=7)
        self.ndays=Label(self)
        self.ndays['text']='Enter no of days you want to book:'
        self.ndays.grid(column=0, row=8)
        self.combo = Combobox(self, textvariable=self.nodays)
        self.combo['values'] = (0,1,2,3,4,5)
        self.combo.grid(column=1, row=8)
        self.button = Button(self)
        self.button['text']='Add'
        self.button['command']=self.get_data
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=15, column=1)
        self.button.grid(column=1,row=16)
    def get_data(self):
        global hot_id
        hoteldetails=get_hotel_details()
        ronum = self.rnum.get()
        rtype=self.rtype.get()
        cname = self.cname.get()
        edate = self.edate.get()
        exdate = self.exdate.get()
        comb=self.combo.get()
        hotIndex = search_hotel(hoteldetails, ronum)
        if hotIndex>=0:
            self.msg.insert(0.0, "The room is already taken:")
        else:
            if ronum=='' or rtype=='' or cname=='' or edate=='' or comb=='':
                self.msg.insert(0.0, "Enter all details correctly:")
            else:
                hot_id =hot_id+ 1
                f = open('hotel_file.txt', 'a+')
                f.write("{hot_id}|{rnum}|{rtype}|{cname}|{edate}|{exdate}|{nodays}$\n".format(hot_id=hot_id,rnum=self.rnum.get(),rtype=self.rtype.get(),cname=self.cname.get(),edate=self.edate.get(),exdate=self.exdate.get(),nodays=self.combo.get()))
                self.msg.insert(0.0, "your room number id is:" + str(hot_id ))
        print('success')

class Search(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.ronum = Label(self)
        self.ronum['text'] = 'Enter Room Number:'
        self.ronum.grid(column=0, row=3)
        self.rnum = Entry(self)
        self.rnum.grid(column=1, row=3)
        self.button = Button(self)
        self.button['text'] = 'Search'
        self.button['command'] = self.search_room
        self.button.grid(column=0, row=11)
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.grid(row=5, column=2)
    def search_room(self):
        global hot_id
        hoteldetails = get_hotel_details()
        ronum = self.rnum.get()
        hotIndex = search_hotel(hoteldetails, ronum)
        if hotIndex >= 0:
            self.msg.insert(0.0, "room number is: " + ronum +"\nyour room id is:" + str(hoteldetails[hotIndex][0]) + '\n')
        else:
            self.msg.insert(0.0, "room not found or not occupied"'\n')

class Delete(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.ronum = Label(self)
        self.ronum['text'] = 'Enter Room Number:'
        self.ronum.grid(column=0, row=3)
        self.rnum = Entry(self)
        self.rnum.grid(column=1, row=3)
        self.button = Button(self)
        self.button['text'] = 'Delete'
        self.button['command'] = self.delete_hotel_details
        self.button.grid(column=0, row=11)
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.grid(row=4, column=1)
    def delete_hotel_details(self):
        global hot_id
        hoteldetails = get_hotel_details()
        ronum = self.rnum.get()
        hotIndex = search_hotel(hoteldetails, ronum)
        if hotIndex >= 0:
            del hoteldetails[hotIndex]
            hot_id-=1
            save_hotel_data(hoteldetails)
            self.msg.insert(0.0, "Hotel Details for the current room is deleted"'\n')
        else:
            self.msg.insert(0.0, "Room number not found"'\n')
        return

def get_hotel_details():
    f = open("hotel_file.txt", 'r').read()
    f = re.split("[" + "\\".join("$\\n") + "]", f)[:-2]
    f = filter(None, f)
    hotDetails = [re.split("[" + "\\".join("|") + "]", hotel) for hotel in f]
    return hotDetails

def save_hotel_data(hot_details):
    hot_details.append([])
    s="$\n".join(['|'.join(bikes) for bikes in hot_details])
    savefile=open("hotel_file.txt", 'w')
    savefile.write(s)
    return s

def search_hotel(hotDetails, ronum):
    hotIndex = -1
    for index,hotel in enumerate(hotDetails):
        if ronum == hotel[1]:
            hotIndex = index
    return hotIndex

class Edit(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):

        self.nodays=IntVar()
        self.ronum = Label(self)
        self.ronum['text']='Enter Room Number:'
        self.ronum.grid(column=0,row=3)
        self.rnum=Entry(self)
        self.rnum.grid(column=1,row=3)
        self.rotype = Label(self)
        self.rotype['text'] = 'Enter Room Type:'
        self.rotype.grid(column=0,row=4)
        self.rtype = Entry(self)
        self.rtype.grid(column=1,row=4)
        self.custname = Label(self)
        self.custname['text'] = 'Enter Customer Name:'
        self.custname.grid(column=0, row=5)
        self.cname = Entry(self)
        self.cname.grid(column=1, row=5)
        self.entrydate = Label(self)
        self.entrydate['text'] = 'Enter Entry Date:'
        self.entrydate.grid(column=0,row=6)
        self.edate = Entry(self)
        self.edate.grid(column=1,row=6)
        self.exitdate = Label(self)
        self.exitdate['text'] = 'Enter Exit Date:'
        self.exitdate.grid(column=0, row=7)
        self.exdate = Entry(self)
        self.exdate.grid(column=1, row=7)
        self.ndays=Label(self)
        self.ndays['text']='Enter no of days you want to book:'
        self.ndays.grid(column=0, row=8)
        self.combo = Combobox(self, textvariable=self.nodays)
        self.combo['values'] = (0,1,2,3,4,5)
        self.combo.grid(column=1, row=8)
        self.button = Button(self)
        self.button['text']='Update Hotel Details'
        self.button['command']=self.get_data
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=15, column=1)
        self.button.grid(column=1,row=16)
    def get_data(self):
        global hot_id
        hoteldetails = get_hotel_details()
        ronum = self.rnum.get()
        rtype = self.rtype.get()
        cname = self.cname.get()
        edate = self.edate.get()
        exdate = self.exdate.get()
        comb = self.combo.get()
        hotIndex = search_hotel(hoteldetails, ronum)
        if hotIndex >= 0:
            if ronum=='' or rtype=='' or cname=='' or edate=='' or comb=='':
                self.msg.insert(0.0, "Enter all details correctly:")
            else:
                hoteldetails[hotIndex] = [str(hot_id),self.rnum.get(),self.rtype.get(), self.cname.get(), self.edate.get(), self.exdate.get(),self.combo.get()]
                save_hotel_data(hoteldetails)
                self.msg.insert(0.0, "the updated room details are:" + str(hot_id))
        else:
            self.msg.insert(0.0, "room number not found"'\n')

def json_to_str_table(hotel_details):
    table_content=''
    for hotel in hotel_details:
        table_content += "room_id={hot_id}\t|\troom_number={rnum}\t|\troom_type={rtype}\t|\tcustomer_name={cname}\t|\tentry_date={edate}\t|\texit_date={exdate}\t|\tnodays={nodays}\n".format(hot_id=hotel[0],rnum=hotel[1],rtype=hotel[2],cname=hotel[3],edate=hotel[4],exdate=hotel[5],nodays=hotel[6])
    return table_content

class Display(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.msg = Text(self, width=150, height=20, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=12, column=1)
        self.msg['command']=self.display_room_details()
    def display_room_details(self):
        global hot_id
        hotdetails = get_hotel_details()
        hotdetails=json_to_str_table(hotdetails)
        self.msg.insert(0.0, "Displaying room booking details: \n" + str(hotdetails)+'\n')

window.mainloop()
