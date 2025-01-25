def countVowelConsonants(s):
    """
        Count vowels, consonants, digits, and special characters in the string.
    """
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    digits = "0123456789"
    
    countVowel = countConsonant = countDigit = countSpecialChar = 0
    
    for char in s:
        if char in vowels:
            countVowel += 1
        elif char in consonants:
            countConsonant += 1
        elif char in digits:
            countDigit += 1
        else:
            countSpecialChar += 1
    
    return countVowel, countConsonant, countDigit, countSpecialChar

def reverseString(s):
    """
        Reverse the input string.
    """
    return s[::-1]

def validateInput(s):
    """
        Validate if the input string is not empty.
    """
    return bool(s.strip())

def main():
    word = input("Enter a string to analyze: ").strip()
    
    if not validateInput(word):
        print("Invalid input! Please enter a non-empty string.")
        return
    
    vowels, consonants, digits, specials = countVowelConsonants(word)
    reversed = reverseString(word)
    
    print(f"\nVowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Digits: {digits}")
    print(f"Special Characters: {specials}")
    print(f"Reversed String: {reversed}")

main()