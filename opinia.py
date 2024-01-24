from pracownik_szeregowy import PracownikSzeregowy


class Opinia:
    def __init__(
        self,
        id: int,
        author_employee: PracownikSzeregowy,
        judged_employee: PracownikSzeregowy,
        opinion_body: str
    ):
        self.id = id
        self.author_employee = author_employee
        self.judged_employee = judged_employee
        self.opinion_body = opinion_body
