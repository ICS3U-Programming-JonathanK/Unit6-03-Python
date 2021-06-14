#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: June 14, 2021
# The program places the numbers into a single variable
# and prints them to the console. The program has a function
# to find the minimum value of a list.

import random


def find_min_value(list_of_numbers):

    minimum = 101
    for number in range(0, len(list_of_numbers)):
        if(list_of_numbers[number] < minimum):
            minimum = list_of_numbers[number]
    return minimum


def main():
    # this function uses an array
    list_of_int = []
    min_value = 0

    # uses a loop
    for loop_number in range(0, 11):
        random_num = random.randint(10, 100)
        list_of_int.append(random_num)
    print("")

    for loop_number in range(0, 11):
        print("{} added to the list at position"
              " {} ".format(list_of_int[loop_number], loop_number))
    print("")

    # gets the minimum value from the list and displays it
    min_value = find_min_value(list_of_int)
    print("The min value is: {}". format(min_value))


if __name__ == "__main__":
    main()
