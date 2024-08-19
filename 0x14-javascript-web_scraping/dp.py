#!/usr/bin/python3

def fibo(number):
    number = int(number)
    if number < 0:
        return "Invalid input"
    elif number == 1:
        return [0]
    elif number == 0:
        return [0]
    elif number == 2:
        return [0, 1]
    else:
        my_list = [0, 1]
        for i in range(2, number):

            my_list.append(my_list[i - 1] + my_list[i - 2])

        return my_list, sum(my_list)
    

if __name__ == '__main__':
    n = input("Please enter an int: ")
    n, _sum = fibo(n)
    print(f'sum of the fibo is: {_sum}')
    for value in n:
        print(value, end=", ")
