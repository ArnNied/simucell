CELL_STATE = {"NEWBORN": "X", "ALIVE": "O"}


class Cell:
    state = "X"
    age = 0
    lifespan = 0

    def __init__(self, lifespan: int) -> None:
        self.lifespan = lifespan
        self.age = 0
        self.state = CELL_STATE["NEWBORN"]

    def __str__(self) -> str:
        return self.state

    def death_check(self):
        return self.age > self.lifespan

    def cycle(self):
        self.age += 1
        if self.age == 2:
            self.state = CELL_STATE["ALIVE"]
        self.death_check()


class SimulCell:
    def __init__(
        self, length: int, width: int, cell_lifespan: int, initial_slot: list
    ) -> None:
        self.length = length
        self.width = width

        self.cell_lifespan = cell_lifespan
        self.initial_slot = initial_slot
        self.filled_slot = initial_slot

        self.board = dict()
        self.board_assemble()

    def board_assemble(self) -> None:
        for i in self.initial_slot:
            self.board[i] = Cell(self.cell_lifespan)

    def board_show(self) -> None:
        for i in range(self.length):
            row = list()
            for j in range(self.width):
                numerical_position = i * self.length + j + 1
                if numerical_position in self.board:
                    row.append(self.board[numerical_position].state)
                else:
                    row.append("∙")
            print("".join(row))

    def initial_slot_validate(self) -> None:
        for index, slot in enumerate(self.initial_slot):
            slot = int(slot)
            if slot > 0 and slot <= self.length * self.width:
                self.board[slot] = Cell(self.cell_lifespan)


simul = SimulCell(10, 10, 2, [1, 2, 3, 4, 5])
simul.board_show()
