word = input("Please enter a word: ")
vowels = 0
consonants = 0

for i in word:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("Total vowels in this word = ", vowels)
print("Total consonants in this word = ", consonants)
