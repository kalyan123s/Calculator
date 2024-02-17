# rows column indexes starts from zero
# lambda is used to pass the function arguments(or values) whenever we click

from tkinter import *
import tkinter as tk
import string

root=tk.Tk()
root.title('Calculator')

# creates a entry box where we can type anything we want
e=Entry(root, width=35, bg='#ffffff',fg='#000000',borderwidth=5)
e.grid(row=0,column=0,columnspan=3,pady=10)
# print(e)

def myclick(number):
    e.insert(END,number)

#Clears all the elements in the range
def clear():
    e.delete(0,END)

def add(): 
    e.insert(END,"+")
def subtract():
    e.insert(END,"-")
    
def multiplication():
    e.insert(END,"*")
    
def divide():
    e.insert(END,"÷")
    
def equal():
    inp_string=e.get()
    for char in inp_string:
        if(char=="+"):
            sum=0
            number=0
            for char in inp_string:
                if char.isdigit():
                    number = number * 10 + int(char)
                else:
                    sum += number
                    number = 0
            sum += number      
            e.delete(0,END)   
            e.insert(0,sum) 
        elif(char=="-"):
            sub=0
            number=0
            for char in inp_string:
                if char.isdigit():
                    number = number * 10 + int(char)
                else:
                    sub = number-sub
                    number = 0
            sub = sub-number
            e.delete(0,END)     
            e.insert(0,sub)
            
        elif(char=="*"):
            mult=1
            number=0
            for char in inp_string:
                if char.isdigit():
                    number = number * 10 + int(char)
                else:
                    mult = number*mult
                    number = 0
            mult = number*mult
            e.delete(0,END)     
            e.insert(0,mult)
            
        elif(char=="÷"):
            div=1
            number=0
            for char in inp_string:
                if char.isdigit():
                    number= number * 10 + int(char)
                else:
                    div= number/div
                    number = 0
            div = div/number
            e.delete(0,END)     
            e.insert(0,div)
     

button1=Button(root,text='1',padx=35, pady=12, command=lambda: myclick("1"), fg='black' ,bg='white')
button1.grid(row=3  , column= 0)

button2=Button(root,text='2',padx=35, pady=12, command=lambda: myclick("2"), fg='black' ,bg='white')
button2.grid(row=3  , column= 1)

button3=Button(root,text='3',padx=35, pady=12, command=lambda: myclick("3"), fg='black' ,bg='white')
button3.grid(row=3  , column= 2)

button4=Button(root,text='4',padx=35, pady=12, command=lambda: myclick("4"), fg='black' ,bg='white')
button4.grid(row= 2 , column=0)

button5=Button(root,text='5',padx=35, pady=12, command=lambda: myclick("5"), fg='black' ,bg='white')
button5.grid(row=2 , column= 1)

button6=Button(root,text='6',padx=35, pady=12, command=lambda: myclick("6"), fg='black' ,bg='white')
button6.grid(row= 2 , column=2)

button7=Button(root,text='7',padx=35, pady=12, command=lambda: myclick("7"), fg='black' ,bg='white')
button7.grid(row=1 , column=0)

button8=Button(root,text='8',padx=35, pady=12, command=lambda: myclick("8"), fg='black' ,bg='white')
button8.grid(row=1 , column=1)

button9=Button(root,text='9',padx=35, pady=12, command=lambda: myclick("9"), fg='black' ,bg='white')
button9.grid(row=1 , column=2)

button0=Button(root,text='0',padx=35, pady=12, command=lambda: myclick("0"), fg='black' ,bg='white')
button0.grid(row=4  , column=0)


button_clear=Button(root,text='Clear',padx=67, pady=12 , command=clear,  fg='black' ,bg='white')
button_clear.grid(row=4  , column=1, columnspan=2)

button_add=Button(root,text='+',padx=34, pady=12, command=add, fg='black' ,bg='white')
button_add.grid(row=5  , column=0)

button_equal=Button(root,text='=',padx=76.5, pady=12, command=equal, fg='black' ,bg='white')
button_equal.grid(row=5 , column=1, columnspan=2)

button_sub=Button(root,text='-',padx=34.5, pady=12, command=subtract, fg='black' ,bg='white')
button_sub.grid(row=6  , column=0)

button_mult=Button(root,text='*',padx=35, pady=12, command=multiplication, fg='black' ,bg='white')
button_mult.grid(row=6  , column=1)

button_divide=Button(root,text='÷',padx=34, pady=12, command=divide, fg='black' ,bg='white')
button_divide.grid(row=6  , column=2)



root.mainloop()
