import tkinter as tk

from add_opinion_frame import AddOpinionFrame
from baza_danych import BazaDanych
from button_frame import ButtonFrame
from opinion_frame import OpinionFrame
from report_frame import ReportFrame


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
        self.current_user = self.baza_danych.get_employee_by_id(1)
        frame_button = ButtonFrame(self)
        frame_button.pack(side="top", fill="x")

    def show_frame(self, frame_name: str):
        self.current_frame.pack_forget()
        self.current_frame = self.frames[frame_name]
        self.current_frame.pack()

    def show_opinion_frame(self):
        self.show_frame('opinie')
        self.frames['opinie'].refresh_opinion_frame()

    def show_report_frame(self):
        self.show_frame('raporty')

    def show_add_opinion_frame(self):
        self.show_frame('dodaj opinię')


if __name__ == "__main__":
    root = System()

    # Run the Tkinter event loop
    root.mainloop()
