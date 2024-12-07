def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    char_count.sort(reverse=True, key=sort_on)

    print_report(word_count, char_count)

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
        local_chars["char"] = key
        local_chars["count"] = value
        char_counts.append(local_chars)

    

    return char_counts

def sort_on(dict):
    return dict["count"]


def print_report(word_count, char_count):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("\n")
    
    for i in range(len(char_count)):
        dictionary = char_count[i]
        l_char = dictionary["char"]
        l_count = dictionary["count"]
        print(f"The '{l_char}' character was found {l_count} times")
    
    print("-- End report ---")

main()