import re


def count_specific_word(text, search_word):
    """
    Counts the number of occurrences of a specified word in the text.
    Returns 0 if no matches are found.
    """
    words = re.findall(r"\b\w+\b", text.lower())
    return words.count(search_word.lower())


def identify_most_common_word(text):
    """
    Returns the most common word in the text.
    Returns None if the text is empty.
    """
    words = re.findall(r"\b\w+\b", text.lower())

    if not words:
        return None

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return max(frequency, key=frequency.get)


def calculate_average_word_length(text):
    """
    Calculates the average word length.
    Excludes punctuation.
    Returns 0 if the text contains no words.
    """
    words = re.findall(r"\b\w+\b", text)

    if not words:
        return 0

    total_length = 0

    for word in words:
        total_length += len(word)

    return total_length / len(words)


def count_paragraphs(text):
    """
    Counts paragraphs separated by blank lines.
    Returns 0 if the text is empty.
    """
    if text.strip() == "":
        return 0

    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


def count_sentences(text):
    """
    Counts sentences ending with '.', '!' or '?'.
    Returns 0 if the text is empty.
    """
    if text.strip() == "":
        return 0

    return len(re.findall(r"[.!?]+", text))


def main():
    try:
        with open("newsArticle.txt", "r", encoding="utf-8") as file:
            article = file.read()
    except FileNotFoundError:
        print("Error: newsArticle.txt was not found.")
        return

    while True:
        search_word = input("Enter a word to search for: ").strip()

        if search_word == "":
            print("Please enter a valid word.\n")
            continue

        print("\n===== Text Analysis Results =====")
        print(f"Occurrences of '{search_word}': {count_specific_word(article, search_word)}")
        print(f"Most common word: {identify_most_common_word(article)}")
        print(f"Average word length: {calculate_average_word_length(article):.2f}")
        print(f"Number of paragraphs: {count_paragraphs(article)}")
        print(f"Number of sentences: {count_sentences(article)}")

        choice = input("\nWould you like to search another word? (y/n): ").strip().lower()

        if choice != "y":
            print("\nThank you for using the Text Analysis Program.")
            break


if __name__ == "__main__":
    main()