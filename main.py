import tkinter as tk

from add_opinion_frame import AddOpinionFrame
from baza_danych import BazaDanych
from button_frame import ButtonFrame
from login_frame import LoginFrame
from opinion_frame import OpinionFrame
from pracownik_szeregowy import PracownikSzeregowy
from report_frame import ReportFrame


class System(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HRNavigator")
        self.geometry("700x450")

        self.baza_danych = BazaDanych()
        self.current_user: PracownikSzeregowy | None = None
        # na potrzeby testów
        # self.current_user: PracownikSzeregowy | None = self.baza_danych.get_employee_by_id(3)

        self.frames = {
            'login': LoginFrame(self),
            # 'harmonogram': ScheduleFrame(),
            'opinie': OpinionFrame(self),
            # 'pracownicy': EmployeesFrame(),
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

    def show_report_frame(self):
        self.show_frame('raporty')
        self.frames['raporty'].refresh_report_frame()

    def show_button_frame(self):
        # self.frame_button.pack_forget()
        self.button_frame.refresh_button_frame()
        # self.frame_button.pack(side="top", fill="x")

    def show_add_opinion_frame(self):
        self.show_frame('dodaj opinię')


if __name__ == "__main__":
    root = System()

    # Run the Tkinter event loop
    root.mainloop()
