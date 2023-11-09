from typing import List


def tf_transform(count_matrix: List[list]) -> List[list]:
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


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    tf_matrix = tf_transform(count_matrix)
    print(tf_matrix)
