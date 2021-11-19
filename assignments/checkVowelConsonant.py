def checkVowelConsonant(ch):
    if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        return "Vowel"
    else:
        return "Consonant"


ch = input("Enter a character:: ")
print(checkVowelConsonant(ch.upper()))
