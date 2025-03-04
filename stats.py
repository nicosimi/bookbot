def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(words):
    table = {}
    for word in words:
        for char in word:
            lower_char = char.lower()
            if lower_char not in table:
                table[lower_char] = 0
            table[lower_char] += 1
    return table

def get_char_count(dict):
    chars = []
    while bool(dict):
        chars.append(dict.popitem())
    sorted_chars = sorted(chars, key=lambda k: k[1],reverse= True)
    for char in sorted_chars:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
