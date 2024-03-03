def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

        print(f"There are {count_words(file_contents)} in the document.")

        letter_count = count_letters(file_contents)
        letter_occurance_list = []
        for letter in letter_count:
            letter_occurance_list.append({'letter': letter, 'count': letter_count[letter]})

        def sort_on(dict):
            return dict["count"]
        letter_occurance_list.sort(reverse=True, key=sort_on)


        for dict in letter_occurance_list:
            print(f"The character '{dict["letter"]}' appeared {dict["count"]} times.")

def count_words(s):
    return len(s.split())

def count_letters(s):
    s = s.lower()
    letter_count = {}

    for char in s:
        if not char.isalpha():
            continue

        if not (char in letter_count):
            letter_count[char] = 1
        else:
            letter_count[char] += 1

    return letter_count

main()