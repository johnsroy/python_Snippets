#!/bin/python/


#####PASS an unlimited number of key-value pairs inside a funtion#######

def createDict(**kvargs):
    for i in kvargs:
        print i, kvargs[i]
    print type(kvargs)
    return

def main():
    createDict(Cust1 = ('Derek',35,1974),Cust2 = ('Roy',23,1992))

if __name__=='__main__':main()


