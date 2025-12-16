def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}

    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts 

def sort(item):
    return item["num"]

def sort_char(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort)
    return sorted_list

