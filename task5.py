from typing import List
from task1 import CountVectorizer
from task4 import TfidfTransformer


class TfidfVectorizer(CountVectorizer):
    """
    Для корпуса вычисляет tfidf
    """
    def __init__(self):
        super().__init__()
        self.tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus: list) -> List[list]:
        """
        Получая корпус, строит соответствующую
        терм-документальную матрицу count_matrix,
        для которой потом находит tfidf_matrix
        """
        count_matrix = super().fit_transform(corpus)
        res = self.tfidf_transformer.fit_transform(count_matrix)
        return res


if __name__ == '__main__':
    corpus = [
     'Crock Pot Pasta Never boil pasta again',
     'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
