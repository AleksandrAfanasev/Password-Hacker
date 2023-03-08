import re

string = input()
for letter in ['A', 'C', 'G', 'T']:
    if re.findall(letter, string):
        print(f'{letter}:', len(re.findall(letter, string)))
