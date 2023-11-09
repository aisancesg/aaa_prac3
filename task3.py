from math import log
from typing import List


def idf_transform(count_matrix: List[list]) -> list:
    """
    :param count_matrix: терм-документная матрица (в виде списка списков)
    :return: список значений idf каждого слова, где
    idf = ln((всего документов + 1) / (документов со словом + 1)) + 1

    Замечание: говоря о 'слове', мы понимаем, что за этим
    стоит процесс построения count_matrix из 1-го задания
    """
    idf = []
    lenght = len(count_matrix[0])
    total_docs = len(count_matrix)
    for i in range(lenght):
        count_docs = 0
        for count_lst in count_matrix:
            if count_lst[i] != 0:
                count_docs += 1
        idf.append(round(log((total_docs + 1)/(count_docs + 1)) + 1, 1))
    return idf


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    idf_matrix = idf_transform(count_matrix)
    print(idf_matrix)
