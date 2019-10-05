"""
decode the emails in the authconfig groups phishing links
"""

import sys

input_string = sys.argv[1]
alpha = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"
first = input_string[0]
str_cp = input_string[2:]

#may need tweaking
for i in range(0, len(alpha)):
    str_cp = str_cp.replace(first + "0" + str(i) + "a", alpha[i])
for i in range(0, len(vowels)):
    str_cp = str_cp.replace(first + str(i), vowels[i])
for i in range(4,3,-1):
    str_cp = str_cp.replace(first*i, "@")

print(str_cp)
