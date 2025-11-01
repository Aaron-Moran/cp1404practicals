"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 30 minutes
Actual: 26 minutes
"""

def main():
    """Count word occurrences from input, then print sorted and aligned results."""
    text = input("text: ")
    words = text.lower().split()

    word_to_count = {}
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

    sorted_words = sorted(word_to_count)

    width = max((len(word) for word in sorted_words), default = 0)

    for word in sorted_words:
        print(f'{word:{width}} : {word_to_count[word]}')


main()