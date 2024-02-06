from opinia import Opinia
from pracownik_szeregowy import PracownikSzeregowy
from raport import Raport
import sqlite3
from sqlite3 import Error


class BazaDanych:
    def __init__(self, nazwa_bazy):
        self.nazwa_bazy = nazwa_bazy
        self.utworz_tabele()
        self.data = {}
        self.data["pracownicy"] = self.load_employees()

        self.data["opinie"] = self.load_opinions()

        self.data["raporty"] = self.load_reports()

    def utworz_tabele(self):
        conn = sqlite3.connect(self.nazwa_bazy)
        cursor = conn.cursor()

        # Tabela pracownicy
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pracownicy (
                id INTEGER PRIMARY KEY,
                imie_pracownika TEXT,
                nazwisko_pracownika TEXT,
                sekcja TEXT
            )
        ''')

        # Tabela harmonogram
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS harmonogram (
                id INTEGER PRIMARY KEY,
                data TEXT,
                sekcja TEXT,
                tresc_zadania TEXT
            )
        ''')

        conn.commit()
        conn.close()

    def dodaj_dane_do_tabeli(self, tabela, dane):
        try:
            conn = sqlite3.connect(self.nazwa_bazy)
            cursor = conn.cursor()

            placeholders = ', '.join(['?' for _ in dane])
            query = f'INSERT INTO {tabela} VALUES ({placeholders})'
            cursor.execute(query, tuple(dane))

            conn.commit()
            conn.close()

            print(f'Dane zostały dodane do tabeli {tabela}.')
        except Exception as e:
            print(f'Błąd podczas dodawania danych: {e}')

    def usun_wybrane_dane_z_tabeli(self, tabela, wiersz):
        try:
            conn = sqlite3.connect(self.nazwa_bazy)
            cursor = conn.cursor()

            cursor.execute(f'DELETE FROM {tabela} WHERE id = ?', (wiersz,))

            conn.commit()
            conn.close()

            print(f'Wiersz {wiersz} z tabeli {tabela} został usunięty.')
        except Exception as e:
            print(f'Błąd podczas usuwania danych: {e}')

    def pobierz_dane_z_tabeli(self, tabela):
        conn = sqlite3.connect(self.nazwa_bazy)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {tabela}')
        dane = cursor.fetchall()
        conn.close()
        return dane

    def get_employee_by_id(self, employee_id):
        conn = sqlite3.connect(self.nazwa_bazy)
        cursor = conn.cursor()

        query = "SELECT imie_pracownika, nazwisko_pracownika FROM pracownicy WHERE id = ?"
        cursor.execute(query, (employee_id,))
        result = cursor.fetchone()

        conn.close()

        # Check if the result is not None before subscripting
        if result:
            return result
        else:
            return None

    def get_employee_by_id(self, id: int) -> PracownikSzeregowy | None:
        for employee in self.data["pracownicy"]:
            if employee.id == id:
                return employee
        return None

    def get_all_employees(self) -> list[PracownikSzeregowy]:
        return self.data["pracownicy"]

    def load_employees(self) -> list[PracownikSzeregowy]:
        employees = []
        with open('pracownicy.csv', 'r', encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                employee = PracownikSzeregowy(int(data[0]), data[1], data[2], data[3])
                employees.append(employee)
        return employees

    def get_all_opinions(self) -> list[Opinia]:
        return self.data["opinie"]

    def load_opinions(self) -> list[Opinia]:
        opinions = []
        with open('opinie.csv', 'r', encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                opinion = Opinia(int(data[0]), self.get_employee_by_id(int(data[1])),
                                 self.get_employee_by_id(int(data[2])), data[3])
                opinions.append(opinion)
        return opinions

    def add_opinion(self, author_employee: PracownikSzeregowy, judged_employee: PracownikSzeregowy, opinion_body: str):
        id = len(self.data["opinie"])
        self.data["opinie"].append(Opinia(id, author_employee, judged_employee, opinion_body))

    def delete_opinion(self, opinion):
        self.data['opinie'].remove(opinion)

    def get_user(self, username: str, password: str) -> PracownikSzeregowy | None:
        for pracownik in self.get_all_employees():
            if username == str(pracownik.id) and password == pracownik.haslo:
                return pracownik
        return None

    def get_all_reports(self) -> list[Raport]:
        return self.data['raporty']

    def load_reports(self) -> list[Raport]:
        reports = []
        with open('raporty.csv', 'r', encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                report = Raport(int(data[0]), self.get_employee_by_id(int(data[1])), data[2], data[3])
                reports.append(report)
        return reports

    def get_reports_by_user_id(self, user_id: int) -> list[Raport]:
        # standardowe filtrowanie
        return [report for report in self.get_all_reports() if report.judged_employee.id == user_id]

if __name__=="__main__":
    baza_danych = BazaDanych("data")
    # print(baza_danych.get_all_employees())
    # print(foo := baza_danych.get_all_opinions())
    print(baza_danych.get_all_reports())
