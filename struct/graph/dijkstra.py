# coding: utf-8
"""
Поиск кратчайшего пути из вершины графа до всех остальных по алгоритму 
Дейкстры
"""
pd = {'∞': 10 ** 6}  # константа бесконечности


class Matrix:
    def __init__(self, size, infinity=pd['∞']):
        self.size = size
        self.infinity = infinity
        self.__matrix = [[0 for _ in range(size)] for _ in range(size)]

    def create_matrix(self):
        from random import randint

        for j in range(self.size):
            for i in range(self.size):
                if i == j:
                    continue
                elif self.__matrix[i][j]:
                    self.__matrix[j][i] = self.__matrix[i][j]
                else:
                    self.__matrix[j][i] = randint(1, 20)
                    self.__matrix[i][j] = self.__matrix[j][i]

    @property
    def matrix(self):
        return self.__matrix


def search(N, S, matrix):
    """
    Функция поиска по алгоритму Дейкстры. 
    Граф с |N| вершинами и  |E| ребрами.
    Сложность - (временная)
                Средний = O((|N|+|E|log(|N|))
                Худший = O((|N|+|E|log(|N|))
                (пямять)
                Худший = O(|N|)
    
    :param N: число вершин
    :param S: вершина, относительно которой ведем поиск
    :param matrix: матрица смежности
    :return: список кратчайших путей до вершин
    """
    weight = [pd['∞'] for _ in range(N)]
    weight[S] = 0
    valide = [True for _ in range(N)]
    # для каждой вершины
    for i in range(N):
        min_weight = pd['∞'] + 1
        id_min_weight = -1

        for i in range(N):
            if valide[i] and weight[i] < min_weight:
                min_weight = weight[i]
                id_min_weight = i
        for i in range(N):
            sum_weight = weight[id_min_weight] + matrix[id_min_weight][i]
            if sum_weight < weight[i]:
                weight[i] = sum_weight
        # проставляем вершину как пройденную
        valide[id_min_weight] = False
    return weight
