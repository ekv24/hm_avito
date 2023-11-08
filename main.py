from typing import List
import numpy as np


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


class TfidfTransformer:
    """Transform a matrix of token(word) counts into TF-IDF values.

    Methods:
    tf_transform: computes the Term Frequency (TF) of tokens in a count matrix.
    Returns matrix - List[List[float]].

    idf_transform: computes the Inverse Document Frequency (IDF) of tokens in a count matrix.
    Returns a list of IDF values - List[float].

    fit_transform: combines TF and IDF to produce TF-IDF values from a count matrix.
    Returns matrix of TF-IDF values - List[List[float]].
    """
    @staticmethod
    def tf_transform(count_matrix: List[List[int]]) -> List[List[int]]:
        count_matrix_tf = np.array(count_matrix)
        sums = np.sum(count_matrix_tf, axis=1)
        sums = sums.reshape(-1, 1)
        return count_matrix_tf / sums

    @staticmethod
    def idf_transform(count_matrix: List[List[int]]) -> List[int]:
        count_matrix = (np.array(count_matrix) > 0).astype(int)
        total_docs = count_matrix.shape[0]
        doc_freq = count_matrix.sum(axis=0)
        idf = np.log((total_docs + 1) / (doc_freq + 1)) + 1
        return np.around(idf, 3)

    def fit_transform(self, count_matrix: List[List[int]]) -> List[List[int]]:
        tfs = self.tf_transform(count_matrix)
        idfs = self.idf_transform(count_matrix)
        result = []
        for doc in tfs:
            result.append([round(t * i, 3) for t, i in zip(doc, idfs)])
        return result


class TfidfVectorizer(CountVectorizer):
    """Convert a collection of texts to a matrix of TF-IDF values.

    This class inherits from CountVectorizer and composes with TfidfTransformer to
    convert a collection of texts into a matrix of TF-IDF values.

    Input:
    Corpus of texts. It is a list of strings.

    Parameters:
    lowercase: convert texts to lowercase or not

    Methods:
    fit_transform: converts a corpus into a matrix of TF-IDF values.
    Returns matrix of TF-IDF values - List[List[float]].
    """
    def __init__(self, lowercase: bool = True) -> None:
        super().__init__(lowercase)
        self.tfidf_ = TfidfTransformer()

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        count_matrix = super().fit_transform(corpus)
        return self.tfidf_.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print("-" * 50)
    print(tfidf_matrix)
