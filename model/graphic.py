class Graphic:

    def __init__(self, cost_matrix: list, rank: int):
        self.__matrix = cost_matrix
        self.__rank = rank
        self.__pheromone = [[1 / (rank * rank) for j in range(rank)] for i in range(rank)]

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, matrix):
        self.__matrix = matrix

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        self.__rank = rank

    @property
    def pheromone(self):
        return self.__pheromone

    @pheromone.setter
    def pheromone(self, pheromone):
        self.__pheromone = pheromone
