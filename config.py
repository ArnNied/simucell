from random import randint

ADJACENT_COEFFICIENT = {
    1: 0.2,  # INT: FLOAT
    2: 0.4,  # INT: FLOAT
    3: 0.6,  # INT: FLOAT
    4: 0.8,  # INT: FLOAT
}

BOARD = {
    "LENGTH": 20,  # POSITIVE INTEGER
    "WIDTH": 80,  # POSITIVE INTEGER
}

CELL_LIFESPAN = 5  # POSITIVE INTEGER

INITIAL_CELL_TOTAL = 5  # POSITIVE INTEGER

INITIAL_CELL = [
    randint(1, BOARD["LENGTH"] * BOARD["WIDTH"])
    for _ in range(INITIAL_CELL_TOTAL)
]  # RANDOMLY FILLED CELL
# INITIAL_CELL = [1,2,3,4] # LIST FILLED WITH POSITIVE INTEGER

MAX_CYCLE = -1  # POSITIVE INTEGER | -1 FOR INFINITE LOOP

TIME_BETWEEN = 0.3  # FLOAT IN SECONDS
