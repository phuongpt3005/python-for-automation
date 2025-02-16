#! /usr/bin/env python

def to_seconds(h, m, s):
    return h*3600+m*60+s


print("Welcome to this time converter")


cont = "y"
while cont.lower() == "y":
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue] ")

print("Good bye!")
