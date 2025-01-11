# 5. Reverse the characters in a string.

word = 'All that glitters is not gold.'

reversed_word = word[::-1]

print(reversed_word)

# <--Using loop-->

new_word = 'All that glitters is not gold.'

rev_word = " "

for char in new_word:
    rev_word = char + rev_word

print(rev_word)