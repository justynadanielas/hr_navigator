from pracownik_szeregowy import PracownikSzeregowy


class Raport:
    def __init__(
        self,
        id: int,
        judged_employee: PracownikSzeregowy,
        report_body: str
    ):
        self.id = id
        self.judged_employee = judged_employee
        self.report_body = report_body
