import config as cf
from exceptions import CellsAnnihilated
from simucell import SimuCell
from utils import validate_config

if __name__ == "__main__":
    validate_config(cf)
    simulation = SimuCell(
        length=cf.BOARD["LENGTH"],
        width=cf.BOARD["WIDTH"],
        cell_lifespan=cf.CELL_LIFESPAN,
        adjacent_coefficient=cf.ADJACENT_COEFFICIENT,
        initial_cell=cf.INITIAL_CELL,
        max_cycle=cf.MAX_CYCLE,
    )
    try:
        while simulation.cycle_counter != simulation.max_cycle:
            simulation.cycle()
    except CellsAnnihilated:
        print("No cells survived")
    except KeyboardInterrupt:
        print("Simulation aborted")
    finally:
        print("Simulation finished")
        exit()
