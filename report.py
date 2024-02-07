from employee import Employee


class Report:
    def __init__(
        self,
        id: int,
        judged_employee: Employee,
        date: str,
        report_body: str,
        is_confirmed: bool = False,
        is_rejected: bool = False
    ):
        self.id = id
        self.judged_employee = judged_employee
        self.date = date
        self.report_body = report_body
        self.is_confirmed = is_confirmed
        self.is_rejected = is_rejected
