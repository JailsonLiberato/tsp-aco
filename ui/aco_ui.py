from business.aco_service import AntColonyOptimizationService
from model.graphic import Graphic
import plot
import math


class AntColonyOptimizerUI:

    def __init__(self):
        self.__aco_service = AntColonyOptimizationService(ant_count=10, alpha=1, beta=5, rho=0.5, q=100,
                                                          iterations=2500)

    def execute(self):
        self.__initialize_cities_points()
        self.__create_graphic()

    def __initialize_cities_points(self):
        cities = []
        points = []
        with open('./data/chn31.txt') as f:
            for line in f.readlines():
                city = line.split(' ')
                cities.append(dict(index=int(city[0]), x=int(city[1]), y=int(city[2])))
                points.append((int(city[1]), int(city[2])))
        cost_matrix = []
        rank = len(cities)
        for i in range(rank):
            row = []
            for j in range(rank):
                row.append(self.__calculate_distance(cities[i], cities[j]))
            cost_matrix.append(row)

    @staticmethod
    def __calculate_distance(city1: dict, city2: dict):
        return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)

    def __create_graphic(self):
        graph = Graphic(self.__aco_service)
        path, cost = self.__aco_service.execute(graph)
        print('cost: {}, path: {}'.format(cost, path))
        plot(self.__aco_service.points, path)
