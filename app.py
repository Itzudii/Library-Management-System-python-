from tkinter import *
from tkinter import ttk
from functools import partial
import csv
import pandas
import datetime
import json
#  varialbles  
screen_X = 700
screen_Y = 400
# today date //////
today = datetime.date.today()
today_date = f"{today.day}-{today.month}-{today.year}"

root = Tk()
root.title("library manage ment system")
root.geometry(f"{screen_X}x{screen_Y}")

menu = Menu(root)
root.config(menu=menu)

#  multiple frames //////////////////////////////////
home_page = Frame(root,height=screen_Y,width=screen_X)
issue = Frame(root,height=screen_Y,width=screen_X)
search = Frame(root,height=screen_Y,width=screen_X)
admin_page = Frame(root,height=screen_Y,width=screen_X)
setting_page = Frame(root,height=screen_Y,width=screen_X)


def charge_adder(date):
    todays_date= datetime.datetime.strptime(today_date,"%d-%m-%Y")
    maching_date = datetime.datetime.strptime(date,"%d-%m-%Y")
    if todays_date > maching_date:
        num_of_day = todays_date - maching_date
        return num_of_day.days
    else:
        return 0
    

# add charge 
with open("settings.json",'r') as file:
    info = json.load(file)

for i in info["settings"]:
    if i["name"] == "charge":
       charge = i["value"]
    
for i in info["settings"]:
    if i["name"] == "time":
        if i["value"] != today_date:
            i["value"] = today_date
            df = pandas.read_csv("active_member.csv")
            for i in range(len(df)):
                df["charges"].iloc[i] = charge_adder(df.loc[i]["return_day"]) * charge
            df.to_csv('active_member.csv',index=False)
            with open("settings.json",'w') as file:
                json.dump(info,file)
    
    

def change_to_home():
    home_page.pack()
    issue.pack_forget()
    search.pack_forget()
    start_btn.pack_forget()
    admin_page.pack_forget()
    setting_page.pack_forget()

def change_to_issue():
    home_page.pack_forget()
    issue.pack()
    search.pack_forget()
    admin_page.pack_forget()
    setting_page.pack_forget()

def change_to_search():
    home_page.pack_forget()
    issue.pack_forget()
    search.pack()
    admin_page.pack_forget()
    setting_page.pack_forget()

def change_to_admin():
    
    home_page.pack_forget()
    issue.pack_forget()
    search.pack_forget()
    admin_page.pack()
    setting_page.pack_forget()
    admin()
    
def change_to_settings():
    home_page.pack_forget()
    issue.pack_forget()
    search.pack_forget()
    admin_page.pack_forget()
    setting_page.pack()

def apend(content):
    with open('active_member.csv','a',newline='') as csvfile:
        write = csv.writer(csvfile)
        write.writerow(content)
    with open('member_history.csv','a',newline='') as csvfile:
        write = csv.writer(csvfile)
        write.writerow(content)

def get_info(book_name,author_name,book_id,student_name,enrollment_no,email,mobileno,issue_day,return_day):
    a=[book_name.get(),author_name.get(),book_id.get(),student_name.get(),enrollment_no.get(),email.get(),mobileno.get(),issue_day.get(),return_day.get(),0]
    apend(a)
    change_to_home()

# add screen menus
menu.add_cascade(label='HOME',command=change_to_home)
menu.add_cascade(label='EXIT',command=root.destroy)

# start screen/////////////////////////////////////////////////
start_btn = Button(root,text='START',width=10,command=change_to_home)
start_btn.pack(side='bottom')

# home screen//////////////////////////////////////////////////
issue_btn = Button(home_page,text='ISSUE',width=10,command=change_to_issue)
issue_btn.place(x=20,y=100)

search_btn = Button(home_page,text='SEARCH',width=10,command=change_to_search)
search_btn.place(x=20,y=150)

search_btn = Button(home_page,text='SETTTING',width=10,command=change_to_admin)
search_btn.place(x=20,y=200)

exit_btn = Button(home_page,text='EXIT',width=10,command=root.destroy)
exit_btn.place(x=20,y=250)

# issue screen//////////////////////////////////////////////////
# entry of book detail
# HEADING......................................
head1 = Label(issue,text='BOOK DETAIL',fg='red')
head1.place(x=100,y=0,width=350,height=25)

# book name
label1 = Label(issue,text='Book Name:')
label1.place(x=50,y=25,width=350,height=25)
entry1 = Entry(issue)
entry1.place(x=50,y=50,width=350,height=25)
# author name
label2 = Label(issue,text='Author Name:')
label2.place(x=50,y=75,width=350,height=25)
entry2 = Entry(issue)
entry2.place(x=50,y=100,width=350,height=25)
# book id
label3 = Label(issue,text='Book Id:')
label3.place(x=450,y=25,width=200,height=25)
entry3 = Entry(issue)
entry3.place(x=450,y=50,width=200,height=25)


seprator1 = ttk.Separator(issue)
seprator1.place(x=0,y=150,width=screen_X,height=1)

# HEADING.......................................
head2 = Label(issue,text='STUDENT DETAIL',fg='red')
head2.place(x=100,y=175,width=350,height=25)

# student name
label4 = Label(issue,text='Student Name:')
label4.place(x=50,y=200,width=350,height=25)
entry4 = Entry(issue)
entry4.place(x=50,y=225,width=350,height=25)
# student enroll no
label5 = Label(issue,text='Enrollment No.:')
label5.place(x=450,y=200,width=200,height=25)
entry5 = Entry(issue)
entry5.place(x=450,y=225,width=200,height=25)
# student email
label6 = Label(issue,text='Email:')
label6.place(x=50,y=250,width=350,height=25)
entry6 = Entry(issue)
entry6.place(x=50,y=275,width=350,height=25)
# student mobile no
label7 = Label(issue,text='Mobile No.:')
label7.place(x=450,y=250,width=200,height=25)
entry7 = Entry(issue)
entry7.place(x=450,y=275,width=200,height=25)
# issue day
label8 = Label(issue,text='Issue Day: DD-MM-YYYY')
label8.place(x=50,y=300,width=150,height=25)
entry8 = Entry(issue)
entry8.place(x=50,y=325,width=150,height=25)
# return day
label9 = Label(issue,text='Return Day: DD-MM-YYYY')
label9.place(x=250,y=300,width=150,height=25)
entry9 = Entry(issue)
entry9.place(x=250,y=325,width=150,height=25)

# sumit button
info=partial(get_info,entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9)
addbtn = Button(issue,text='SUBMIT',command=info,activebackground='green',activeforeground='white')
addbtn.place(x=450,y=325,width=200,height=25)

# serach screen related functions/ ////////////////
def searcher(input,data=None,main_index=None):
    global search_reset
    df = pandas.read_csv('active_member.csv')
    for index,i in enumerate(df["book_id"]):
        if str(i) == input:
            main_index = index

    if main_index != None:
        info_dict = [df.loc[main_index],main_index]
        return info_dict

def delete(indx):
    global search_reset
    df = pandas.read_csv('active_member.csv')
    dff = df.drop(df.index[indx])
    dff.to_csv('active_member.csv',index=False)

    change_to_home()

    search_name.destroy()
    search_enrollment_no.destroy()
    search_mobileno.destroy()
    search_book_name.destroy()
    search_book_id.destroy()
    search_author_name.destroy()
    search_issue_date.destroy()
    search_return_date.destroy()
    search_charges.destroy()


def search_info(entry):
    global search_name,search_enrollment_no,search_mobileno,search_book_name,search_book_id,search_author_name,search_issue_date,search_return_date,search_charges
 
    a = searcher(entry.get())
    if a != None:
        search_name = Label(search,text='STUDENT NAME:     '+a[0]["student_name"])
        search_name.place(x=50,y=100)

        search_enrollment_no = Label(search,text='ENROLLMENT NO:     '+str(a[0]["enrollment_no"]))
        search_enrollment_no.place(x=50,y=125)

        search_mobileno = Label(search,text='MOBILE NO:     '+str(a[0]["mobileno"]))
        search_mobileno.place(x=50,y=150)

        search_book_name = Label(search,text='BOOK NAME:     '+a[0]["book_name"])
        search_book_name.place(x=50,y=200)

        search_book_id = Label(search,text='BOOK ID:     '+str(a[0]["book_id"]))
        search_book_id.place(x=50,y=225)

        search_author_name = Label(search,text='AUTHOR NAME:     '+a[0]["author_name"])
        search_author_name.place(x=50,y=250)

        search_issue_date = Label(search,text='ISSUE DATE:     '+str(a[0]["issue_day"]))
        search_issue_date.place(x=50,y=300)

        search_return_date = Label(search,text='RETURN DATE:     '+str(a[0]["return_day"]))
        search_return_date.place(x=300,y=300)

        search_charges = Label(search,text='CHARGES:     '+str(a[0]["charges"]))
        search_charges.place(x=50,y=325)
    
        remove = partial(delete , a[1])
        remove_btn = Button(search,text='Remove',command=remove)
        remove_btn.place(x=50,y=350,width=100,height=20)

    else:
        search_alert = Label(search,text='NOT FOUND')
        search_alert.place(x=50,y=200)

# search screen///////////////////////////////////////////////////////
search_entry = Entry(search)
search_entry.place(x=50,y=25,width=450,height=25)
s_info = partial(search_info,search_entry)
search_lb = Button(search,text='SEARCH',command=s_info)
search_lb.place(x=550,y=25,width=100,height=25)

# admin page //////////////////////////////////////
import hashlib
def generate_sha256_hash(input_string):
    encoded_input = input_string.encode()
    sha256_hash = hashlib.sha256()
    sha256_hash.update(encoded_input)
    hash_hex = sha256_hash.hexdigest()
    
    return hash_hex
def password_checker(password):
    a = password.get()
    pas_alert  = Label(admin_page,text="password is incorrect")
    pas = generate_sha256_hash(a)
    with open("settings.json",'r') as file:
        info = json.load(file)

    for i in info["settings"]:
        if i["name"] == "password":
            if i["value"] == pas:
                change_to_settings()
                pas_alert.destroy()
                password.destory()
            else:
                pas_alert.place(x=300,y=300,height=25)

    

def admin():
    password_lb = Label(admin_page,text='PASSWORD')
    password_lb.place(x=300,y=150,width=100,height=25)
    password_entry = Entry(admin_page)
    password_entry.place(x=300,y=200,width=100,height=25)
    p_info = partial(password_checker,password_entry)
    password_button = Button(admin_page,text='SUBMIT',command=p_info)
    password_button.place(x=300,y=250,width=100,height=25)
# setting screen / ///////////////////////////////////////////////
def change_password(password):
    a = password.get()
    pas = generate_sha256_hash(a)
    print(a,pas)
    with open("settings.json",'r') as file:
        info = json.load(file)

    for i in info["settings"]:
        if i["name"] == "password":
            i["value"] = pas
    
    with open("settings.json",'w') as file:
        info = json.dump(info,file)

def change_charges(charge):
    chr = charge.get()
    with open("settings.json",'r') as file:
        info = json.load(file)

    for i in info["settings"]:
        if i["name"] == "charge":
            i["value"] = int(chr)
    
    with open("settings.json",'w') as file:
        info = json.dump(info,file)
    



set_heading = Label(setting_page,text="SETTINGS",foreground='red')
set_heading.place(x=0,y=0,width=screen_X,height=25)

set_seprator1 = ttk.Separator(setting_page)
set_seprator1.place(x=0,y=25,width=screen_X,height=2)

set_change_pass_lb = Label(setting_page,text="change password",foreground='red')
set_change_pass_lb.place(x=0,y=50,width=screen_X,height=25)

set_new_pass_lb = Label(setting_page,text="enter new password")
set_new_pass_lb.place(x=50,y=75,height=25)
set_new_pass_en = Entry(setting_page)
set_new_pass_en.place(x=50,y=100,width=450,height=25)
new_pass_info = partial(change_password,set_new_pass_en)
set_new_pass_btn = Button(setting_page,text="done",command=new_pass_info)
set_new_pass_btn.place(x=550,y=100,width=100,height=25)

set_seprator2 = ttk.Separator(setting_page)
set_seprator2.place(x=0,y=150,width=screen_X,height=2)

set_change_chr_lb = Label(setting_page,text="change charges",foreground='red')
set_change_chr_lb.place(x=0,y=175,width=screen_X,height=25)

set_new_chr_lb = Label(setting_page,text="enter new charge per day")
set_new_chr_lb.place(x=50,y=200,height=25)
set_new_chr_en = Entry(setting_page)
set_new_chr_en.place(x=50,y=225,width=450,height=25)
new_chr_info = partial(change_charges,set_new_chr_en)
set_new_chr_btn = Button(setting_page,text="done",command=new_chr_info)
set_new_chr_btn.place(x=550,y=225,width=100,height=25)

set_seprator3 = ttk.Separator(setting_page)
set_seprator3.place(x=0,y=275,width=screen_X,height=2)

root.mainloop()

# admin password :1234