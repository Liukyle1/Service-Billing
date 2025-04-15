import sqlite3
from tkinter import *
from tkinter import messagebox, ttk

root = Tk()
root.title("Service Billing Management System")
root.geometry("800x600")

def connect_db():
    conn = sqlite3.connect('service_billing.db')
    cursor = conn.cursor()
    return conn, cursor

# Customer CRUD

def create_client():
    conn, c = connect_db()
    c.execute("INSERT INTO Clients(FirstName, LastName, Email, PhoneNumber) VALUES(?, ?, ?, ?)", 
              (FirstName_entry.get(), LastName_entry.get(), Email_entry.get(), PhoneNumber_entry.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Customer added successfully")

def read_client():
    conn, c = connect_db()
    c.execute("SELECT * FROM Clients")
    records = c.fetchall()
    conn.close()

    # JOINING RECORDS FOR DISPLAY
    result = "\n".join([f"ID: {row[0]} | FirstName: {row[1]} | LastName: {row[2]} | Email: {row[3]} | PhoneNumber: {row[4]}" for row in records])
    messagebox.showinfo("All Clients", result if result else "No Clients Found")

# GUI Layout

Label(root, text="Client ID (For Update/Delete)").pack()
id_entry = Entry(root)
id_entry.pack()

Label(root, text="Client Name").pack()
FirstName_entry = Entry(root)
FirstName_entry.pack()
LastName_entry = Entry(root)
LastName_entry.pack()
Email_entry = Entry(root)
Email_entry.pack()
PhoneNumber_entry = Entry(root)
PhoneNumber_entry.pack()

Button(root, text="Add Client", command=create_client).pack(pady=2)
Button(root, text="View All Clients", command=read_client).pack(pady=2)

root.mainloop()
