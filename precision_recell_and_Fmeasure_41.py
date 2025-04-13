# precision_recell_and_Fmeasure

def calculate_precision_recall_fmeasure(TP, FP, FN):
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    if (precision + recall) != 0:
        fmeasure = 2 * (precision * recall) / (precision + recall)
    else:
        fmeasure = 0
    
    return precision, recall, fmeasure

TP = 3  
FP = 1  
FN = 2  

precision, recall, fmeasure = calculate_precision_recall_fmeasure(TP, FP, FN)
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F-measure: {fmeasure:.2f}")
