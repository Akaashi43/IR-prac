# train_ranking_model_labbeled_data

import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, ndcg_score
X = np.array([
    [1, 2],  
    [1, 3],  
    [2, 3],  
    [3, 4],  
    [2, 5],  
    [1, 6],  
    [2, 6],  
    [3, 2], 
    [4, 1],  
    [5, 2],  
])
y = np.array([0, 0, 1, 0, 1, 1, 0, 1, 1, 0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
svm_rank = SVC(kernel='linear', C=1.0, decision_function_shape='ovo')  
svm_rank.fit(X_train, y_train)
y_pred_train = svm_rank.predict(X_train)
y_pred_test = svm_rank.predict(X_test)
train_mse = mean_squared_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)
print("Train MSE: ", train_mse)
print("Test MSE: ", test_mse)
y_true = np.array([[0, 1], [0, 1], [1, 0], [1, 0]]) 
y_pred = np.array([[0.2, 0.7], [0.1, 0.9], [0.8, 0.4], [0.9, 0.2]]) 
ndcg = ndcg_score(y_true, y_pred)
print("NDCG Score: ", ndcg)
