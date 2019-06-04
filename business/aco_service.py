from model.ant import Ant
from model.graphic import Graphic
import random


class AntColonyOptimizationService:

    def __init__(self, ant_count, alpha, beta, rho, q, iterations, strategy):
        self.__ant_count = ant_count
        self.__alpha = alpha
        self.__beta = beta
        self.__rho = rho
        self.__Q = q
        self.__iterations = iterations
        self.__update_strategy = strategy

    def execute(self, graph: Graphic):
        best_cost = float('inf')
        best_solution = []
        for it in range(self.__iterations):
            ants = [Ant(self, graph) for i in range(self.__ant_count)]
            for ant in ants:
                for i in range(graph.rank - 1):
                    self.__select_next(ant)
                ant.total_cost += graph.matrix[ant.tabu[-1]][ant.tabu[0]]
                if ant.total_cost < best_cost:
                    best_cost = ant.total_cost
                    best_solution = [] + ant.tabu
                self.__update_pheromone_delta(ant)
            self.__update_pheromone(graph, ants)
        return best_solution, best_cost

    @staticmethod
    def __update_pheromone(graph: Graphic, ants: list):
        for i, row in enumerate(graph.pheromone):
            for j, col in enumerate(row):
                for ant in ants:
                    graph.pheromone[i][j] *= ant.colony.rho
                    graph.pheromone[i][j] += ant.pheromone_delta[i][j]

    @staticmethod
    def __update_pheromone_delta(ant):
        ant.pheromone_delta = [[0 for j in range(ant.graph.rank)] for i in range(ant.graph.rank)]
        for _ in range(1, len(ant.tabu)):
            i = ant.tabu[_ - 1]
            j = ant.tabu[_]
            if ant.colony.update_strategy == 1:
                ant.pheromone_delta[i][j] = ant.colony.Q
            elif ant.colony.update_strategy == 2:
                if ant.graph.matrix[i][j] > 0:
                    ant.pheromone_delta[i][j] = ant.colony.Q / ant.graph.matrix[i][j]
            else:
                ant.pheromone_delta[i][j] = ant.colony.Q / ant.total_cost

    @staticmethod
    def __select_next(ant):
        denominator = 0
        for i in ant.allowed:
            denominator += ant.graph.pheromone[ant.current][i] ** ant.colony.alpha * ant.eta[ant.current][
                i] ** ant.colony.beta
        probabilities = [0 for i in range(ant.graph.rank)]
        for i in range(ant.graph.rank):
            try:
                ant.allowed.index(i)
                if denominator > 0:
                    probability = ant.graph.pheromone[ant.current][i] ** ant.colony.alpha * \
                                            ant.eta[ant.current][i] ** ant.colony.beta / denominator
                    print(probability)
                    probabilities[i] = probability
            except ValueError:
                continue
        selected = 0
        rand = random.random()
        for i, probability in enumerate(probabilities):
            rand -= probability
            if rand <= 0:
                selected = i
                break
        if selected in ant.allowed:
            ant.allowed.remove(selected)
        ant.tabu.append(selected)
        ant.total_cost += ant.graph.matrix[ant.current][selected]
        ant.current = selected

    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha):
        self.__alpha = alpha

    @property
    def beta(self):
        return self.__beta

    @beta.setter
    def beta(self, beta):
        self.__beta = beta

    @property
    def update_strategy(self):
        return self.__update_strategy

    @update_strategy.setter
    def update_strategy(self, update_strategy):
        self.__update_strategy = update_strategy

    @property
    def Q(self):
        return self.__Q

    @Q.setter
    def Q(self, Q):
        self.__Q = Q

    @property
    def rho(self):
        return self.__rho

    @rho.setter
    def rho(self, rho):
        self.__rho = rho
