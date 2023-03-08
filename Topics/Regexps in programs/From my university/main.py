import re 

string = input()
print(bool(re.match(r'From: \w+@ucsc.cl', string)))
