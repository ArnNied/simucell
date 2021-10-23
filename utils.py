from random import random


def validate_config(cf) -> None:
    if type(cf.BOARD) is not dict:
        raise TypeError("Error: config.BOARD must be a 'dict'")

    if type(cf.BOARD["LENGTH"]) is not int:
        raise TypeError("Error: config.BOARD['LENGTH'] must be an 'int'")
    if cf.BOARD["LENGTH"] < 2:
        raise ValueError("Error: config.BOARD['LENGTH'] must be above 1")

    if type(cf.BOARD["WIDTH"]) is not int:
        raise TypeError("Error: config.BOARD['WIDTH'] must be an 'int'")
    if cf.BOARD["WIDTH"] < 2:
        raise ValueError("Error: config.BOARD['WIDTH'] must be above 1")

    if type(cf.CELL_LIFESPAN) is not int:
        raise TypeError("Error: config.CELL_LIFESPAN must be an 'int'")
    if cf.CELL_LIFESPAN < 1:
        raise ValueError("Error: config.CELL_LIFESPAN must be above 0")

    if type(cf.INITIAL_CELL) is not list:
        raise TypeError("Error: config.INITIAL_CELL must be a 'list'")
    if not all(type(i) is int for i in cf.INITIAL_CELL):
        raise ValueError(
            "Error: Items inside config.INITIAL_CELL must be an 'int'"
        )
    if (
        min(cf.INITIAL_CELL) < 1
        or max(cf.INITIAL_CELL) > cf.BOARD["LENGTH"] * cf.BOARD["WIDTH"]
    ):
        raise ValueError(
            "Error: One or more item inside cf.INITIAL_CELL is out of range"
        )

    if type(cf.MAX_CYCLE) is not int:
        raise TypeError("Error: config.MAX_CYCLE must be an 'int'")
    if cf.MAX_CYCLE == 0 or cf.MAX_CYCLE < -1:
        raise ValueError("Error: config.MAX must be -1 or above 0")


def rng(data: float = None) -> float:
    if data is not None:
        return data >= random()

    return random()
