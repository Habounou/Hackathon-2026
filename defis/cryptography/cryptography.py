with open("input_level_1.txt") as fichier:
    input_1 = fichier.read()

for i in range(26):
    shift = i
    resolu = ''
    for char in input_1:
        if char != ' ':
            resolu += chr(ord(char) + shift)
        else:
            resolu += ' '

    print(resolu)

