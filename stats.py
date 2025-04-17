def word_count_f(book_text):
    words = book_text.split()
    return len(words)

def char_count_f(book_text):
    char_count = {}

    for char in book_text:
        if char.lower() not in char_count:
            char_count[char.lower()] = 1
            continue
        char_count[char.lower()] += 1
    return char_count

def sorted_char_count(char_dict):
    sorted_count = []

    for key in char_dict:
        if not key.isalpha():
            continue
        sorted_count.append({"character": key, "count": char_dict[key]})

    for i in range(0,len(sorted_count)):
        max = float("-inf")
        for j in range(i,len(sorted_count)):
            if sorted_count[j]["count"] > max:
                max = sorted_count[j]["count"]
                max_index = j
        temp_index = sorted_count[max_index]
        sorted_count[max_index] = sorted_count[i]
        sorted_count[i] = temp_index

    return sorted_count



    