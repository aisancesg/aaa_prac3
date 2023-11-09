from math import log
from typing import List


class TfidfTransformer:
    """
    Для терм-документной матрицы считает tf, idf, tfidf
    """
    def __init__(self):
        self.tf = []
        self.idf = []

    def fit_transform(self, count_matrix: List[list]) -> List[list]:
        """
        Перемножает значения tf_matrix и idf покомпонентно.
        То есть находит tfidf = tf * idf
        """
        self.tf = self.tf_transform(count_matrix)
        self.idf = self.idf_transform(count_matrix)
        for el in self.tf:
            for i in range(len(el)):
                el[i] = round(el[i] * self.idf[i], 3)
        return self.tf

    def tf_transform(self, count_matrix: List[list]) -> List[list]:
        """
        Считает term frequency (= количество повторений / всего)
        для каждого числа* из списка из count_matrix.
        И так для каждого списка, входящего в count_matrix.

        Замечание *: здесь число соответствует слову из документа корпуса,
        если вспомнить, как строилась count_matrix в 1-м задании.
        То есть term frequency = количество повторений слова / всего слов.

        :param count_matrix: терм-документная матрица (в виде списка списков)
        :return: tf_matrix - список списков из значений вышеуказанных
        term frequency
        """
        tf_matrix = []
        for elem in count_matrix:
            tf_vector = []
            for num in elem:
                num = round(num / sum(elem), 3)
                tf_vector.append(num)
            tf_matrix.append(tf_vector)
        return tf_matrix

    def idf_transform(self, count_matrix: List[list]) -> list:
        """
        :param count_matrix: терм-документная матрица (в виде списка списков)
        :return: список значений idf каждого слова, где
        idf = ln((всего документов + 1) / (документов со словом + 1)) + 1

        Замечание: говоря о 'слове', мы понимаем, что за этим
        стоит процесс построения count_matrix из 1-ого задания
        """
        idf = []
        lenght = len(count_matrix[0])
        total_docs = len(count_matrix)
        for i in range(lenght):
            count_docs = 0
            for count_lst in count_matrix:
                if count_lst[i] != 0:
                    count_docs += 1
            idf.append(round(log((total_docs + 1) / (count_docs + 1)) + 1, 1))
        return idf


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)
