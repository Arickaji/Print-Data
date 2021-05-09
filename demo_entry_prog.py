# I also make a program to print the data using pdf file but i need to print the data without using pdf file  

from tkinter import *

def print_data(): # this function print the hole data into page
    pass

root = Tk()
root.title("Print Data")
root.geometry("500x500+400+100")

name_label = Label(root,text = "Name :",font = "Arial 12")
name_label.place(x = 5,y = 10)

name_value = StringVar() 
name_entry= Entry(root,textvar = name_value,font = "Arial 12",relief = FLAT)
name_entry.place(x = 65,y = 12)

address_lable = Label(root,text = "Address :",font = "Arial 12")
address_lable.place(x = 5,y = 50)

address_text= Text(root,font = "Arial 12",width = 40,height = 2,relief = FLAT,wrap = WORD)
address_text.place(x = 85,y = 50)

gender_lable = Label(root,text = "Gender :",font = "Arial 12")
gender_lable.place(x = 5,y = 110)

var_gender = IntVar()
boy = Radiobutton(root,text = "Boy",font = "Arial 12",variable = var_gender,value = 1)
boy.place(x = 100,y = 110)

girl = Radiobutton(root,text = "Girl",font = "Arial 12",variable = var_gender,value = 2)
girl.place(x = 170,y = 110)
var_gender.set(1)

print_button = Button(root,text = "Print",font = "Arial 20",width = 10,command = print_data)
print_button.place(x = 150,y = 180)

root.mainloop()