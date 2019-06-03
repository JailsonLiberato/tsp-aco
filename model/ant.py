from util.graphic_util import GraphicUtil
from business.aco_service import AntColonyOptimizationService
import random


class Ant:

    def __init__(self, aco: AntColonyOptimizationService, graph: GraphicUtil):
        self.__colony = aco
        self.__graph = graph
        self.__total_cost = 0.0
        self.__tabu = []
        self.__pheromone_delta = []
        self.__allowed = [i for i in range(graph.rank)]
        self.__eta = [[0 if i == j else 1 / graph.matrix[i][j] for j in range(graph.rank)] for i in
                      range(graph.rank)]  # heuristic information
        start = random.randint(0, graph.rank - 1)
        self.__tabu.append(start)
        self.__current = start
        self.__allowed.remove(start)

    @property
    def colony(self):
        return self.__colony

    @colony.setter
    def colony(self, colony):
        self.__colony = colony

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph):
        self.__graph = graph

    @property
    def total_cost(self):
        return self.__total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        self.__total_cost = total_cost

    @property
    def tabu(self):
        return self.__tabu

    @tabu.setter
    def tabu(self, tabu):
        self.__tabu = tabu

    @property
    def pheromone_delta(self):
        return self.__pheromone_delta

    @pheromone_delta.setter
    def pheromone_delta(self, pheromone_delta):
        self.__pheromone_delta = pheromone_delta

    @property
    def allowed(self):
        return self.__allowed

    @allowed.setter
    def allowed(self, allowed):
        self.__allowed = allowed

    @property
    def eta(self):
        return self.__eta

    @eta.setter
    def eta(self, eta):
        self.__eta = eta

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, current):
        self.__current = current
