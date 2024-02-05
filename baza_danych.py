from opinia import Opinia
from pracownik_szeregowy import PracownikSzeregowy
from raport import Raport


class BazaDanych:
    def __init__(self):
        self.data = {}
        self.data["pracownicy"] = [
            PracownikSzeregowy(1, 'maslo', 'Adam', 'Adamski'),
            PracownikSzeregowy(2, 'maslo', 'Jan', 'Kowalski'),
            PracownikSzeregowy(3, 'maslo', 'Anna', 'Nowak'),
            PracownikSzeregowy(4, 'maslo', 'Marta', 'Wiśniewska'),
            PracownikSzeregowy(5, 'maslo', 'Piotr', 'Kaczmarek'),
            PracownikSzeregowy(6, 'maslo', 'Piotr', 'Kaczmarek'),
            PracownikSzeregowy(7, 'maslo', 'Piotr', 'Kaczmarek'),
            PracownikSzeregowy(8, 'maslo', 'Piotr', 'Kaczmarek')
        ]

        self.data["opinie"] = [
            Opinia(1, self.get_employee_by_id(1), self.get_employee_by_id(3), "Dobra robota"),
            Opinia(2, self.get_employee_by_id(2), self.get_employee_by_id(4), "Bardzo profesjonalne podejście"),
            Opinia(3, self.get_employee_by_id(3), self.get_employee_by_id(2), "Szybko i sprawnie wykonana praca"),
            Opinia(4, self.get_employee_by_id(4), self.get_employee_by_id(5), "Doskonała komunikacja i współpraca"),
            Opinia(5, self.get_employee_by_id(5), self.get_employee_by_id(1), "Polecam tego pracownika"),
            Opinia(6, self.get_employee_by_id(1), self.get_employee_by_id(3), "Jestem bardzo zadowolony"),
            Opinia(7, self.get_employee_by_id(2), self.get_employee_by_id(4), "Zawsze punktualny"),
            Opinia(8, self.get_employee_by_id(3), self.get_employee_by_id(1), "Pracownik godny zaufania"),
            Opinia(9, self.get_employee_by_id(4), self.get_employee_by_id(2), "Rzetelna i dokładna praca"),
            Opinia(10, self.get_employee_by_id(1), self.get_employee_by_id(5), "Wysoka jakość usług")
        ]

        self.data["raporty"] = [
            Raport(1, self.get_employee_by_id(1), "2024-01-01", "Ogólnie spoko"),
            Raport(2, self.get_employee_by_id(2), "2024-01-01", "Ogólnie nieźle"),
            Raport(3, self.get_employee_by_id(3), "2024-01-01", "Ogólnie daje radę"),
            Raport(4, self.get_employee_by_id(4), "2024-01-01", "Ogólnie miła")
        ]

    def get_employee_by_id(self, id: int) -> PracownikSzeregowy | None:
        for employee in self.data["pracownicy"]:
            if employee.id == id:
                return employee
        return None

    def get_all_employees(self) -> list[PracownikSzeregowy]:
        return self.data["pracownicy"]

    def get_all_opinions(self) -> list[Opinia]:
        return self.data["opinie"]

    def add_opinion(self, author_employee: PracownikSzeregowy, judged_employee: PracownikSzeregowy, opinion_body: str):
        id = len(self.data["opinie"])
        self.data["opinie"].append(Opinia(id, author_employee, judged_employee, opinion_body))

    def delete_opinion(self, opinion):
        self.data['opinie'].remove(opinion)

    def get_user(self, username: str, password: str) -> PracownikSzeregowy | None:
        for pracownik in self.data["pracownicy"]:
            if username == str(pracownik.id) and password == pracownik.haslo:
                return pracownik
        return None

    def get_all_reports(self) -> list[Raport]:
        return self.data['raporty']

    def get_reports_by_user_id(self, user_id: int) -> list[Raport]:
        # standardowe filtrowanie
        return [report for report in self.data['raporty'] if report.judged_employee.id == user_id]
