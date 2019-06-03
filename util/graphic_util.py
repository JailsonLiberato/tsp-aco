import operator
import matplotlib.pyplot as plot


class GraphicUtil:

    @staticmethod
    def generate_plot(points, path):
        x =[]
        y = []
        for point in points:
            x.append(point[0])
            y.append(point[1])
        y = list(map(operator.sub, [max(y) for i in range(len(points))], y))
        plot.plot(x, y, 'co')

        for _ in range(1, len(path)):
            i = path[_ - 1]
            j = path[_]
            plot.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], color='r', length_includes_head=True)

        plot.xlim(0, max(x) * 1.1)
        plot.ylim(0, max(y) * 1.1)
        plot.show()

