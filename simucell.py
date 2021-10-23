from os import system
from time import sleep

from exceptions import CellsAnnihilated
from utils import rng

CELL_STATE = {"NEWBORN": "X", "ALIVE": "O"}


class Cell:
    def __init__(self, lifespan: int) -> None:
        self.lifespan = lifespan
        self.age = 1
        self.state = CELL_STATE["NEWBORN"]

    def death_check(self):
        """Check if `self` should be dead or not"""

        return self.age > self.lifespan

    def cycle(self):
        """Main method for a cycle"""

        self.age += 1
        if self.age == 2:
            self.state = CELL_STATE["ALIVE"]
        self.death_check()


class SimuCell:
    def __init__(
        self,
        length: int,
        width: int,
        cell_lifespan: int,
        initial_cell: list,
        adjacent_coefficient: dict,
        max_cycle: int = -1,
        time_between: float = 0.3,
    ) -> None:
        self.length = length
        self.width = width
        self.board_full_size = length * width

        self.time_between = time_between
        self.adjacent_coefficient = adjacent_coefficient

        self.cell_lifespan = cell_lifespan
        self.initial_cell = initial_cell

        self.cycle_counter = 0
        self.max_cycle = max_cycle

        self.board = dict()
        self.board_assemble()

    def cycle(self) -> None:
        """Main method for a single cycle"""

        self.cycle_counter += 1
        self.board_show()
        self.annihilation_check()

        dead_cells = list()
        for slot, cell in self.board.items():
            cell.cycle()

            if cell.death_check():
                dead_cells.append(slot)

        self.populate_adjacent()
        self.dead_cell_remove(dead_cells)

        sleep(self.time_between)

    def board_assemble(self) -> None:
        """Instantiate  and assign `Cell` to the board"""

        for i in self.initial_cell:
            self.board[i] = Cell(self.cell_lifespan)

    def board_show(self) -> None:
        """Output the board to the console"""

        system("cls")

        for i in range(self.length):
            row = list()
            for j in range(self.width):
                numerical_position = i * self.width + j + 1
                if numerical_position in self.board:
                    row.append(self.board[numerical_position].state)
                else:
                    row.append("∙")
            print("".join(row))

        print(f"Cycle: {self.cycle_counter}/{self.max_cycle}")
        print(f"Cells alive: {len(self.board)}")

    def populate_adjacent(self) -> None:
        """Populate the cells according to condition."""

        alive_adjacent = self.alive_adjacent_get()
        for slot in alive_adjacent:
            if slot not in self.board and rng(
                self.adjacent_coefficient[self.adjacent_alive_count(slot)]
            ):
                self.board[slot] = Cell(self.cell_lifespan)

    def alive_adjacent_get(self) -> list:
        """Returns the adjacent slot of currently alive cell(s)."""

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

            if left > 0 and slot % self.width != 1:
                alive_adjacent.add(left)

            if right <= self.board_full_size and slot % self.width != 0:
                alive_adjacent.add(right)

        alive_adjacent = alive_adjacent ^ set(self.board.keys())

        return list(alive_adjacent)

    def adjacent_alive_count(self, slot: int) -> int:
        """Returns how many adjacent is alive with `slot` as anchor."""

        alive_adjacent = 0

        up = slot - self.width
        down = slot + self.width
        left = slot - 1
        right = slot + 1

        if up in self.board:
            alive_adjacent += 1

        if down in self.board:
            alive_adjacent += 1

        if left in self.board:
            alive_adjacent += 1

        if right in self.board:
            alive_adjacent += 1

        return alive_adjacent

    def dead_cell_remove(self, dead_cells: list) -> None:
        """Remove any dead cells from the board."""

        for slot in dead_cells:
            del self.board[slot]

    def annihilation_check(self) -> None:
        """Raise `CellsAnnihilated` when there's no cell left on the board."""

        if len(self.board) == 0:
            raise CellsAnnihilated
