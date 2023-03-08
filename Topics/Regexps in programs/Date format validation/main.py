import re

string = input()
print(bool(re.match(r'(3[01]|[12][0-9]|[01][1-9])/(1[0-2]|[1-9])/(\d{4})', string)))
