# FizzBuzz challenge:


my_list = list(range(1, 101)) #It is no necesary to create a list with the number from 1 to 0 like this.

for num in my_list: #We can iterate trough the for loop using range function for num in range(1, 101)
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)