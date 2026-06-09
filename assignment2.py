s = input("Enter string: ")
ls = len(s)

for i in range(1, ls + 1):
    print(s[0:i])

for i in range(0, ls):
    print(s[i:ls])

print("\nThank you for using my program!")
