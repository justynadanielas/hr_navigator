import tkinter as tk


class ReportFrame(tk.Frame):
    def __init__(self, root: "System"):
        super().__init__(root)
        self.root = root
        self.refresh_report_frame()

    def show_report(self):
        self.pack()
        self.root.opinion_frame.pack_forget()

    def refresh_report_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

        reports = self.root.baza_danych.get_all_reports()

        for report in reports:
            if report.judged_employee == self.root.current_user:
                label = tk.Label(self, text=report.report_body)
                label.pack(padx=30, pady=30)
            # else:
            #     label = tk.Label(self, text="brak raportów do pokazania")
            #     label.pack(padx=30, pady=30)
