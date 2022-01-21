'''Create a program to replace letters for numbers of a given text:
    O = 0
    I = 1
    E = 3
    A = 4
    S = 5
    G = 6
    T = 7
    B = 8
    P = 9

'''
# My solution:

my_text = input("Write something: ").upper().replace('O', '0').replace('I', '1').replace('E', '3').replace('A', '4').replace('S', '5').replace('G', '6').replace('T', '7').replace('B', '8').replace('P', '9')

print(my_text)
