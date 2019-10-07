#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program checks if a number matched the months


def main():
    # This function shows if the number matched the months

    user_input = int(input("Enter an integer: "))
    print("")

    if user_input == 1:
        print("January")
    elif user_input == 2:
        print("February")
    elif user_input == 3:
        print("March")
    elif user_input == 4:
        print("April")
    elif user_input == 5:
        print("May")
    elif user_input == 6:
        print("June")
    elif user_input == 7:
        print("July")
    elif user_input == 8:
        print("August")
    elif user_input == 9:
        print("September")
    elif user_input == 10:
        print("October")
    elif user_input == 11:
        print("November")
    elif user_input == 12:
        print("December")
    else:
        print("nothing to say !")


if __name__ == "__main__":
    main()
