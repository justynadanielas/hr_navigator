import tkinter as tk


class ButtonFrame(tk.Frame):
    def __init__(self, root: "System"):
        super().__init__(root)
        self.root = root
        self.refresh_button_frame()

    def refresh_button_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

        button_harmonogram = tk.Button(self, text="Harmonogram")
        button_opinie = tk.Button(self, text="Opinie", command=self.root.show_opinion_frame)
        button_pracownicy = tk.Button(self, text="Pracownicy")
        button_raporty = tk.Button(self, text="Raporty", command=self.root.show_report_frame)
        button_moje_konto = tk.Button(self, text="Moje konto")
        button_harmonogram.pack(side="left", padx=10)
        button_opinie.pack(side="left", padx=10)
        button_pracownicy.pack(side="left", padx=10)
        button_raporty.pack(side="left", padx=10)
        button_moje_konto.pack(side="left", padx=10)
        if self.root.current_user:
            label_welcome_user = tk.Label(self, text=f"Witaj, {self.root.current_user.get_full_name()}")
            label_welcome_user.pack(side="left", padx=10)
            button_wyloguj = tk.Button(self, text="Wyloguj", command=self.root.handle_logout)
        else:
            button_wyloguj = tk.Button(self, text="Zaloguj", command=self.root.show_login_frame)

        button_wyloguj.pack(side="right", padx=10)
