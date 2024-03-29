class Employee:
    def __init__(
            self,
            id: int,
            haslo: str,
            imie: str,
            nazwisko: str,
            kwalifikacje=None,
            harmonogram=None,
            raport=None
    ):
        self.id = id
        self.haslo = haslo
        self.imie = imie
        self.nazwisko = nazwisko
        self.kwalifikacje = kwalifikacje
        self.harmonogram = harmonogram
        self.raport = raport
        self.oceny: list = []

    def get_full_name(self):
        return f"{self.imie} {self.nazwisko}"
