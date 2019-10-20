word = input("Enter the name ")
current = ''
longest = ''

for i in range(len(s)):
 if (s[i] >= s[i-1]):
  current += s[i]
 else:
  current = s[i]
 if len(current) > len(longest):
  longest = current

print("Longest substring in alphabetical order is: " + longest)