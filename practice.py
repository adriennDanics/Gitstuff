def tribonacci(signature, n):
    sign = signature
    if len(sign) > n:
        return sign[0:n]
    else:
        while len(sign) < n:
            signature.append(sign[-1] + sign[-2] + sign[-3])
        return sign


def bowling_pins(arr):
    pose = ['', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I']
    board = "{} {} {} {}\n {} {} {} \n  {} {}  \n   {}  "
    for item in arr:
        pose[item] = ' '
    printing = board.format(pose[7], pose[8], pose[9], pose[10], pose[4], pose[5], pose[6], pose[2], pose[3], pose[1])
    return printing


def elimination(arr):
    arr.sort()
    j = 0
    for i in range(len(arr)-1):
        if arr[j] == arr[j+1]:
            return "{} is the twin".format(i)
        elif arr[j] != arr[j+1]:
            j += 1


def count_arara(n):
    if n % 2 == 0:
        return int(n/2) * "adak "
    else:
        return int(n/2) * "adak " + "anane"


def invert(lst):
    return [i*-1 for i in lst]


def first_non_consecutive(arr):
    j = 0
    for i in range(len(arr)-1):
        if arr[j]+1 != arr[j+1]:
            print(arr[j], arr[j+1], i)
            return arr[j+1]
        elif arr[j] != arr[j+1]:
            j += 1
        else:
            return None


hive = [["b", "e", "e", ".", "b", "e", "e"],
        [".", "e", ".", ".", "e", ".", "."],
        [".", "b", ".", ".", "e", "e", "b"]]

hive2 = [["b", "e", "e", ".", "b", "e", "e"],
        ["e", ".", "e", ".", "e", ".", "e"],
        ["e", "e", "b", ".", "e", "e", "b"]]


def how_many_bees(hive):
    count = 0
    for line in hive:
        for char in line:
            if char == 'b':
                

print(how_many_bees(hive2))