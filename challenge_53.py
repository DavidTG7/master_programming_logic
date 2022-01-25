def fibonacci(_maxnumber):
    total_list = []
    if _maxnumber <= 0:
        return total_list
    else:
        a = 0
        b = 1
        result = 1
        if _maxnumber == 1:
            total_list.append(a)
            return total_list
        else:
            total_list.append(a)
            for i in range(_maxnumber - 1):
                total_list.append(result)
                result = a + b
                a = b
                b = result
    return total_list

my_number = int(input("Give the max number: "))
print(fibonacci(my_number))