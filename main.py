import tkinter as tk


class ButtonFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()
        button_harmonogram = tk.Button(self, text="Harmonogram")
        button_opinie = tk.Button(self, text="Opinie")
        button_pracownicy = tk.Button(self, text="Pracownicy")
        button_raporty = tk.Button(self, text="Raporty")
        button_moje_konto = tk.Button(self, text="Moje konto")
        button_wyloguj = tk.Button(self, text="Wyloguj")
        button_harmonogram.pack(side="left", padx=10)
        button_opinie.pack(side="left", padx=10)
        button_pracownicy.pack(side="left", padx=10)
        button_raporty.pack(side="left", padx=10)
        button_moje_konto.pack(side="left", padx=10)
        button_wyloguj.pack(side="right", padx=10)


class System(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HRNavigator")
        self.geometry("700x300")
        frame = ButtonFrame(self)
        # frame.pack()


if __name__ == "__main__":
    root = System()

    # Run the Tkinter event loop
    root.mainloop()
