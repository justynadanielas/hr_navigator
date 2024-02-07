from employee import Employee


class Opinion:
    def __init__(
        self,
        id: int,
        author_employee: Employee,
        judged_employee: Employee,
        opinion_body: str
    ):
        self.id = id
        self.author_employee = author_employee
        self.judged_employee = judged_employee
        self.opinion_body = opinion_body
