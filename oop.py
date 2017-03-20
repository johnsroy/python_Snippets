#!/bin/python/

def addNumbers(*args):
    final_value = 0
    if args:
        for i in args:
            final_value += i
        return final_value
    else:
        return "Please enter a valid no."


def main():
    print addNumbers(20,50,30,50)

if __name__ == '__main__':main()

