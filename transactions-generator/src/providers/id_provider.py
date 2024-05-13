class IdProvider:
    id_counter = 0
    instance = None

    def __new__(self) -> None:
        if self.instance is None:
            self.instance = super().__new__(self)
        return self.instance

    def get_next(self) -> int:
        self.id_counter += 1
        return self.id_counter
