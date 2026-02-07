with open("input_level_1.txt") as fichier:
    input_1 = fichier.read().split()

shift = 1
resolu = ''
for mot in input_1:
    resolu += mot[-shift] + mot[:-shift]
    if mot != input_1[-1]:
        resolu += ' '
print(resolu)


with open("input_level_2.txt") as fichier:
    input_2 = fichier.read().lower()

for i in range(26):
    print('==========' + str(i) + '==========')
    shift = i
    resolu = ''
    for char in input_2:
        if char == ' ':
            resolu += ' '
        elif char == '-':
            resolu += '-'
        elif char == '\n':
            resolu += '\n'
        else:
            nouvelle_ascii = (ord(char) + shift) % 123
            if nouvelle_ascii < 97:
                nouvelle_ascii += 97
            resolu += chr(nouvelle_ascii)
    resolu = resolu.capitalize()
    print(resolu + '\n======================\n')


# with open("input_level_3.txt") as fichier:
#     input_3 = fichier.read().lower()
#
# for i in range(26):
#     print('==========' + str(i) + '==========')
#     shift = i
#     resolu = ''
#     for char in input_3:
#         if char == ' ':
#             resolu += ' '
#         elif char == '-':
#             resolu += '-'
#         elif char == '\n':
#             resolu += '\n'
#         elif char == '.':
#             resolu += '.'
#         elif char == ',':
#             resolu += ','
#         elif char == '_':
#             resolu += '_'
#         else:
#             nouvelle_ascii = (ord(char) + shift) % 123
#             if nouvelle_ascii < 97:
#                 nouvelle_ascii += 97
#             resolu += chr(nouvelle_ascii)
#     resolu = resolu.capitalize()
#     print(resolu + '\n======================\n')
