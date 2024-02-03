import tkinter as tk


class ReportFrame(tk.Frame):
    def __init__(self, root: "System"):
        super().__init__(root)
        self.root = root
        self.refresh_report_frame()

    def show_report(self):
        self.pack()
        self.root.opinion_frame.pack_forget()

    def set_confirmation(self):
        pass

    def set_rejection(self):
        pass

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
                button_zatwierdz = tk.Button(self, text="Zatwierdź", command=self.set_confirmation)
                button_zatwierdz.grid(row=1, column=2)
                button_odrzuc = tk.Button(self, text="Odrzuć", command=self.set_rejection)
                button_odrzuc.grid(row=1, column=3)
