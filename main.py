import tkinter as tk
from tkinter import simpledialog

from baza_danych import BazaDanych


class ButtonFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        button_harmonogram = tk.Button(self, text="Harmonogram")
        button_opinie = tk.Button(self, text="Opinie", command=self.root.show_opinion_frame)
        button_pracownicy = tk.Button(self, text="Pracownicy")
        button_raporty = tk.Button(self, text="Raporty", command=self.root.show_report_frame)
        button_moje_konto = tk.Button(self, text="Moje konto")
        button_wyloguj = tk.Button(self, text="Wyloguj")
        button_harmonogram.pack(side="left", padx=10)
        button_opinie.pack(side="left", padx=10)
        button_pracownicy.pack(side="left", padx=10)
        button_raporty.pack(side="left", padx=10)
        button_moje_konto.pack(side="left", padx=10)
        button_wyloguj.pack(side="right", padx=10)


class OpinionFrame(tk.Frame):
    def __init__(self, root: "System"):
        super().__init__(root)
        self.root = root
        self.refresh_opinion_frame()

    def show_opinion(self, opinion):
        opinion_window = tk.Toplevel(self)
        opinion_window.title("Opinia")
        label = tk.Label(opinion_window, text=opinion.opinion_body)
        label.pack(padx=30, pady=30)

    def refresh_opinion_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

        opinions = self.root.baza_danych.get_all_opinions()
        for i, opinion in enumerate(opinions):
            label = tk.Label(self, text=opinion.opinion_body[:15] + "...")
            label.grid(row=i, column=0, padx=100)
            button_wyswietl = tk.Button(self, text="Wyświetl", command=lambda o=opinion: self.show_opinion(o))
            button_wyswietl.grid(row=i, column=1)
            button_edytuj = tk.Button(self, text="Edytuj", command=lambda o=opinion: self.edit_opinion(o))
            button_edytuj.grid(row=i, column=2)
            button_usun = tk.Button(self, text="Usuń", command=lambda o=opinion: self.delete_opinion(o))
            button_usun.grid(row=i, column=3)
        button_dodaj_opinie = tk.Button(self, text="Dodaj opinię", command=self.root.show_add_opinion_frame)
        button_dodaj_opinie.grid(row=len(opinions), column=3)

    def edit_opinion(self, opinion):
        new_opinion = simpledialog.askstring(
            "Edytuj opinię",
            f"Edytuj opinię dla pracownika A",
            initialvalue=opinion.opinion_body)
        # jeśli ktoś nic nie zmieni, new_opinion będzie None
        if new_opinion is not None:
            opinion.opinion_body = new_opinion
        self.refresh_opinion_frame()

    def delete_opinion(self, opinion):
        self.root.baza_danych.delete_opinion(opinion)
        self.refresh_opinion_frame()


class AddOpinionFrame(tk.Frame):
    def __init__(self, root: "System"):
        super().__init__(root)
        self.root = root
        self.refresh_add_opinion_frame()

    def refresh_add_opinion_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        employees = self.root.baza_danych.get_all_employees()
        employees_names = []
        for employee in employees:
            employees_names.append(f"{employee.imie} {employee.nazwisko}")

        var = tk.Variable(value=employees_names)
        listbox = tk.Listbox(
            self,
            listvariable=var,
            height=6,
            selectmode=tk.SINGLE)

        listbox.pack(fill=tk.X, expand=False)
        text = tk.Text(self, height=6)
        text.pack(fill=tk.X, expand=False)
        button = tk.Button(self, text="Wyślij opinię", command=self.submit_opinion)
        button.pack()

    def submit_opinion(self):
        pass


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
            'raporty': ReportFrame(self),
            'dodaj opinię': AddOpinionFrame(self)
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

    def show_add_opinion_frame(self):
        self.show_frame('dodaj opinię')


if __name__ == "__main__":
    root = System()

    # Run the Tkinter event loop
    root.mainloop()
