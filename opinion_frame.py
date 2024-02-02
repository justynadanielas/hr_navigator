from tkinter import simpledialog
import tkinter as tk


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
            # jak dodać nagłówki "osoba opiniująca" i "osoba opiniowana"?
            # jak to wyrównać, chyba trzeba znów użyć grid?
            author_employee_name = opinion.author_employee.imie + " " + opinion.author_employee.nazwisko
            judged_employee_name = opinion.judged_employee.imie + " " + opinion.judged_employee.nazwisko
            label = tk.Label(
                self,
                text=opinion.opinion_body[:15] + f"... {author_employee_name}  {judged_employee_name}"
            )
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
