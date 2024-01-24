from opinia import Opinia
from pracownik_szeregowy import PracownikSzeregowy


class BazaDanych:
    def __init__(self):
        self.data = {}
        self.data["lista_pracownikow"] = [
            PracownikSzeregowy(1, 'maslo', 'Adam', 'Adamski'),
            PracownikSzeregowy(2, 'maslo', 'Jan', 'Kowalski'),
            PracownikSzeregowy(3, 'maslo', 'Anna', 'Nowak'),
            PracownikSzeregowy(4, 'maslo', 'Marta', 'Wiśniewska'),
            PracownikSzeregowy(5, 'maslo', 'Piotr', 'Kaczmarek')
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

    # to niekoniecznie potrzebne
    def add_employee(self, employee: PracownikSzeregowy):
        self.data["lista_pracownikow"].append(employee)

    def get_employee_by_id(self, id: int) -> PracownikSzeregowy | None:
        for employee in self.data["lista_pracownikow"]:
            if employee.id == id:
                return employee
        return None