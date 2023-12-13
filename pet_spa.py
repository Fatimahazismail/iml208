import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def book_appointment():
    # Pet info
    pet_name = pet_name_entry.get()
    pet_species = pet_species_combobox.get()
    
    if pet_name and pet_species:
        service = service_combobox.get()
        pet_info = f"Pet Name: {pet_name}, Pet Species: {pet_species}, Service: {service}"
        user_listbox.insert(tk.END, pet_info)
        print("Pet Name:", pet_name, "Pet Species:", pet_species, "Service:", service)
        print("------------------------------------------")
    else:
        messagebox.showwarning(title="Error", message="Pet name and pet species are required.")

def register_user():
    user_name = user_name_entry.get()
    user_email = user_email_entry.get()
    
    if user_name and user_email:
        user_phone = user_phone_entry.get()
        user_info = f"User Name: {user_name}, User Email: {user_email}, User Phone: {user_phone}"
        user_listbox.insert(tk.END, user_info)
        print("User Name:", user_name, "User Email:", user_email, "User Phone:", user_phone)
        print("------------------------------------------")
    else:
        messagebox.showwarning(title="Error", message="User name and user email are required.")

window = tk.Tk()
window.title("Pet Spa Booking System")
window.geometry("800x600")  # Set the initial size of the window

# Set background color
window.configure(bg="#05454A")

frame = tk.Frame(window, bg="#05454A")
frame.pack()

# Pet Info
pet_info_frame = tk.LabelFrame(frame, text="Pet Information", bg="#05454A", fg="white", font=("Arial", 14))
pet_info_frame.grid(row=0, column=0, padx=20, pady=10)

pet_name_label = tk.Label(pet_info_frame, text="Pet Name", bg="#05454A", fg="white", font=("Arial", 12))
pet_name_label.grid(row=0, column=0)
pet_name_entry = tk.Entry(pet_info_frame, font=("Arial", 12))
pet_name_entry.grid(row=1, column=0)

pet_species_label = tk.Label(pet_info_frame, text="Pet Species", bg="#05454A", fg="white", font=("Arial", 12))
pet_species_combobox = ttk.Combobox(pet_info_frame, values=["Dog", "Cat"], font=("Arial", 12))
pet_species_label.grid(row=0, column=1)
pet_species_combobox.grid(row=1, column=1)

service_label = tk.Label(pet_info_frame, text="Service", bg="#05454A", fg="white", font=("Arial", 12))
service_combobox = ttk.Combobox(pet_info_frame, values=["Pet Grooming", "Pet Spa"], font=("Arial", 12))
service_label.grid(row=0, column=2)
service_combobox.grid(row=1, column=2)

for widget in pet_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# User Registration
user_registration_frame = tk.LabelFrame(frame, text="User Registration", bg="#05454A", fg="white", font=("Arial", 14))
user_registration_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

user_name_label = tk.Label(user_registration_frame, text="User Name", bg="#05454A", fg="white", font=("Arial", 12))
user_name_label.grid(row=0, column=0)
user_name_entry = tk.Entry(user_registration_frame, font=("Arial", 12))
user_name_entry.grid(row=1, column=0)

user_email_label = tk.Label(user_registration_frame, text="User Email", bg="#05454A", fg="white", font=("Arial", 12))
user_email_entry = tk.Entry(user_registration_frame, font=("Arial", 12))
user_email_label.grid(row=0, column=1)
user_email_entry.grid(row=1, column=1)

user_phone_label = tk.Label(user_registration_frame, text="User Phone", bg="#05454A", fg="white", font=("Arial", 12))
user_phone_entry = tk.Entry(user_registration_frame, font=("Arial", 12))
user_phone_label.grid(row=0, column=2)
user_phone_entry.grid(row=1, column=2)

for widget in user_registration_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Buttons
book_button = tk.Button(pet_info_frame, text="Book Appointment", command=book_appointment, font=("Arial", 12))
book_button.grid(row=2, column=0, columnspan=3, sticky="news", padx=20, pady=10)

register_button = tk.Button(user_registration_frame, text="Register User", command=register_user, font=("Arial", 12))
register_button.grid(row=2, column=0, columnspan=3, sticky="news", padx=20, pady=10)

user_listbox = tk.Listbox(frame, selectmode=tk.SINGLE, font=("Arial", 12), width=75)
user_listbox.grid(row=3, column=0, padx=20, pady=10)

# New Frame for Delete and Update Buttons
bottom_frame = tk.Frame(frame, bg="#05454A")
bottom_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

delete_button = tk.Button(bottom_frame, text="Delete Entry", command=lambda: user_listbox.delete(tk.ACTIVE), font=("Arial", 12))
delete_button.grid(row=0, column=0, padx=10)

update_button = tk.Button(bottom_frame, text="Update", font=("Arial", 12))
update_button.grid(row=0, column=1, padx=10)

# Center the buttons within bottom_frame
bottom_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(1, weight=1)

window.mainloop()
