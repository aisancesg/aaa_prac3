from typing import List
from collections import defaultdict


class CountVectorizer:
    """
    Преобразует корпус (список текстов) в терм-документную матрицу
    """
    def __init__(self):
        self.vocabulary = []

    def fit_transform(self, corpus: list) -> List[list]:
        """
        Выясняет, каков список всех встречающихся слов (терминов) в корпусе,
        и возвращает терм-документную матрицу (в виде списка списков)
        """
        sentences_dicts = []
        for sentence in corpus:
            words = sentence.lower().split()
            sentence_dict = defaultdict(int)  # type: dict
            for word in words:
                if word not in self.vocabulary:
                    self.vocabulary.append(word)
                sentence_dict[word] += 1
            sentences_dicts.append(sentence_dict)

        count_matrix = []
        for i, sentence in enumerate(corpus):
            count_in_sentence = []
            for termin in self.vocabulary:
                if termin in sentences_dicts[i]:
                    count_in_sentence.append(sentences_dicts[i][termin])
                else:
                    count_in_sentence.append(0)
            count_matrix.append(count_in_sentence)

        return count_matrix

    def get_feature_names(self) -> list:
        """
        Возвращает список всех встречающихся слов в корпусе
        """
        return self.vocabulary


if __name__ == '__main__':
    corpus = [
     'Crock Pot Pasta Never boil pasta again',
     'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
