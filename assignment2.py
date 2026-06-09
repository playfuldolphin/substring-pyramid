# Program: Substring Pyramid
# Author: Noah Wilson
# Date: June 8, 2026
# Description: Prompts the user for a string and prints all growing prefixes
#              followed by all shrinking suffixes of that string.

s = input("Enter string: ")
ls = len(s)

for i in range(1, ls + 1):
    print(s[0:i])

for i in range(0, ls):
    print(s[i:ls])

print("\nThank you for using my program!")
