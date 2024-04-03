alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def create_map():
    map = alphabet.copy()
    return map


def map_text(user_input, map):
    result = ""
    temp = map.pop()
    map.insert(0, temp)
    for x in user_input.lower():
        if x in alphabet:
            source_index = alphabet.index(x)
            mapped_letter = map[source_index]
            result += mapped_letter
        else:
            result += x
    return result


user_input = input("Enter your encrypted sentence: ")
map = create_map()
num = 0
for y in range(0, 26):
    num = num + 1
    result = map_text(user_input, map)
    print("{}. {}".format(num, result))
