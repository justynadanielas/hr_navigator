import tkinter as tk

from add_opinion_frame import AddOpinionFrame
from baza_danych import Database
from button_frame import ButtonFrame
from login_frame import LoginFrame
from opinion_frame import OpinionFrame
from employee import Employee
from report_frame import ReportFrame
from employee_frame import EmployeeFrame
from schedule_frame import ScheduleFrame


class System(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HRNavigator")
        self.geometry("700x450")

        self.database = Database("moja_baza.db")
        self.current_user: Employee | None = None

        # na potrzeby testów
        self.current_user: Employee | None = self.database.get_employee_by_id(3)

        self.frames = {
            'login': LoginFrame(self),
            'harmonogram': ScheduleFrame(self),
            'opinie': OpinionFrame(self),
            'pracownicy': EmployeeFrame(self),
            'raporty': ReportFrame(self),
            'dodaj opinię': AddOpinionFrame(self)
        }

        self.current_frame = self.frames['opinie']
        self.button_frame = ButtonFrame(self)
        self.button_frame.pack(side="top", fill="x")

    def show_frame(self, frame_name: str):
        self.current_frame.pack_forget()
        self.current_frame = self.frames[frame_name]
        self.current_frame.pack()

    def show_login_frame(self):
        self.show_frame('login')

    def handle_logout(self):
        self.current_user = None
        self.button_frame.refresh_button_frame()
        self.show_login_frame()
        self.frames['login'].refresh_login_frame()

    def show_opinion_frame(self):
        self.show_frame('opinie')
        self.frames['opinie'].refresh_opinion_frame()

    def show_employees_frame(self):
        self.show_frame('pracownicy')
        self.frames['pracownicy'].refresh_employees_frame()

    def show_report_frame(self):
        self.show_frame('raporty')
        self.frames['raporty'].refresh_report_frame()

    def show_schedule_frame(self):
        self.show_frame('harmonogram')
        self.frames['harmonogram'].refresh_schedule_frame()

    def show_my_account_frame(self):  # Dodana metoda
        # Tutaj umieść kod do wyświetlania ramki Moje konto
        pass

    def show_button_frame(self):
        self.button_frame.refresh_button_frame()

    def show_add_opinion_frame(self):
        self.show_frame('dodaj opinię')


if __name__ == "__main__":
    """baza = BazaDanych('moja_baza.db')
    # Dodanie danych

    baza.dodaj_dane_do_tabeli("harmonogram", (1, "5.02.2024", "hala", "wierc dziury frezarką"))
    baza.dodaj_dane_do_tabeli("harmonogram", (2, "5.02.2024", "hala", "frezuj detal"))
    
    baza.dodaj_dane_do_tabeli("pracownicy", (1,'Adam', 'Adamski', "sekcja hala"))
    baza.dodaj_dane_do_tabeli("pracownicy", (2,'Jan', 'Kowalski', "sekcja hala"))
    baza.dodaj_dane_do_tabeli("pracownicy", (3,'Anna', 'Nowak', "sekcja hala"))
    baza.dodaj_dane_do_tabeli("pracownicy", (4,'Marta', 'Wiśniewska', "sekcja hala"))
    baza.dodaj_dane_do_tabeli("pracownicy", (5,'Piotr', 'Kaczmarek', "sekcja hala"))
    baza.dodaj_dane_do_tabeli("pracownicy", (6,'Andrzej', 'Kaczmarek', "sekcja hala"))
    baza.dodaj_dane_do_tabeli("pracownicy", (7,'Jakub', 'Piotrkowski', "sekcja hala"))
    baza.dodaj_dane_do_tabeli("pracownicy", (8,'Piotr', 'Baran', "sekcja hala"))"""
    root = System()

    # Run the Tkinter event loop
    root.mainloop()
