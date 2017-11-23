hive = [["b", "e", "e", ".", "b", "e", "e"],
        [".", "e", ".", ".", "e", ".", "."],
        [".", "b", ".", ".", "e", "e", "b"]]

def how_many_bees(hive):
    count = 0
    for line in range(len(hive)):
        for char in range(len(hive[line])):
            if hive[line][char] == "b":
                try:
                    if line < 2:
                        if hive[line][char + 1] == "e" and hive[line][char + 2] == "e":
                            count += 1
                        if hive[line + 1][char] == "e" and hive[line + 2][char] == "e":
                            count += 1
                        if hive[line][char - 1] == "e" and hive[line][char - 2] == "e" and char - 1 >= 0 and char - 2 >= 0:
                            count += 1
                        if hive[line - 1][char] == "e" and hive[line - 2][char] == "e" and line - 1 >= 0 and line - 2 >= 0:
                            count += 1
                    else:
                        if hive[line][char - 1] == "e" and hive[line][char - 2] == "e" and char - 1 >= 0 and char - 2 >= 0:
                            count += 1
                        if hive[line - 1][char] == "e" and hive[line - 2][char] == "e" and line - 1 >= 0 and line - 2 >= 0:
                            count += 1
                        if hive[line][char + 1] == "e" and hive[line][char + 2] == "e":
                            count += 1
                except IndexError:
                    continue
    return count

hive3 = ''
hive2 = [["b", "e", "e", ".", "b", "e", "e"],
        ["e", ".", "e", ".", "e", ".", "e"],
        ["e", "e", "b", ".", "e", "e", "b"]]

print(how_many_bees(hive3))