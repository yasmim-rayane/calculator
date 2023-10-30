import tkinter as tk
from tkinter import *
import customtkinter

root = customtkinter.CTk()
root.title("Calculator")
root.iconbitmap("Calculator.ico")
root.geometry("275x350")
root.resizable(False,False)

customtkinter.set_appearance_mode("Dark")

equation = ""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except ZeroDivisionError:
            result = "Division by zero isn't possible"
            equation = ""
        except:
            result = "Error"
            equation = ""
    label_result.config(text = result)

label_result = Label(root,width=27,height=4,text="",font=("arial",15,), bg="#242424", bd=1, fg="#fff")
label_result.pack()

Button = customtkinter.CTkButton(root,text="C", width=60, height=40, font=("arial",15), fg_color=("dimgray"), corner_radius=15, command=lambda: clear()).place(x=10, y=100)
Button = customtkinter.CTkButton(root,text="/", width=60, height=40, font=("arial",15), fg_color=("dimgray"), corner_radius=15, command=lambda: show("/")).place(x=75, y=100)
Button = customtkinter.CTkButton(root,text="%", width=60, height=40, font=("arial",15), fg_color=("dimgray"), corner_radius=15, command=lambda: show("%")).place(x=140, y=100)
Button = customtkinter.CTkButton(root,text="*", width=60, height=40, font=("arial",15), fg_color=("dimgray"), corner_radius=15, command=lambda: show("*")).place(x=205, y=100)

Button = customtkinter.CTkButton(root,text="7", width=60, height=40, font=("arial",15), fg_color=("gray"), corner_radius=15, command=lambda: show("7")).place(x=10, y=150)
Button = customtkinter.CTkButton(root,text="8", width=60, height=40, font=("arial",15), fg_color=("gray"), corner_radius=15, command=lambda: show("8")).place(x=75, y=150)
Button = customtkinter.CTkButton(root,text="9", width=60, height=40, font=("arial",15), fg_color=("gray"), corner_radius=15, command=lambda: show("9")).place(x=140, y=150)
Button = customtkinter.CTkButton(root,text="-", width=60, height=40, font=("arial",15), fg_color=("dimgray"), corner_radius=15, command=lambda: show("-")).place(x=205, y=150)

Button = customtkinter.CTkButton(root,text="4", width=60, height=40, font=("arial",15), fg_color=("gray"), corner_radius=15, command=lambda: show("4")).place(x=10, y=200)
Button = customtkinter.CTkButton(root,text="5", width=60, height=40, font=("arial",15), fg_color=("gray"), corner_radius=15, command=lambda: show("5")).place(x=75, y=200)
Button = customtkinter.CTkButton(root,text="6", width=60, height=40, font=("arial",15), fg_color=("gray"), corner_radius=15, command=lambda: show("6")).place(x=140, y=200)
Button = customtkinter.CTkButton(root,text="+", width=60, height=40, font=("arial",15), fg_color=("dimgray"), corner_radius=15, command=lambda: show("+")).place(x=205, y=200)

Button = customtkinter.CTkButton(root,text="1", width=60, height=40, font=("arial",15), fg_color=("gray"), corner_radius=15, command=lambda: show("1")).place(x=10, y=250)
Button = customtkinter.CTkButton(root,text="2", width=60, height=40, font=("arial",15), fg_color=("gray"), corner_radius=15, command=lambda: show("2")).place(x=75, y=250)
Button = customtkinter.CTkButton(root,text="3", width=60, height=40, font=("arial",15), fg_color=("gray"), corner_radius=15, command=lambda: show("3")).place(x=140, y=250)
Button = customtkinter.CTkButton(root,text="=", width=60, height=90, font=("arial",15), fg_color=("orange"), corner_radius=15, command=lambda: calculate()).place(x=205, y=250)

Button = customtkinter.CTkButton(root,text="0", width=125, height=40, font=("arial",15), fg_color=("gray"), corner_radius=15, command=lambda: show("0")).place(x=10, y=300)
Button = customtkinter.CTkButton(root,text=".", width=60, height=40, font=("arial",15), fg_color=("dimgray"), corner_radius=15, command=lambda: show(".")).place(x=140, y=300)

root.mainloop()