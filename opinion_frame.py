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

        # trzeba w tych forach zapodać counter zamiast enumerate
        # for i, opinion in enumerate(opinions, start=1):
        #     author_employee_name = opinion.author_employee.imie + " " + opinion.author_employee.nazwisko
        #     judged_employee_name = opinion.judged_employee.imie + " " + opinion.judged_employee.nazwisko
        #     if opinion.author_employee != self.root.current_user:
        #         label_opinion_body = tk.Label(self, text=opinion.opinion_body[:15] + "...")
        #         label_opinion_body.grid(row=i, column=0, padx=20)
        #
        #         label_author_employee_name = tk.Label(self, text=author_employee_name)
        #         label_author_employee_name.grid(row=i, column=1, padx=20)
        #
        #         label_judged_employee_name = tk.Label(self, text=judged_employee_name)
        #         label_judged_employee_name.grid(row=i, column=2, padx=20)
        #
        #         button_wyswietl = tk.Button(self, text="Wyświetl", command=lambda o=opinion: self.show_opinion(o))
        #         button_wyswietl.grid(row=i, column=3)

        # for i, opinion in enumerate(opinions, start=1):
        #     author_employee_name = opinion.author_employee.imie + " " + opinion.author_employee.nazwisko
        #     judged_employee_name = opinion.judged_employee.imie + " " + opinion.judged_employee.nazwisko
        #
        #     if opinion.author_employee == self.root.current_user:
        #         label_opinion_body = tk.Label(self, text=opinion.opinion_body[:15] + "...")
        #         label_opinion_body.grid(row=i, column=0, padx=20)
        #
        #         label_author_employee_name = tk.Label(self, text=author_employee_name)
        #         label_author_employee_name.grid(row=i, column=1, padx=20)
        #
        #         label_judged_employee_name = tk.Label(self, text=judged_employee_name)
        #         label_judged_employee_name.grid(row=i, column=2, padx=20)
        #
        #         button_wyswietl = tk.Button(self, text="Wyświetl", command=lambda o=opinion: self.show_opinion(o))
        #         button_wyswietl.grid(row=i, column=3)
        #         button_edytuj = tk.Button(self, text="Edytuj", command=lambda o=opinion: self.edit_opinion(o))
        #         button_edytuj.grid(row=i, column=4)
        #         button_usun = tk.Button(self, text="Usuń", command=lambda o=opinion: self.delete_opinion(o))
        #         button_usun.grid(row=i, column=5)
        # button_dodaj_opinie = tk.Button(self, text="Dodaj opinię", command=self.root.show_add_opinion_frame)
        # button_dodaj_opinie.grid(row=len(opinions)+1, column=5)

        others_opinions_frame = tk.Frame(self)
        others_opinions_frame.pack()
        my_opinions_frame = tk.Frame(self)
        my_opinions_frame.pack()

        opinions = self.root.baza_danych.get_all_opinions()
        label_opinion_header = tk.Label(others_opinions_frame, text="Treść opinii")
        label_opinion_header.grid(row=0, column=0, padx=20)
        label_author_employee_header = tk.Label(others_opinions_frame, text="Osoba opiniująca")
        label_author_employee_header.grid(row=0, column=1, padx=20)
        label_judged_employee_header = tk.Label(others_opinions_frame, text="Osoba opiniowana")
        label_judged_employee_header.grid(row=0, column=2, padx=20)

        label_my_opinion_header = tk.Label(my_opinions_frame, text="Moje opinie")
        label_my_opinion_header.grid(row=0, column=1, padx=20)
        label_opinion_header = tk.Label(my_opinions_frame, text="Treść opinii")
        label_opinion_header.grid(row=1, column=0, padx=20)
        label_author_employee_header = tk.Label(my_opinions_frame, text="Osoba opiniująca")
        label_author_employee_header.grid(row=1, column=1, padx=20)
        label_judged_employee_header = tk.Label(my_opinions_frame, text="Osoba opiniowana")
        label_judged_employee_header.grid(row=1, column=2, padx=20)

        # zaczyna się od 2, aby uwzględnić headery
        my_opinions_counter = 2
        others_opinions_counter = 1
        for opinion in opinions:
            author_employee_name = opinion.author_employee.imie + " " + opinion.author_employee.nazwisko
            judged_employee_name = opinion.judged_employee.imie + " " + opinion.judged_employee.nazwisko
            if opinion.author_employee != self.root.current_user:
                label_opinion_body = tk.Label(others_opinions_frame, text=opinion.opinion_body[:15] + "...")
                label_opinion_body.grid(row=others_opinions_counter, column=0, padx=20)

                label_author_employee_name = tk.Label(others_opinions_frame, text=author_employee_name)
                label_author_employee_name.grid(row=others_opinions_counter, column=1, padx=20)

                label_judged_employee_name = tk.Label(others_opinions_frame, text=judged_employee_name)
                label_judged_employee_name.grid(row=others_opinions_counter, column=2, padx=20)

                button_wyswietl = tk.Button(others_opinions_frame, text="Wyświetl", command=lambda o=opinion: self.show_opinion(o))
                button_wyswietl.grid(row=others_opinions_counter, column=3)
                others_opinions_counter += 1

            if opinion.author_employee == self.root.current_user:
                label_opinion_body = tk.Label(my_opinions_frame, text=opinion.opinion_body[:15] + "...")
                label_opinion_body.grid(row=my_opinions_counter, column=0, padx=20)

                label_author_employee_name = tk.Label(my_opinions_frame, text=author_employee_name)
                label_author_employee_name.grid(row=my_opinions_counter, column=1, padx=20)

                label_judged_employee_name = tk.Label(my_opinions_frame, text=judged_employee_name)
                label_judged_employee_name.grid(row=my_opinions_counter, column=2, padx=20)

                button_wyswietl = tk.Button(my_opinions_frame, text="Wyświetl", command=lambda o=opinion: self.show_opinion(o))
                button_wyswietl.grid(row=my_opinions_counter, column=3)
                button_edytuj = tk.Button(my_opinions_frame, text="Edytuj", command=lambda o=opinion: self.edit_opinion(o))
                button_edytuj.grid(row=my_opinions_counter, column=4)
                button_usun = tk.Button(my_opinions_frame, text="Usuń", command=lambda o=opinion: self.delete_opinion(o))
                button_usun.grid(row=my_opinions_counter, column=5)
                my_opinions_counter += 1
        button_dodaj_opinie = tk.Button(my_opinions_frame, text="Dodaj opinię", command=self.root.show_add_opinion_frame)
        button_dodaj_opinie.grid(row=len(opinions)+1, column=5)

    def edit_opinion(self, opinion):
        new_opinion = simpledialog.askstring(
            "Edytuj opinię",
            f"Edytuj opinię dla pracownika",
            initialvalue=opinion.opinion_body)
        # jeśli ktoś nic nie zmieni, new_opinion będzie None
        if new_opinion is not None:
            opinion.opinion_body = new_opinion
        self.refresh_opinion_frame()

    def delete_opinion(self, opinion):
        self.root.baza_danych.delete_opinion(opinion)
        self.refresh_opinion_frame()
