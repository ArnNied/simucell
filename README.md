# SimuCell
A totally unrealistic cell growth/reproduction simulation.

## How to run
1. Go to directory
2. `py main.py`

## Customizing starting condition
Edit the constants inside `config.py`

### `ADJACENT_COEFFICIENT`
Specifies the chance of a new cell spawning according to it's adjacent alive.

- TYPE: `dict[int, int]`
- DEFAULT: `{1: 0.2, 2: 0.4, 3: 0.6, 4: 0.8} `

### `BOARD`
Specifies the size of the board or slot available.

- TYPE: `dict[str["LENGTH", "WIDTH"], int]`
- DEFAULT: `{"LENGTH": 20, "WIDTH": 80}`

### `CELL_LIFESPAN`
Specifies the lifespan of spawned cell.

- TYPE: `int`
- DEFAULT: `5`

### `INITIAL_CELL`
Specifies the cell(s) slot that will be spawned on the first cycle.

- TYPE: `list`
- DEFAULT: `[randint(1, BOARD["LENGTH"] * BOARD["WIDTH"]) for _ in range(5)]`

### `MAX_CYCLE`
Specifies the cycle to stop the simulation. `-1` for an infinite simulation.

- TYPE: `int`
- DEFAULT: `-1`

### `TIME_BETWEEN`
Specifies the time before clearing the console and showing the new board state.

- TYPE: `int|float`
- DEFAULT: `0.3`
