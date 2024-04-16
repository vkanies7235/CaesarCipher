alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
common_words = ["the", "be", "to", "of", "and", "in", "for", "that", "have",
                "it", "not", "on", "with", "he", "she", "they", "you", "as", "this", "their",
                "be", "and", "do", "will", "from", "out", "up", "about", "get", "my", "but",
                "by", "would", "go", "me", "just", "some", "could", "then", "than", "people",
                "see", "after", "two", "one", "want", "because", "well", "first", "second"
                ]


def create_map():
    map = alphabet.copy()
    return map


def map_text(user_input, map):
    check = ""
    temp = map.pop()
    map.insert(0, temp)
    for x in user_input.lower():
        if x in alphabet:
            source_index = alphabet.index(x)
            mapped_letter = map[source_index]
            check += mapped_letter
        else:
            check += x
    return check


def check_input(check, common_words):
    count = 0
    for x in common_words:
        if x in check:
            count = count + 1
        if count == 2:
            found = 1
            return found


map = create_map()
user_input = input("Enter your encrypted sentence: ")
found = 0
for y in range(26):
    check = map_text(user_input, map)
    found = check_input(check, common_words)
    if found == 1:
        break
print("Here is your decrypted sentence: {}".format(check))
