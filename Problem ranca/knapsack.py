# Problem ranca - Unazad
import numpy as np
import sys

# Klasa koja opisuje cvor drveta
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Stampanje podataka drveta
    def print_tree(self):
        print(self.data)

# Klasa koja predstavlja problem ranca i metoda koja predstavlja problem resenja unazad        
class Knapsack:
    def __init__(self, num_items, knapsack_size, weights, values):
        self.num_items = num_items
        self.knapsack_size = knapsack_size
        self.weights = weights
        self.values = values
        self.x_solution = None

    # Resavanje problema unazad
    def solve_backwards(self, k, y):
        if k == 0:
            print("F1(%s) = %s * [%s/%s] = %s" %
                  (y, self.values[0], y, self.weights[0], min(1, self.values[k] * np.floor(y / self.weights[k]))))
            sol = self.values[k] * np.floor(y / self.weights[k])
            print("* F1(%s) = %s * [%s/%s] = %s" %
                  (y, self.values[0], y, self.weights[0], min(1, self.values[k] * np.floor(y / self.weights[k]))))
            return sol
        if self.weights[k] > y:
            print("F%s(%s) = max{F%s(%s)}" % (k + 1, y, k, y))
            sol = self.solve_backwards(k - 1, y)
            print("* F%s(%s) = max{F%s(%s)} = %s" % (k + 1, y, k, y, sol))
            return sol
        else:
            print("F%s(%s) = max{F%s(%s), %s + F%s(%s)}" % (k + 1, y, k, y, self.values[k], k, y - self.weights[k]))
            sol = max(self.solve_backwards(k - 1, y),
                      self.solve_backwards(k - 1, y - self.weights[k]) + self.values[k])
            print("* F%s(%s) = max{F%s(%s), %s + F%s(%s)} = %s" %
                  (k + 1, y, k, y, self.values[k], k, y - self.weights[k], sol))
            return sol

    def solve(self):
        i, j = np.where(np.array([self.weights]) == 0)
        self.weights = np.delete(self.weights, j)
        self.values = np.delete(self.values, j)
        self.x_solution = np.zeros(shape=(1, self.num_items))[0]
        self.num_items -= len(j)
        result = [0] * self.num_items

        f_max = self.solve_backwards(self.num_items - 1, self.knapsack_size)
        print("f_max = %s" % f_max)
        print("x = %s" % self.x_solution)


def main():
    #knapsack_size = 4
    #num_items = 4
    #values = np.array([[10, 2, -1, 3]])
    #weights = np.array([[3, 1, 3, 0]])

    #knapsack_size = 8
    #num_items = 5
    #values = np.array([[3, 1, 7, 2, 5]])
    #weights = np.array([[4, 1, 2, 3, 6]])
    
    knapsack_size = 9
    num_items = 4
    values = np.array([[3, 4, 5, 2]])
    weights = np.array([[2, 3, 4, 5]])

    problem = Knapsack(num_items, knapsack_size, weights[0], values[0])
    problem.solve()


if __name__ == '__main__':
    main()
