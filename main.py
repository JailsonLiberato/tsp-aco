from ui.aco_ui import AntColonyOptimizerUI


class Main:

    def __init__(self):
        self.__ant_colony_ui = AntColonyOptimizerUI()

    def execute(self):
        self.__ant_colony_ui.execute()


main = Main()
main.execute()
