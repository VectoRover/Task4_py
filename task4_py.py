import os
path_to_file = "F:/prog/input.txt"
file = open(path_to_file, "r")

try:
    if os.stat(path_to_file).st_size > 0:
        print("file opened successfully")
    if os.stat(path_to_file).st_size == 0:
        print("Error: empty file")
except OSError:
    print("cannot open file")

def count_min(file):
    temp_min1 = 0
    temp_int2 = 0
    i = 0
    string = file.read()
    temp_int = ""
    count = 1
    if len(string) == 0:
        print("Error: empty file")
        exit(-3)
    for index in range(len(string)):
        if (string[index] != " ") or (string[index] != "\n"):
            temp_int += string[index]
        if (string[index] == " ") or (string[index] == "\n") or (index == (len(string) - 1)):
            try:
                temp_min1 = int(temp_int)
                if (i == 0):
                    temp_min2 = temp_min1
                if (temp_min1 == temp_min2) and (i != 0):
                    count += 1
                    temp_min2 = temp_min1
                if (temp_min1 < temp_min2):
                    count = 1
                    temp_min2 = temp_min1
                i += 1
            except ValueError:
                pass
            temp_int = ""
    return count

def Autotest():
    file = open("autotest.txt", "r")
    count = count_min(file)
    if count == 3:
        print("Autotest passed")
    else:
        print("Autotest not passed")

Autotest()
print(count_min(file))




