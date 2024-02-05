import tkinter as tk
from tkinter import messagebox

from raport import Raport


class ReportFrame(tk.Frame):
    def __init__(self, root: "System"):
        super().__init__(root)
        self.root = root
        self.refresh_report_frame()

    def show_report(self):
        self.pack()
        self.root.opinion_frame.pack_forget()

    def confirm(self, report: Raport):
        report.is_confirmed = True
        messagebox.showinfo("Raport", "Raport potwierdzony")
        self.refresh_report_frame()

    def reject(self, report: Raport):
        report.is_rejected = True
        messagebox.showinfo("Raport", "Raport odrzucony")
        self.refresh_report_frame()

    def refresh_report_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

        if not self.root.current_user:
            label_report_header = tk.Label(self, text="Brak raportów")
            label_report_header.grid(row=0, column=0, padx=20)
            return

        reports = self.root.baza_danych.get_reports_by_user_id(self.root.current_user.id)

        label_report_header = tk.Label(self, text="Treść raportu")
        label_report_header.grid(row=0, column=0, padx=20)
        label_report_date_header = tk.Label(self, text="Data wystawienia")
        label_report_date_header.grid(row=0, column=1, padx=20)

        # tu mozna dodać napis "brak raportu"
        for report in reports:
            if report.judged_employee == self.root.current_user:
                label_report_body = tk.Label(self, text=report.report_body)
                label_report_body.grid(row=1, column=0, padx=20)
                label_report_date = tk.Label(self, text=report.date)
                label_report_date.grid(row=1, column=1, padx=20)
                if not (report.is_confirmed or report.is_rejected):
                    button_zatwierdz = tk.Button(self, text="Zatwierdź", command=lambda r=report: self.confirm(r))
                    button_zatwierdz.grid(row=1, column=2)
                    button_odrzuc = tk.Button(self, text="Odrzuć", command=lambda r=report: self.reject(r))
                    button_odrzuc.grid(row=1, column=3)
                elif report.is_confirmed:
                    label_confirmed = tk.Label(self, text="Zatwierdzony")
                    label_confirmed.grid(row=1, column=2)
                elif report.is_rejected:
                    label_rejected = tk.Label(self, text="Odrzucony")
                    label_rejected.grid(row=1, column=2)
