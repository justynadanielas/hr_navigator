import tkinter as tk

from baza_danych import BazaDanych


class ButtonFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        button_harmonogram = tk.Button(self, text="Harmonogram")
        button_opinie = tk.Button(self, text="Opinie", command=lambda: self.root.show_opinion_frame())
        button_pracownicy = tk.Button(self, text="Pracownicy")
        button_raporty = tk.Button(self, text="Raporty", command=lambda: self.root.show_report_frame())
        button_moje_konto = tk.Button(self, text="Moje konto")
        button_wyloguj = tk.Button(self, text="Wyloguj")
        button_harmonogram.pack(side="left", padx=10)
        button_opinie.pack(side="left", padx=10)
        button_pracownicy.pack(side="left", padx=10)
        button_raporty.pack(side="left", padx=10)
        button_moje_konto.pack(side="left", padx=10)
        button_wyloguj.pack(side="right", padx=10)


class OpinionFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        opinions = self.root.baza_danych.get_all_opinions()
        for i, opinion in enumerate(opinions):
            label = tk.Label(self, text=opinion.opinion_body[:15]+"...")
            label.grid(row=i, column=0, padx=100)
            button_wyswietl = tk.Button(self, text="Wyświetl", command=lambda o=opinion: self.show_opinion(o))
            button_wyswietl.grid(row=i, column=1)
            button_edytuj = tk.Button(self, text="Edytuj")
            button_edytuj.grid(row=i, column=2)
            button_usun = tk.Button(self, text="Usuń")
            button_usun.grid(row=i, column=3)

    def show_opinion(self, opinion):
        opinion_window = tk.Toplevel(self)
        opinion_window.title("Opinia")
        label = tk.Label(opinion_window, text=opinion.opinion_body)
        label.pack(padx=30, pady=30)


class ReportFrame(tk.Frame):
    def __init__(self, root: "System"):
        super().__init__(root)
        self.root = root
        label = tk.Label(self, text="Raport")
        label.pack(padx=30, pady=30)

    def show_report(self):
        self.pack()
        self.root.opinion_frame.pack_forget()


class System(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HRNavigator")
        self.geometry("700x400")

        self.baza_danych = BazaDanych()

        self.frames = {
            # 'harmonogram': ScheduleFrame(),
            'opinie': OpinionFrame(self),
            # 'pracownicy': EmployeesFrame(),
            'raporty': ReportFrame(self)
        }

        self.current_frame = self.frames['opinie']
        frame_button = ButtonFrame(self)
        frame_button.pack(side="top", fill="x")

    def show_frame(self, frame_name: str):
        self.current_frame.pack_forget()
        self.current_frame = self.frames[frame_name]
        self.current_frame.pack()

    def show_opinion_frame(self):
        self.show_frame('opinie')

    def show_report_frame(self):
        self.show_frame('raporty')


if __name__ == "__main__":
    root = System()

    # Run the Tkinter event loop
    root.mainloop()
