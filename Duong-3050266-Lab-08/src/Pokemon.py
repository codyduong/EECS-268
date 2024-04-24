class Pokemon:
    def __init__(self, i, name_EN, name_JP) -> None:
        self.id = int(i)
        self.name_EN = name_EN
        self.name_JP = name_JP

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return (
            f"(US name: {self.name_EN:<24} JP name: {self.name_JP:<24} id: {self.id})"
        )

    def __repr__(self):
        return f"{self.id}"
    
