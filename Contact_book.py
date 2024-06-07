#import library
from tkinter import *
from tkinter import messagebox

#address book - Initialize windowg
root = Tk()
root.geometry('700x550')
root.config(bg = '#d3f3f5')
root.title('Contact Book')
root.resizable(0,0)
contactlist = [
    ['Siddharth Nigam','369854712', '123 Main St', 'siddharth@example.com'],
    ['Gaurav Patil', '521155222', '134 tain St', 'gaur@example.com'],
    ['Abhishek Nikam', '78945614', '113 sain St', 'abhi@example.com'],
    ['Sakshi Gaikwad', '58745246', ' Main St', 'sak@example.com'],
    ['Mohit Paul', '5846975', ' lain Star', 'paul@example.com'],
    ['Karan Patel', '5647892', '120 road St', 'karan@example.com'],
    ['Sam Sharma', '89685320', ' Main St 23', 'sam@example.com'],
    ['John Maheshwari', '98564785', '111 Main St', 'john@example.com'],
    ['Ganesh Pawar','85967412', '123 Rann St', 'pawar@example.com']
    ]
 
Name = StringVar()
Number = StringVar()
Address = StringVar()
Email = StringVar()


#create frame
frame = Frame(root)
frame.pack(side = RIGHT)
 
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman' ,16), bg="#f0fffc", width=20, height=20, borderwidth=3, relief= "groove")
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

#function to get select value
 
def Selected():
    print("hello",len(select.curselection()))
    if len(select.curselection())==0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])
    
#fun to add new contact
def AddContact():
    if Name.get()!="" and Number.get()!="" and Address.get()!="" and Email.get()!="":
        contactlist.append([Name.get() ,Number.get(), Address.get(), Email.get()])
        print(contactlist)
        Select_set()
        
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")
 
    else:
        messagebox.showerror("Error","Please fill the information")
 
def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get(), Address.get(), Email.get()]
   
        messagebox.showinfo("Confirmation", "Successfully Update Contact")
        
        Select_set()
 
    elif not(Name.get()) and not(Number.get()) and not(Address.get())and not(Email.get())and not(len(select.curselection())==0):
        messagebox.showerror("Error", "Please fill the information")
 
    else:
        if len(select.curselection())==0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n
                          selected row press Load button\n.
                          """
            messagebox.showerror("Error", message1)


def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')
 
def VIEW():
    NAME, PHONE, ADDR, EMAIL = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Address.set(ADDR)
    Email.set(EMAIL)


# exit game window  
def EXIT():
    root.destroy() 
 
def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for contact  in contactlist :
        name ,number, address, email = contact
        select.insert (END, name)
Select_set()

# define buttons labels and entry widget
Label(root, text = 'Name', font=("Times new roman",22,"bold"), bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Name, width=30).place(x= 200, y=30)
Label(root, text = 'Contact No.', font=("Times new roman",20,"bold"),bg = 'SlateGray3').place(x= 30, y=70)
Entry(root, textvariable = Number, width=30).place(x= 200, y=80)
Label(root, text='Address', font=("Times new roman", 20, "bold"), bg='SlateGray3').place(x=30, y=120)
Entry(root, textvariable=Address, width=30).place(x=200, y=130)

Label(root, text='Email', font=("Times new roman", 20, "bold"), bg='SlateGray3').place(x=30, y=170)
Entry(root, textvariable=Email, width=30).place(x=200, y=180)
 
Button(root,text=" ADD", font='Helvetica 16 bold',bg='#e8c1c7', command = AddContact, padx=20). place(x= 30, y=220)
Button(root,text="EDIT", font='Helvetica 16 bold',bg='#e8c1c7',command = UpdateDetail, padx=20).place(x= 30, y=280)
Button(root,text="DELETE", font='Helvetica 16 bold',bg='#e8c1c7',command = Delete_Entry, padx=20).place(x=30, y=340)
Button(root,text="VIEW", font='Helvetica 16 bold',bg='#e8c1c7', command = VIEW).place(x= 30, y=400)
Button(root,text="EXIT", font='Helvetica 20 bold',bg='yellow', command = EXIT).place(x= 250, y=470)
 
root.mainloop()





    