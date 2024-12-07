def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    

    print(word_count)
    print(char_count)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    char_counts = []

    for char in text:

        if char.isalpha():

            lower_char = char.lower()

            if lower_char in chars:
                chars[lower_char] = chars[lower_char] + 1
            else :
                chars[lower_char] = 1

    
    for key in chars:
        local_chars = {}
        value = chars[key]
        local_chars[key] = value
        char_counts.append(local_chars)

    

    return char_counts







main()