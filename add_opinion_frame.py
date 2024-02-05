import tkinter as tk


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
            employees_names.append(f"{employee.id}. {employee.imie} {employee.nazwisko}")

        var = tk.Variable(value=employees_names)
        self.employee_listbox = tk.Listbox(
            self,
            listvariable=var,
            height=6,
            selectmode=tk.SINGLE)

        self.employee_listbox.pack(fill=tk.X, expand=False)

        opinion_text = tk.Text(self, height=6)
        opinion_text.pack(fill=tk.X, expand=False)

        # opinion_text.get() wyciąga tekst z pola tekstowego opinii
        # 1.0 i tk.END to dziwny styl indeksowania tutaj
        # opinion_text = opinion_text.get("1.0", tk.END)
        button = tk.Button(
            self,
            text="Wyślij opinię",
            command=lambda: self.submit_opinion(opinion_text.get("1.0", tk.END).strip())
        )
        button.pack()

    def submit_opinion(self, opinion_body):
        selected_index = self.employee_listbox.curselection()
        judged_employee = None

        if selected_index:
            # ponieważ selected_index to tuple, castuję go na inta
            selected_index_int = selected_index[0]
            # id pracowników zaczyna się od 1, więc trzeba przesunąć indeks o 1
            judged_employee = self.root.baza_danych.get_employee_by_id(selected_index_int + 1)

        # tu potrzebny kod, który jako author_employee umieści zalogowaną osobę
        author_employee = self.root.current_user

        self.root.baza_danych.add_opinion(author_employee, judged_employee, opinion_body)
        self.refresh_add_opinion_frame()
        self.root.show_opinion_frame()
