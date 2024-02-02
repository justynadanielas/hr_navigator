import tkinter as tk


class ReportFrame(tk.Frame):
    def __init__(self, root: "System"):
        super().__init__(root)
        self.root = root
        label = tk.Label(self, text="Raport")
        label.pack(padx=30, pady=30)

    def show_report(self):
        self.pack()
        self.root.opinion_frame.pack_forget()

