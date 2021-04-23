from tkinter import *
import tkinter as tk
import psycopg2


root = Tk()


def insert_data(name, age, address):
    connection = psycopg2.connect(dbname="postgres", user="postgres",
                                  password="EnterYourPassword", host="localhost", port="5432")
    cursor = connection.cursor()
    sql = '''Insert into student (NAME, AGE, ADDRESS) values (%s, %s, %s);'''
    cursor.execute(sql, (name, age, address))
    print("Values added!!!")
    connection.commit()
    connection.close()
    display_all()


def search(id):
    connection = psycopg2.connect(dbname="postgres", user="postgres",
                                  password="EnterYourPassword", host="localhost", port="5432")
    cursor = connection.cursor()
    sql = '''select * from student where id = %s;'''
    cursor.execute(sql, (id))
    result = cursor.fetchone()
    print("Data Fetched!!!")
    display_search(result)
    connection.commit()
    connection.close()


def display_search(result):
    listbox = Listbox(frame, width=30, height=1)
    listbox.grid(row=9, column=1)
    listbox.insert(END, result)


def display_all():
    connection = psycopg2.connect(dbname="postgres", user="postgres",
                                  password="EnterYourPassword", host="localhost", port="5432")
    cursor = connection.cursor()
    sql = '''select * from student;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Data Fetched!!!")

    listbox = Listbox(frame, width=30, height=10)
    listbox.grid(row=10, column=1)
    for row in result:
        listbox.insert(END, row)
    connection.commit()
    connection.close()


canvas = Canvas(root, width=800, height=540)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="Add data : ")
label.grid(row=0, column=1)

label = Label(frame, text="Add Name : ")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

label = Label(frame, text="Add Age : ")
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

label = Label(frame, text="Add Address : ")
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

button = Button(frame, text="Add", command=lambda: insert_data(
    entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row=4, column=1)

label = Label(frame, text="Search data : ")
label.grid(row=5, column=1)

label = Label(frame, text="Search by ID : ")
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text="Search", command=lambda: search(id_search.get()))
button.grid(row=6, column=2)

display_all()

root.mainloop()
