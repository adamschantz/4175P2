'''
Calculate the index of coincidences for the above ciphered text by assuming m = 6, 7, 8 and verify
that the index of coincidences method supports our guess that m = 7. You may manually type the
reason why your calculations below support our guess.
• Step(1): m = 6, Split the cipher text into six substrings y1, y2, y3, y4, y5, y6 as explained in
the class, and calculate the index of coincidence for each substring. You will have to list six
numbers here (not just their average).
• Step(2): m = 7, Split the cipher text into seven substrings y1, y2, y3, y4, y5, y6, y7 as explained
in the class, and calculate the index of coincidence for each substring. You will have to get
seven numbers here.
• Step(3): m = 8, Split the cipher text into eight substrings y1, y2, y3, y4, y5, y6, y7, y8 as ex-
plained in the class, and calculate the index of coincidence for each substring. You will have
to get eight numbers here.
• Step(4): Do your outputs verify that m = 7 is the correct guess? Say yes or no, and briefly
explain your reason.
'''

import random

cipher_text = (
    "KBWWMRSINEXVVGWDMLBKUVBSLJGWEUFWEKDCUDPIAKSYUHUOAKNWWBQHIILXKVAEALAMNA"
    "SYJMGCFUMWVCTAKSGYBJGJYOAWOOVMWKDGAELWVMPLDIFMPUZFQWOMTOVBSOMQFRHWPAES"
    "CYKXMPERCFLBTWRGHKWFMTNKTVFKVLNBKGKUYKBOPWUCFTECQKBSMOKNVMMLMTKJIDXKQF"
    "KLGEWXWIUUVMUKKILAMKJUULTIUSIYKNTVDRQWGNQJTYEXVVAJMGFMVADYKNVCTCYLHZGU"
    "FPWKBJWTIFMMPLFZWEMELIIFBKEGDGMGQESKCGGAHJFGLAMVWTBFHTQYPJJHDKVVLWOMPA"
    "ELWLXQFJYLHIEGLLLHZFWIIJWCNQROLAWTAQYVPITJRHLBAUMVXTRIHWUYJTTLMUAWYWTW"
    "OUEITGERHQVWOELHAVIVAFHKLMTNZWWLVQOVHUKGRLTYJMIKFTIEFCPATULBWPKSSVXNCM"
    "CNOBBJLYYCXGPWTYKLITQKIVXKTQGNLAMEGDGMGQESKCGGAUGCYDRQPLYYZTVFKFZLAMGF"
    "UOKXZVZZMSIXNAVMTHBJOYYFMPGVRNSBAKFDILBWPGMYJXTGUKLGGQEFVNOHZMKFLSMZGK"
    "KIFTVGDVWLKWPATXWOQEWZZLAMEGDGMGQESKCGGARJFPAWMTAJMWKDGVNCLAIYSILSGBUW"
    "VEAGOVZFMWVWOELHAVIVAFHKMPGHIINBLGJTUFGWVHIINBLGLYYVTBCTVWSNAGAKBSLLGK"
    "ZAFXLVZVNWVPPGCIYRAWUYNZTBKLTUFGWVTVUUVMUKVXTRIPQKBAKLRSINQPMFGEILAIXW"
    "RHQLQNNVLTNTNWKMSGLVZVXALKWKJCGGAYAKBAGBJWVRWVCVAMYTKIPUYUJXAVACFGGOQA"
    "EAOAQNWKBWKMJSJHGMGGLSYWGIFWTCKBWPOYYLAMTLFMWXSNWXCKEIVAFHOXUWKKQGKSYA"
    "KBUHVIJVMKBVFMJNJRIESUYEBKUHICNTKAYIIMIACFUILAMTKKIUKIHLRHSIXTGRWZMPCL"
    "RXVKMUKVMSETQXKBWFCNLZJDXKQEGYLBVIUFHUXZPKKBSMPCNVVWXVVZVZGVCUGWMGFCEZ"
    "UYTTBGTLNOXKCFRFDTOTWVNZTBYWNCDEVGWUIFZWKFXBGGMULRHVBVHGIGWWXWTCCUWMDS"
    "KYSUWWLYIOUMULKIHKWVWTNDBJGJKSSGLUWTOJBBAAEVGMPQMIFSPACFUIMKBGUYHGEWIQ"
)

# calculating individual coincidence index
def coincidence_index(freqs):
    numerator = 0
    denominator = sum(freqs) * (sum(freqs)-1)
    for i in range(len(freqs)):
        numerator += freqs[i] * (freqs[i]-1)
    return numerator / denominator

# putting all ci's in a list
def all_ci(all_freqs):
    vals = []
    all_ci = []
    for freq in all_freqs:
        vals.append(list(freq.values()))
    for val in vals:
        all_ci.append(coincidence_index(val))
    return all_ci

# getting the frequencies of each letter in each substrings
def get_freq(substrings):
    all_freqs = []
    for i in range(0, len(substrings)):
        all_freqs.append({c: substrings[i].count(c) for c in substrings[i]})
    return all_freqs

def main():
    for i in range(6, 9):
        n = len(cipher_text) // i       # length of substrings
        substrings = [cipher_text[j:j+n] for j in range(0, len(cipher_text), n)]        # splitting substrings
        freqs = get_freq(substrings)        # getting all frequencies for all substrings
        indices = all_ci(freqs)     # getting all coincidence indices for all substrings
        
        print(f"\nIndex of Coinicidence Values for m = {i}:\n")
        for i, index in enumerate(indices):
            print(f"y{i}: {index:.5f}")
    print("The best fit is m = 7 because that contains the Index of Coincidence closest to 0.065")
if __name__ == '__main__':
     main()   
