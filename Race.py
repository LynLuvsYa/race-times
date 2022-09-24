def viewpb():
    temp = 100**100
    val = 0
    with open("racetimes.txt", "r") as t:
        val = t.readline().rstrip()
        while val != "":
            val = float(val)
            if val != "":
                if temp > val: temp = val
            val = t.readline().rstrip()
    print(temp)
def append():
    with open("racetimes.txt", "a") as t: t.write(input("input time \n") + "\n") # appending
answer = ""
while answer != "x" and answer != "X":
    answer = input("input pb to view your personal best, add to append to the list, or x to exit. \n")
    if answer == "pb": viewpb()
    if answer == "add": append()
