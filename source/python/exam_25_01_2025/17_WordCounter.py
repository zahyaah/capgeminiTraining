def countWords(sentence):
    """ Count the occurrences of each word in the given sentence. """
    
    wordCounts = {}
    words = sentence.split()
    for word in words:
        word = word.lower()  
        wordCounts[word] = wordCounts.get(word, 0) + 1
    return wordCounts


def displayWordCounts(wordCounts):
    """Display the word counts in a readable format."""

    print("\nWord Count:")

    for word, count in wordCounts.items():
        print(f"{word}: {count}")

def getValidatedInput(prompt):
    """Get and validate a non-empty string input from the user."""

    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        print("Invalid input! Please enter a non-empty sentence.")


def main():
    while True:
        sentence = getValidatedInput("Enter a sentence (or type 'exit' to quit): ")
        if sentence.lower() == "exit":
            print("Goodbye!")
            break
        wordCounts = countWords(sentence)
        displayWordCounts(wordCounts)


main()