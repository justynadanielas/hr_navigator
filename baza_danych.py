from opinion import Opinion
from employee import Employee
from report import Report
import sqlite3
from sqlite3 import Error
from typing import Literal, List


class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.create_table()
        self.data = {}
        self.data["pracownicy"] = self.load_employees()

        self.data["opinie"] = self.load_opinions()

        self.data["raporty"] = self.load_reports()

    def create_table(self):
        conn = sqlite3.connect(self.database_name)
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

    def add_data_to_table(self, table, data):
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()

            placeholders = ', '.join(['?' for _ in data])
            query = f'INSERT INTO {table} VALUES ({placeholders})'
            cursor.execute(query, tuple(data))

            conn.commit()
            conn.close()

            print(f'Dane zostały dodane do tabeli {table}.')
        except Exception as e:
            print(f'Błąd podczas dodawania danych: {e}')

    def delete_data_from_table(self, table, row):
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()

            cursor.execute(f'DELETE FROM {table} WHERE id = ?', (row,))

            conn.commit()
            conn.close()

            print(f'Wiersz {row} z tabeli {table} został usunięty.')
        except Exception as e:
            print(f'Błąd podczas usuwania danych: {e}')

    def get_data_from_table(self, table):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table}')
        data = cursor.fetchall()
        conn.close()
        return data

    def get_employee_by_id(self, employee_id):
        conn = sqlite3.connect(self.database_name)
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

    def get_employee_by_id(self, id: int) -> Employee | None:
        for employee in self.data["pracownicy"]:
            if employee.id == id:
                return employee
        return None

    def get_all_employees(self) -> list[Employee]:
        return self.data["pracownicy"]

    def load_employees(self) -> list[Employee]:
        employees = []
        with open('pracownicy.csv', 'r', encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                employee = Employee(int(data[0]), data[1], data[2], data[3])
                employees.append(employee)
        return employees

    def get_all_opinions(self) -> list[Opinion]:
        return self.data["opinie"]

    def load_opinions(self) -> list[Opinion]:
        opinions = []
        with open('opinie.csv', 'r', encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                opinion = Opinion(int(data[0]), self.get_employee_by_id(int(data[1])),
                                  self.get_employee_by_id(int(data[2])), data[3])
                opinions.append(opinion)
        return opinions

    def add_opinion(self, author_employee: Employee, judged_employee: Employee, opinion_body: str):
        id = len(self.data["opinie"])
        self.data["opinie"].append(Opinion(id, author_employee, judged_employee, opinion_body))
        self.save_opinions_to_csv()

    def delete_opinion(self, opinion):
        self.data['opinie'].remove(opinion)

    def get_user(self, username: str, password: str) -> Employee | None:
        for employee in self.get_all_employees():
            if username == str(employee.id) and password == employee.haslo:
                return employee
        return None

    def get_all_reports(self) -> list[Report]:
        return self.data['raporty']

    def load_reports(self) -> list[Report]:
        reports = []
        with open('raporty.csv', 'r', encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                report = Report(int(data[0]), self.get_employee_by_id(int(data[1])), data[2], data[3])
                reports.append(report)
        return reports

    def save_reports_to_csv(self):
        with open('raporty.csv', 'w', encoding="utf-8") as file:
            for report in self.data['raporty']:
                file.write(f"{report.id},{report.judged_employee.id},{report.date},{report.report_body}\n")

    def save_opinions_to_csv(self):
        with open('opinie.csv', 'w', encoding="utf-8") as file:
            for opinion in self.data['opinie']:
                file.write(f"{opinion.id},{opinion.author_employee.id},{opinion.judged_employee.id},{opinion.opinion_body}\n")

    def save_employees_to_csv(self):
        with open('pracownicy.csv', 'w', encoding="utf-8") as file:
            for employee in self.data['pracownicy']:
                file.write(f"{employee.id},{employee.haslo},{employee.imie},{employee.nazwisko}\n")

    def save_data_to_csv(self):
        self.save_opinions_to_csv()
        self.save_reports_to_csv()
        self.save_employees_to_csv()

    def get_reports_by_user_id(self, user_id: int) -> list[Report]:
        # standardowe filtrowanie
        return [report for report in self.get_all_reports() if report.judged_employee.id == user_id]


if __name__=="__main__":
    baza_danych = Database("data")
    # print(baza_danych.get_all_employees())
    # print(foo := baza_danych.get_all_opinions())
    print(baza_danych.get_all_reports())
    baza_danych.save_reports_to_csv()
    baza_danych.save_opinions_to_csv()
    baza_danych.save_employees_to_csv()
