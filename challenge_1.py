''' Given a number, return its multiplication table:
    Multiplication table of 5:
    1 x 5 = 5
    2 x 5 = 10
    3 x 5 = 15
    4 x 5 = 20
    5 x 5 = 25
    6 x 5 = 30
    7 x 5 = 35
    8 x 5 = 40
    9 x 5 = 45
    10 x 5 = 50
'''
# My solution:


def multiplication_table(num):
    
    print(f"Multiplication table of {num}:")

    for n in range(1, 11):
        result = n * num
        print(f"{num} x {n} = {result}")
        

my_num = int(input("Give me the number to get the multiplication table: "))

multiplication_table(my_num)