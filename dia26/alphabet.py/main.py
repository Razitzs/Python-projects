from re import A
import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

alphabet=pandas.read_csv("dia26/alphabet.py/nato_phonetic_alphabet.csv") 
a_dict={row.letter:row.code for (index,row) in alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word=input("Enter the code word you want to generate: ").upper()

print("\n")
output_list=[]
for letter in word:
    output_list.append(a_dict.get(letter))

print(output_list)

