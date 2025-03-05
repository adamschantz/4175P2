import numpy as np
import pandas as pd
from collections import Counter

p = np.array([0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061,  
    0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019,  
    0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001,  
    0.020, 0.001])
#alphabet frequencies
    #read ciphertext from a file
with open("ciphertext.txt", "r") as file:
    ciphertext = file.read().strip()
m = 7  # key length assumption
substrings = [ciphertext[i::m] for i in range(m)]
substring_lengths = [len(sub) for sub in substrings]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def compute_q(substring):
    """computes the frequency vector q for a substring."""
    N = len(substring)
    freq_counts = np.array([substring.count(letter) / N for letter in alphabet])
    return freq_counts

q_vectors = [compute_q(substring) for substring in substrings]

def cyclic_shift(arr, g):
    """shifts an array to the right by g positions."""
    return np.roll(arr, g)

dot_products = []

for i, q in enumerate (q_vectors):
    row = [np.dot(p, cyclic_shift(q, g)) for g in range(26)]
    dot_products.append(row)

#   (A-Z) as rows and yi as columns
df = pd.DataFrame(dot_products).T  

# Rename columns to y1, y2, ..., ym
df.columns = [f"y{i+1}" for i in range(m)]  

# Rename rows to A-Z (g values as shifts)
df.index = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

print(df)