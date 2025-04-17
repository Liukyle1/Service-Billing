import sqlite3
from tkinter import *
from tkinter import messagebox, ttk

root = Tk()
root.title("Service Billing Management System")
root.geometry("800x600")

def connect_db():
    conn = sqlite3.connect('service_management.db')
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
    c.execute('''
        SELECT Clients.ClientID, Clients.FirstName, Clients.LastName, Clients.Email, Clients.PhoneNumber,
               Services.ServiceName, Services.Rate
        FROM Clients
        LEFT JOIN Services ON Clients.ServiceID = Services.ServiceID
    ''')

    records = c.fetchall()
    conn.close()

    if not records:
        messagebox.showinfo("Clients", "No clients found.")
        return

    result = ""
    for row in records:
        ClientID, fname, lname, email, phone, service, rate = row
        result += (
            f"\nClient ID : {ClientID}\n"
            f"Name      : {fname} {lname}\n"
            f"Email     : {email}\n"
            f"Phone     : {phone}\n"
            f"Service   : {service or 'N/A'}\n"
            f"Rate      : ${rate or 0:.2f}\n"
            f"{'-'*40}\n"
        )

    messagebox.showinfo("Client List", result)

def delete_client():
    conn, c= connect_db()
    c.execute("DELETE FROM Clients WHERE ClientID=?", (id_entry.get(),))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success","Customer Deleted Successfully")

def update_client():
    conn, c = connect_db()
    c.execute("UPDATE Clients SET FirstName=?, LastName=?, Email=?, PhoneNumber=? WHERE ClientID=?",
    (FirstName_entry.get(), LastName_entry.get(), Email_entry.get(), PhoneNumber_entry.get(),id_entry.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Customer Updated Successfully")

# GUI Layout






# Create a frame for the form
form_frame = Frame(root)
form_frame.pack(pady=30, expand =True)

# Now use grid INSIDE the frame (not root)
Label(form_frame, text="Client ID (For Update/Delete)").grid(row=5, column=0, padx=10, pady=5)
id_entry = Entry(form_frame)
id_entry.grid(row=5, column=1, padx=10, pady=5)


Label(form_frame, text="First Name").grid(row=0, column=0, padx=10, pady=5, sticky="e")
FirstName_entry = Entry(form_frame)
FirstName_entry.grid(row=0, column=1, padx=10, pady=5)

Label(form_frame, text="Last Name").grid(row=1, column=0, padx=10, pady=5, sticky="e")
LastName_entry = Entry(form_frame)
LastName_entry.grid(row=1, column=1, padx=10, pady=5)

Label(form_frame, text="Email").grid(row=2, column=0, padx=10, pady=5, sticky="e")
Email_entry = Entry(form_frame)
Email_entry.grid(row=2, column=1, padx=10, pady=5)

Label(form_frame, text="Phone Number").grid(row=3, column=0, padx=10, pady=5, sticky="e")
PhoneNumber_entry = Entry(form_frame)
PhoneNumber_entry.grid(row=3, column=1, padx=10, pady=5)

Button(form_frame, text="Add Client", command=create_client).grid(row=4, column=0, columnspan=2, pady=10)

Button(root, text="View All Clients", command=read_client).pack(pady=2)
Button(root, text="Delete Clients", command=delete_client).pack(pady=2)
Button(root, text="Update Clients", command=update_client).pack(pady=2)

root.mainloop()
