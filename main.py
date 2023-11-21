"""

Furnace_simulation Project


"""
import klm_menu
import sim_env
import plot_sim
import simulate
import edit_sim

# import klm_menu


def new_sim():
    global e
    e = sim_env.new_env()


def run_sim():
    simulate.run_sim(e)


def plot_graph():
    global e
    if e['status']:
        df = plot_sim.prepare_data(e)
        plot_sim.display_graph(df)
    else:
        print("Run Simulation first.")


def export_data():
    global e
    if e['status']:
        df = plot_sim.prepare_data(e)
        plot_sim.export_data(df)
    else:
        print("Run Simulation first.")


def show_menu(m):
    # display menu to user
    global e
    ex = False
    while not ex:
        cmd, menu_name = klm_menu.present_menu("simulation", m)
        ex = cmd == "exit"
        print(cmd)
        if cmd == "new_sim":
            new_sim()

        elif cmd == "run_sim":
            run_sim()

        elif cmd == "plot":
            plot_graph()

        elif cmd == "export":
            export_data()

        elif cmd == "edit_var":
            edit_sim.edit_var(e)

        elif cmd == "edit_f_settings":
            edit_sim.edit_f_settings(e)

        elif cmd == "edit_sim_settings":
            edit_sim.edit_sim_settings(e)

        elif cmd == "conf_out":
            edit_sim.conf_out(e)


sim_menu = {
    "menu": "Furnace Simulation Menu",
    "name": "simulation",
    "options": [
        ["new_sim", "New Simulation", "n"],
        ["menu:edit_sim", "Edit Simulation", "e"],
        ["run_sim", "Run Simulation", "r"],
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

e = {}
new_sim()
show_menu(menu_system)
