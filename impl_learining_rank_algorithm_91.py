# impl_learining_rank_algorithm

import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
X = np.array([[1, 2], [1, 3], [2, 3], [3, 4], [2, 5], [1, 6], [2, 6], [3, 2], [4, 1], [5, 2]])
y = np.array([0, 0, 1, 0, 1, 1, 0, 1, 1, 0])  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
svm_rank = SVC(kernel='linear', C=1.0, decision_function_shape='ovo')
svm_rank.fit(X_train, y_train)
y_pred_train = svm_rank.predict(X_train)
y_pred_test = svm_rank.predict(X_test)
print("Train Accuracy: ", mean_squared_error(y_train, y_pred_train))
print("Test Accuracy: ", mean_squared_error(y_test, y_pred_test))
