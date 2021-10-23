from os import system
from time import sleep

CELL_STATE = {"NEWBORN": "X", "ALIVE": "O"}


class Cell:
    state = "X"
    age = 0
    lifespan = 0

    def __init__(self, lifespan: int) -> None:
        self.lifespan = lifespan
        self.age = 1
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


class SimuCell:
    def __init__(
        self, length: int, width: int, cell_lifespan: int, initial_slot: list
    ) -> None:
        self.length = length
        self.width = width
        self.board_full_size = length * width

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
            if slot > 0 and slot <= self.board_full_size:
                self.board[slot] = Cell(self.cell_lifespan)

    def alive_adjacent_get(self) -> list:
        alive_adjacent = set()
        for slot in self.board.keys():
            up = slot - self.width
            down = slot + self.width
            left = slot - 1
            right = slot + 1

            if up > 0:
                alive_adjacent.add(up)
            if down <= self.board_full_size:
                alive_adjacent.add(down)
            if left > 0 and slot % self.width - 1 > 0:
                alive_adjacent.add(left)
            if (
                right <= self.board_full_size
                and slot % self.width + 1 <= self.width
            ):
                alive_adjacent.add(right)

        alive_adjacent = alive_adjacent ^ set(self.board.keys())

        return list(alive_adjacent)

    def populate_adjacent(self) -> None:
        alive_adjacent = self.alive_adjacent_get()
        for slot in alive_adjacent:
            if slot not in self.board:
                self.board[slot] = Cell(self.cell_lifespan)

    def dead_cells_remove(self, dead_cells: list) -> None:
        for slot in dead_cells:
            del self.board[slot]

    def cycle(self) -> None:
        dead_cells = list()
        for slot, cell in self.board.items():
            cell.cycle()

            if cell.death_check():
                dead_cells.append(slot)

        self.populate_adjacent()
        self.dead_cells_remove(dead_cells)


simul = SimuCell(11, 11, 2, [61])

while True:
    system("cls")
    simul.board_show()
    simul.cycle()
    sleep(0.5)
