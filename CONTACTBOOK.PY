import customtkinter as ctk
from tkinter import messagebox
import json
import os

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

DATA_FILE = "contacts.json"


# Utility Functions
def load_contacts():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_contacts(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


# GUI Class
class ContactBook(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Contact Book - Task 5")
        self.geometry("700x450")
        self.resizable(False, False)

        self.contacts = load_contacts()

        # UI Layout
        self.create_widgets()
        self.refresh_contact_list()

    def create_widgets(self):
        # Entry Frame
        entry_frame = ctk.CTkFrame(self)
        entry_frame.pack(pady=10, padx=10, fill="x")

        self.name_entry = ctk.CTkEntry(entry_frame, placeholder_text="Name")
        self.name_entry.grid(row=0, column=0, padx=5, pady=5)

        self.phone_entry = ctk.CTkEntry(entry_frame, placeholder_text="Phone")
        self.phone_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_entry = ctk.CTkEntry(entry_frame, placeholder_text="Email")
        self.email_entry.grid(row=1, column=0, padx=5, pady=5)

        self.address_entry = ctk.CTkEntry(entry_frame, placeholder_text="Address")
        self.address_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = ctk.CTkButton(entry_frame, text="Add / Update", command=self.add_or_update_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Search Field
        self.search_entry = ctk.CTkEntry(self, placeholder_text="Search by Name or Phone")
        self.search_entry.pack(pady=5, padx=10, fill="x")
        self.search_entry.bind("<KeyRelease>", self.search_contact)

        # Listbox
        self.contact_listbox = ctk.CTkTextbox(self, width=650, height=150)
        self.contact_listbox.pack(pady=5, padx=10)

        # Delete Button
        self.delete_button = ctk.CTkButton(self, text="Delete Selected", fg_color="red", command=self.delete_contact)
        self.delete_button.pack(pady=10)

    def refresh_contact_list(self, filtered=None):
        self.contact_listbox.delete("0.0", "end")
        data = filtered if filtered else self.contacts
        for contact in data:
            display = f"{contact['name']} - {contact['phone']}\n"
            self.contact_listbox.insert("end", display)

    def add_or_update_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required!")
            return

        updated = False
        for contact in self.contacts:
            if contact['phone'] == phone:
                contact.update({"name": name, "email": email, "address": address})
                updated = True
                break

        if not updated:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})

        save_contacts(self.contacts)
        self.refresh_contact_list()
        self.clear_entries()
        messagebox.showinfo("Success", "Contact saved successfully!")

    def delete_contact(self):
        selected = self.contact_listbox.get("sel.first", "sel.last")
        if not selected.strip():
            messagebox.showerror("Error", "No contact selected.")
            return

        name = selected.split(" - ")[0].strip()
        self.contacts = [c for c in self.contacts if c["name"] != name]
        save_contacts(self.contacts)
        self.refresh_contact_list()
        messagebox.showinfo("Deleted", "Contact deleted successfully.")

    def search_contact(self, event):
        query = self.search_entry.get().strip().lower()
        if not query:
            self.refresh_contact_list()
            return

        filtered = [c for c in self.contacts if query in c["name"].lower() or query in c["phone"]]
        self.refresh_contact_list(filtered)

    def clear_entries(self):
        self.name_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')


if __name__ == "__main__":
    app = ContactBook()
    app.mainloop()