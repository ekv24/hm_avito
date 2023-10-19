from typing import List


class CountVectorizer:
    """Convert a collection of texts to a matrix of token(word) counts.

    Input:
    Corpus of texts. It is list of strings.

    Parametrs:
    lowercase: convert texts to lowercase or not

    Methods:
    fit_transform: makes matrix of token(word) counts.
    Returns matrix - List[List[int]].

    get_feature_names: makes list of unique tokens (words) from texts.
    Returns List[str]
    """

    def __init__(self, lowercase: bool = True) -> None:
        self.lowercase = lowercase
        self.matrix = []
        self.feature_names = []

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        if self.lowercase:
            for index, task in enumerate(corpus):
                corpus[index] = task.lower()

        for task in corpus:
            list_of_words = task.split()
            for token in list_of_words:
                if token not in self.feature_names:
                    self.feature_names.append(token)

        for index, task in enumerate(corpus):
            list_of_words = task.split()
            dict_of_words = {}
            for token in list_of_words:
                if token in dict_of_words:
                    dict_of_words[token] += 1
                else:
                    dict_of_words[token] = 1
            self.matrix.append([])
            for word in self.feature_names:
                if word in dict_of_words:
                    self.matrix[index].append(dict_of_words[word])
                else:
                    self.matrix[index].append(0)
        return self.matrix

    def get_feature_names(self) -> List[str]:
        return self.feature_names


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
