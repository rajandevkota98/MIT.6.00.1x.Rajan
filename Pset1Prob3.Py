# Paste your code into this box 
current = ''
longest = ''

for i in range(len(s)):
 if (s[i-1] <= s[i]):
  current += s[i]
 else:
  current = s[i]
 if len(current) > len(longest):
  longest = current

print("Longest substring in alphabetical order is: " + str(longest))