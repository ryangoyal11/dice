import random
b = "c"
while b == "c":
    x = input("Would you like to roll a dice?")
    if x == "Y":
        no = random.randint(1, 6)
        if no == 1:
            print(0)
        if no == 2:
            print("0    0")
        if no == 3:
            print("0  0  0")
        if no == 4:
            print("0 0   0 0")
        if no == 5:
            print("0 0 0 0 0")
        if no == 6:
            print("00 00 00")
