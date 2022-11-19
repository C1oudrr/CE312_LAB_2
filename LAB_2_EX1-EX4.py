def EX1():
    print("Exercise 1")
    array = [5, 7, 9, 11, 13]

    print(array)

    lenarray = len(array)

    ans = sum(array)

    print(ans)
    print(lenarray)
    inputnumber()

def EX2():
    print("Exercise 2")
    array1 = [7, 5, 10, 14, 3, 9, 7]
    array2 = [9, 10, 3, 4, 2, 5, 7, 1]

    lenarray = len(array1), len(array2)

    print(lenarray)

    array1.insert(15, 8)

    indexarray1 = array1.index(7)
    indexarray2 = array2.index(7)

    print(indexarray1)
    print(indexarray2)

    array1.append(1)
    array2.append(14)

    print("array1", array1)
    print("array2", array2)

    array3 = array1.copy()

    print("array3", array3)

    array2.extend(array3)

    print(array2)

    indexarray3 = array2.index(7)

    print(indexarray3)

    array3.sort()

    print(array3)

    array3.remove(7)
    array3.remove(7)

    print(array3)

    array4 = array3.copy()

    print(array4)

    array4.reverse()

    print("array 3", array3)
    print("array 4", array4)
    inputnumber()

def EX3():
    print("Exercise 3")
    arrayEX3 = ["Number", "ID", "Name", "Count"]

    arraylen = len(arrayEX3)

    locate = arrayEX3.index("Name")

    print(locate)

    arrayEX3.append("Status")

    print(arrayEX3)
    inputnumber()

def EX4():
    print("Exercise 4")
    arrayEX4 = [['Number ID', 'Name', 'Count', 'Status'], []]
    arraylen = len(arrayEX4)
    print(arraylen)

    arrayEX4.insert(1, [1, "Rubber", 0, "Out of stock"])
    arrayEX4.insert(2, [2, "Ruler", 5, "In stock"])
    arrayEX4.insert(3, [3, "Pencil", 1, "In stock"])
    print(arrayEX4)
    inputnumber()

def inputnumber():
    while (True):
        i = int(input("Enter Input 1-4 For View Exercise 1-4 0 to Exit: "))
        if(i == 1):
            return EX1()
        if(i == 2):
            return EX2()
        if (i == 3):
            return EX3()
        if (i == 4):
            return EX4()
        if (i == 0):
            print("Exit...")
            break
        else:
            print("Wrong Input !!?")
            return inputnumber()
inputnumber()