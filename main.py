"""

Furnace_simulation Project


"""
import klm_menu


#import klm_menu


def main_function(m):
    # display menu to user
    pass
    klm_menu.display_menu(m)


sim_menu = {
            "menu": "Furname Simualtion Menu",
            "name": "simulation",
            "options": [
                ["new_sim", "New Simulation", "n"],
                ["edit_sim", "Edit Simulation", "e"],
                ["exit", "Exit", "x"]
            ],
            "back_option": False,
            "back_to": None
        }


main_function(sim_menu)
