
result = ""

alphabet = [ " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "l",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def create_map(num):
    map = alphabet.copy()
    for i in range(num):
        temp = map.pop()
        map.insert(0, temp)
    return map


def map_text(sentence, map):
    result = ""
    for x in sentence.lower():
        if x in alphabet:
            source_index = alphabet.index(x)
            mapped_letter = map[source_index]
            result += mapped_letter
        else:
            result += x
    return result
    

def convert_to_number(user_input):
    while True:
        try:
            x = int(user_input)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            exit(1)
        if x < 0:
            print("Please enter a positive number.")
            exit(2)
        return x



user_input = input("How many times would you like the letters shifted? ")
num = convert_to_number(user_input)
sentence = input("Your sentence (all lower-case): ")
map = create_map(num)
result = map_text(sentence, map)
print("Here is the encrypted sentence: {}".format(result))