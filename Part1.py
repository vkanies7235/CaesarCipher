num = int(input("How many times would you like the code shifted? "))
sentence = input("Your sentence (all lower-case): ")
middle = []
result = "ex"


def shiftmiddle():
    for [x] in sentence:
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



def shiftend():
    for [x] in middle:
        if middle[x] != 0:
            for y in range(num):
                middle[x] = middle[x] + 1
                if middle[x] == 27:
                    middle[x] = 1
    for [z] in middle:
        if middle[z] == 1:
            result[0] = "a"
        if middle[z] == 1:
            result[1] = "b"
