from sklearn.base import BaseEstimator, TransformerMixin


iris = load_iris()

X = iris.data
y = iris.target 


y_names = iris.target_names


test_ids = np.random.permutation(len(X))



X_train = X[test_ids[:-100]]
X_test = X[test_ids[-100:]]

y_train = y[test_ids[:-100]]
y_test = y[test_ids[-100:]]
# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
