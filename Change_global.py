#!/bin/python/

globalTen = 10

def changeGlobal():
    #globals()['globalTen'] = 20
    ####OR#######
    global globalTen
    globalTen = 20

def main():
    print globalTen
    changeGlobal()
    print globalTen

if __name__ == '__main__':main()

