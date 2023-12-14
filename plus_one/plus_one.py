def plusOne(digits=[]):
    number = 0
    for i in digits:
        number = number * 10 + i

    number = number + 1
    list1 = [int(i) for i in str(number)]

    return list1

number=[1,2,8]
print(plusOne(number))