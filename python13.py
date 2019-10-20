numVowels = 0
s = 'aaaaaaaeeueoemmmmmmm'
for char in s:
 if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
  numVowels += 1
print(str(numVowels))