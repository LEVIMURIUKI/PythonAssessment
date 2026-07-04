import re

with open("newsArticle.txt", "r", encoding="utf-8") as file:
    article = file.read()

print(article)

def count_specific_word(text, search_word):
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(search_word.lower())

word = input("Enter a word to search: ")

count = count_specific_word(article, word)

print("Occurrences:", count)

def identify_most_common_word(text):

    if text.strip() == "":
        return None

    words = re.findall(r'\b\w+\b', text.lower())

    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    most_common = max(frequency, key=frequency.get)

    return most_common
common_word = identify_most_common_word(article)

print("Most common word:", common_word)

def calculate_average_word_length(text):

    if text.strip() == "":
        return 0

    words = re.findall(r'\b\w+\b', text)

    total_length = 0

    for word in words:
        total_length += len(word)

    return total_length / len(words)
average = calculate_average_word_length(article)

print("Average word length:", round(average, 2))

def count_paragraphs(text):

    if text.strip() == "":
        return 1

    paragraphs = text.strip().split("\n\n")

    return len(paragraphs)
paragraphs = count_paragraphs(article)

print("Paragraphs:", paragraphs)


def count_sentences(text):

    if text.strip() == "":
        return 1

    sentences = re.findall(r'[.!?]+', text)

    return len(sentences)
sentences = count_sentences(article)

print("Sentences:", sentences)

search_word = input("Enter a word to search for: ")

print()

print("Text Analysis Results")
print("---------------------")

print("Occurrences:", count_specific_word(article, search_word))

print("Most common word:", identify_most_common_word(article))

print("Average word length:",
      round(calculate_average_word_length(article), 2))

print("Paragraphs:", count_paragraphs(article))

print("Sentences:", count_sentences(article))