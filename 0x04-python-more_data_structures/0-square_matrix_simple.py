#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in range(len(matrix)):
        iner_list = list(map(lambda x: x ** 2, matrix[i]))
        square_matrix.append(iner_list)

    return square_matrix[:]
