"""

Furnace_simulation Project


"""
import klm_menu


# import klm_menu


def show_menu(m):
    # display menu to user
    ex = False
    while not ex:
        cmd, menu_name = klm_menu.present_menu("simulation", m)
        ex = cmd == "exit"
        print(cmd)


sim_menu = {
    "menu": "Furnace Simulation Menu",
    "name": "simulation",
    "options": [
        ["new_sim", "New Simulation", "n"],
        ["menu:edit_sim", "Edit Simulation", "e"],
        ["menu:run_sim", "Run Simulation", "r"],
        ["menu:sim_output", "Output", "o"],
        ["exit", "Exit", "x"]
    ],
    "back_option": False,
    "back_to": None
}


edit_sim_menu = {
    "menu": "Edit Simulation Menu",
    "name": "edit_sim",
    "options": [
        ["edit_var", "Edit Variables", "v"],
        ["edit_f_settings", "Edit Furnace Settings", "f"],
        ["edit_sim_settings", "Edit Simulation Settings", "s"],
    ],
    "back_option": True,
    "back_to": "simulation"
}

output_menu = {
    "menu": "Simulation Output Menu",
    "name": "sim_output",
    "options": [
        ["conf_out", "Configure Output", "c"],
        ["plot", "Plot Graph", "p"],
        ["export", "Export Data", "e"],
    ],
    "back_option": True,
    "back_to": "simulation"
}

menu_system = {"simulation": sim_menu,
               "sim_output": output_menu,
               "edit_sim": edit_sim_menu}

show_menu(menu_system)
