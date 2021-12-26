"""Assignment - making a sklearn estimator.

The goal of this assignment is to implement by yourself a scikit-learn
estimator for the OneNearestNeighbor and check that it is working properly.

The nearest neighbor classifier predicts for a point X_i the target y_k of
the training sample X_k which is the closest to X_i. We measure proximity with
the Euclidean distance. The model will be evaluated with the accuracy (average
number of samples corectly classified). You need to implement the `fit`,
`predict` and `score` methods for this class. The code you write should pass
the test we implemented. You can run the tests by calling at the root of the
repo `pytest test_sklearn_questions.py`.

We also ask to respect the pep8 convention: https://pep8.org. This will be
enforced with `flake8`. You can check that there is no flake8 errors by
calling `flake8` at the root of the repo.

Finally, you need to write docstring similar to the one in `numpy_questions`
for the methods you code and for the class. The docstring will be checked using
`pydocstyle` that you can also call at the root of the repo.
"""
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.base import ClassifierMixin
from sklearn.utils.validation import check_X_y
from sklearn.utils.validation import check_array
from sklearn.utils.validation import check_is_fitted
from sklearn.utils.multiclass import check_classification_targets
from sklearn.metrics import pairwise_distances


class OneNearestNeighbor(BaseEstimator, ClassifierMixin):
    "OneNearestNeighbor classifier."

    def __init__(self):  # noqa: D107
        pass

    def fit(self, X, y):
        """X is our features array
        and y is our label vector.
        X and y form a training set.
        """
        X, y = check_X_y(X, y)
        check_classification_targets(y)
        self.classes_ = np.unique(y)

        # XXX fix
        self.X_ = X
        self.y_ = y

        return self

    def predict(self, X):
        """This function predicts our label 
        vector y by computing the distances 
        pairwise and determinig nearest 
        neighbors based on these distances.
        """
        check_is_fitted(self)
        X = check_array(X)
        y_pred = np.full(
            shape=len(X), fill_value=self.classes_[0],
            dtype=self.classes_.dtype
        )

        # XXX fix
        # Compute the distance matrix from the vector array X and self.X_
        dist = pairwise.pairwise_distances(
            X, Y=self.X_, metric='euclidean', n_jobs=1)
        # Get the nearest neighbors by sorting distances 
        nearest_neighbors = np.argsort(dist, axis=1)[:,0]

        y_pred = self.y_[nearest_neighbors]
        return y_pred

    def score(self, X, y):
        """This function computes the score
        of our predictions by indentifying
        the number of right predictions over
        the total number of elements. 
        """
        X, y = check_X_y(X, y)
        y_pred = self.predict(X)

        # XXX fix
        return (y_pred==y).mean()
