# evaluation tookit to measure average precision

from sklearn.metrics import precision_score, recall_score, f1_score, average_precision_score
import numpy as np
y_true = np.array([1, 0, 1, 1, 0, 1, 0])
y_pred = np.array([0.9, 0.1, 0.8, 0.7, 0.2, 0.9, 0.3])
ap_score = average_precision_score(y_true, y_pred)
precision = precision_score(y_true, (y_pred > 0.5)) 
recall = recall_score(y_true, (y_pred > 0.5))
f1 = f1_score(y_true, (y_pred > 0.5))
print(f"Average Precision (AP): {ap_score:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
