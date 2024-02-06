import tkinter as tk
from tkinter import messagebox


class LoginFrame(tk.Frame):
    def __init__(self, root: "System"):
        super().__init__(root)
        self.root = root
        self.refresh_login_frame()

    def refresh_login_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Login:").grid(row=0, column=0, sticky="e")
        tk.Label(self, text="Hasło:").grid(row=1, column=0, sticky="e")

        self.username_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show="*")  # Entry widget for password with a '*' mask

        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        login_button = tk.Button(self, text="Login", command=self.validate_login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.root.baza_danych.get_user(username, password)
        # Replace this with your actual validation logic
        if user:
            self.root.current_user = user
            # messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            self.root.show_button_frame()
            self.root.show_opinion_frame()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
