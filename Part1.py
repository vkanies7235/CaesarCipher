num = int(input("How many times would you like the code shifted? "))
sentence = input("Your sentence (all lower-case): ")
middle = []
result = ""


def shiftmiddle():
    for x in sentence:
        if sentence[x] == "a":
            middle.append(1)
        elif sentence[x] == "b":
            middle.append(2)
        elif sentence[x] == "c":
            middle.append(3)
        elif sentence[x] == "d":
            middle.append(4)
        elif sentence[x] == "e":
            middle.append(5)
        elif sentence[x] == "f":
            middle.append(6)
        elif sentence[x] == "g":
            middle.append(7)
        elif sentence[x] == "h":
            middle.append(8)
        elif sentence[x] == "i":
            middle.append(9)
        elif sentence[x] == "j":
            middle.append(10)
        elif sentence[x] == "k":
            middle.append(11)
        elif sentence[x] == "l":
            middle.append(12)
        elif sentence[x] == "m":
            middle.append(13)
        elif sentence[x] == "n":
            middle.append(14)
        elif sentence[x] == "o":
            middle.append(15)
        elif sentence[x] == "p":
            middle.append(16)
        elif sentence[x] == "q":
            middle.append(17)
        elif sentence[x] == "r":
            middle.append(18)
        elif sentence[x] == "s":
            middle.append(19)
        elif sentence[x] == "t":
            middle.append(20)
        elif sentence[x] == "u":
            middle.append(21)
        elif sentence[x] == "v":
            middle.append(22)
        elif sentence[x] == "w":
            middle.append(23)
        elif sentence[x] == "x":
            middle.append(24)
        elif sentence[x] == "y":
            middle.append(25)
        elif sentence[x] == "z":
            middle.append(26)
        elif sentence[x] == " ":
            middle.append(0)
    return middle



def shiftend():
    for [x] in middle:
        if middle[x] != 0:
            for y in range(num):
                middle[x] = middle[x] + 1
                if middle[x] == 27:
                    middle[x] = 1
    for [z] in middle:
        if middle[z] == 0:
            result[z] = " "
        elif middle[z] == 1:
            result[z] = "a"
        elif middle[z] == 2:
            result[z] = "b"
        elif middle[z] == 3:
            result[z] = "c"
        elif middle[z] == 4:
            result[z] = "d"
        elif middle[z] == 5:
            result[z] = "e"
        elif middle[z] == 6:
            result[z] = "f"
        elif middle[z] == 7:
            result[z] = "g"
        elif middle[z] == 8:
            result[z] = "h"
        elif middle[z] == 9:
            result[z] = "i"
        elif middle[z] == 10:
            result[z] = "j"
        elif middle[z] == 11:
            result[z] = "k"
        elif middle[z] == 12:
            result[z] = "l"
        elif middle[z] == 13:
            result[z] = "m"
        elif middle[z] == 14:
            result[z] = "n"
        elif middle[z] == 15:
            result[z] = "o"
        elif middle[z] == 16:
            result[z] = "p"
        elif middle[z] == 17:
            result[z] = "q"
        elif middle[z] == 18:
            result[z] = "r"
        elif middle[z] == 19:
            result[z] = "s"
        elif middle[z] == 20:
            result[z] = "t"
        elif middle[z] == 21:
            result[z] = "u"
        elif middle[z] == 22:
            result[z] = "v"
        elif middle[z] == 23:
            result[z] = "w"
        elif middle[z] == 24:
            result[z] = "x"
        elif middle[z] == 25:
            result[z] = "y"
        elif middle[z] == 26:
            result[z] = "z"
    return result


middle = shiftmiddle()
result = shiftend()
print("Here is the encrypted sentence: {}".format(result))