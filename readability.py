from cs50 import get_string


def main():
    text = get_string("Text: ")
    letters = sum(c.isalpha() for c in text)
    words = sum(c.isspace() for c in text) + 1
    sentences = sentences_count(text)
    L = 100 * letters / words
    S = 100 * sentences / words
    index = round(0.0588 * L - 0.296 * S - 15.8)
    grade(index)


def sentences_count(text):
    count = 0
    end = {".", "!", "?"}
    for c in text:
        if c in end:
            count += 1
    return count


def grade(i):
    if i < 1:
        print("Before Grade 1")
    elif i >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {i}")


main()