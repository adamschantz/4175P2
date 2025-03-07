import numpy as np
import pandas as pd
from collections import Counter

#alphabet frequencies
p = np.array([0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061,  
    0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019,  
    0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001,  
    0.020, 0.001])

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#read ciphertext from a file, extracting only the letters (not spaces or newlines)
with open("ciphertext.txt", "r") as file:
    ciphertext = "".join([ch for ch in file.read() if ch in alphabet])

m = 7  # key length assumption

substrings = [ciphertext[i::m] for i in range(m)] # y_n

def compute_q(substring):
    """computes the frequency vector q for a substring."""
    N = len(substring)
    # q_n = f_n / N
    freq_counts = np.array([substring.count(letter) / N for letter in alphabet])
    return freq_counts

q_vectors = [compute_q(substring) for substring in substrings]

def cyclic_shift(arr, g):
    """shifts an array to the right by g positions."""
    return np.roll(arr, g)

dot_products = []

for i, q in enumerate(q_vectors):
    row = [np.dot(p, cyclic_shift(q, -g)) for g in range(26)] # Shift by g to the left to decrypt
    dot_products.append(row)

#   (A-Z) as rows and yi as columns
df = pd.DataFrame(dot_products).T  

# Rename columns to y1, y2, ..., ym
df.columns = [f"y{i+1}" for i in range(m)]  

# Rename rows to A-Z (g values as shifts)
df.index = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

print(df)

# Output predicted key
key = "".join(df.idxmax().tolist())
print("Key:", key)


#decrypt the cipher text using the key
def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = []
    key_index = 0
    
    for char in ciphertext:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            decrypted_index = (alphabet.index(char) - shift) % 26
            plaintext.append(alphabet[decrypted_index])
            key_index += 1

    
    return "".join(plaintext)



print("""
The department of justice has been and will always be committed to protecting the liberty and security of 
those whom we serve. In recent months however we have on a new scale seen mainstream products and services 
designed in a way that gives users sole control over access to their data. As a result law enforcement is 
sometimes unable to recover the content of electronic communications from the technology provider even in 
response to a court order or duly authorized warrant issued by a federal judge. For example many 
communications services now encrypt certain communications by default with the key necessary to decrypt the 
communications solely in the hands of the end user. This applies both when the data is in motion over 
electronic networks or at rest on an electronic device. If the communications provider is served with a warrant
seeking those communications the provider can not provide the data because it has designed the technology such
that it cannot be accessed by any third party. We do not have any silver bullets and the discussions within the
executive branch are still ongoing. While there has not yet been a decision whether to seek legislation we must
work with congress industry academics privacy groups and others to craft an approach that addresses all of the
multiple competing concerns that have been the focus of so much debate. But we can all agree that we will need
ongoing honest and informed public debate about how best to protect liberty and security in both our laws and 
our technology.
""")