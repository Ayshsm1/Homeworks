#zad1
def sum_of_digits(num):
    result = 0

    for iter in range(0, 3):
        result = result + num % 10
        num = num // 10 
    return result
print(sum_of_digits(235))
#zad2
def to_digits(n):
    number = 12345
    to_digits = [int(n) for n in str(number)]
    print(to_digits)
    pass
#zad3
def to_number(digits):
    to_number = [3, 5, 6, 9]
    number = 0
    for current_digit in to_number:
        number = number*10 + current_digit
    pass
#zad4
def fib_number(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_number(n-1) + fib_number(n-2)
    print(fib_number(20))
    pass
#zad5 
def is_number_balanced(n):
    left_sum = 0
    right_sum = 0
    for i in range(0, int(len(n)/2)):
        left_sum = left_sum + int(n[i])
        right_sum = (right_sum + int(n[len(n) - 1 - i]))
        if (left_sum == right_sum):
            print("True", end = '\n')
        else:
            print("False", end = '\n')
    pass
#zad6