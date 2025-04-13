# spelling_correction_model_using_edit_distance_algorithms

import numpy as np
def levenshtein_distance(str1, str2):
    dp = np.zeros((len(str1) + 1, len(str2) + 1), dtype=int)
    for i in range(len(str1) + 1): dp[i][0] = i
    for j in range(len(str2) + 1): dp[0][j] = j
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + (str1[i-1] != str2[j-1]))
    return dp[len(str1)][len(str2)]

def correct_spelling(word, dictionary):
    return min(dictionary, key=lambda w: levenshtein_distance(word, w))
dict_words = ["apple", "banana", "grape", "orange", "pear"]
misspelled_word = "bbanana"
corrected_word = correct_spelling(misspelled_word, dict_words)
print(f"Corrected Word: {corrected_word}")
