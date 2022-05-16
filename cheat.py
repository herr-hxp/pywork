import re
from pyparsing import line

words = []
file = open('svenska-ord.txt', encoding='utf-8')

def startwith():
    query_start = input("What letters does your word start with?:\n")
    pattern_start = f'^{query_start}'
    for line in file.readlines():
        if re.findall(pattern_start, line.rstrip('\n')):
           line = words.append(line.rstrip('\n'))
           

def endwith():
    query_end = input("What letters does your word end with?:\n")
    pattern_end = f'({query_end}$)'
    for line in file.readlines():
        if re.findall(pattern_end, line.rstrip('\n')):
            line = words.append(line.rstrip('\n'))

def contains():
    query_contain = input("What letters does your word contain?:\n")
    pattern_contain = f'({query_contain})'
    for line in file.readlines():
        if re.findall(pattern_contain, line.rstrip('\n')):
            line = words.append(line.rstrip('\n'))

def position():
    query_pos = input("Choose a position for each letter, for wildcards use '.'. Amount of letters(dots) equals length of word.\n")
    pos = list(query_pos)
    if len(pos) <= 3:
        pat1 = f'^{pos[0]}{pos[1]}{pos[2]}$'
        for line in file.readlines():
            if re.findall(pat1, line.rstrip('\n')):
                line = words.append(line.rstrip('\n'))
    elif len(pos) <= 4:
        pat2 = f'^{pos[0]}{pos[1]}{pos[2]}{pos[3]}$'
        for line in file.readlines():
            if re.findall(pat2, line.rstrip('\n')):
                line = words.append(line.rstrip('\n'))
    elif len(pos) <= 5:
        pat3 = f'^{pos[0]}{pos[1]}{pos[2]}{pos[3]}{pos[4]}$'
        for line in file.readlines():
            if re.findall(pat3, line.rstrip('\n')):
                line = words.append(line.rstrip('\n'))
    elif len(pos) <= 6:
        pat4 = f'^{pos[0]}{pos[1]}{pos[2]}{pos[3]}{pos[4]}{pos[5]}$'
        for line in file.readlines():
            if re.findall(pat4, line.rstrip('\n')):
                line = words.append(line.rstrip('\n'))

def htmlsearch():
    htmlquery = ""
    pattern_start = f'^{htmlquery}'
    for line in file.readlines():
        if re.findall(pattern_start, line.rstrip('\n')):
           line = words.append(line.rstrip('\n'))
    complete_words = [x for x in words if len(x) <= 6]
    print(complete_words)


# while True:
#     prompt = "What would you like to search for?\n"
#     prompt += "1: Search for word starting with:\n"
#     prompt += "2: Search for word ending with:\n"
#     prompt += "3: Search for word containing:\n"
#     prompt += "4: Search for letters in a position\n"
#     prompt += "Choose: "
#     command = input(prompt)
#     if command == "1":
#         print("- Search for word starting with - \n")
#         startwith()
#         complete_words = [x for x in words if len(x) <= 6]
#         print(complete_words)
#         break
#     if command == "2":
#         print("- Search for word ending with - \n")
#         endwith()
#         complete_words = [x for x in words if len(x) <= 6]
#         print(complete_words)
#         break
#     if command == "3":
#         print("- Search for word containing - \n")
#         contains()
#         complete_words = [x for x in words if len(x) <= 6]
#         print(complete_words)
#         break
#     if command == "4":
#         print("- Search for letters in a position - \n")
#         position()
#         complete_words = [x for x in words if len(x) <= 6]
#         print(complete_words)
#         break
#     else:
#         print("unknown command.. try again..")
