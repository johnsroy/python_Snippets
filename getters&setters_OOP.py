#!/bin/python/


#####OOP Concepts#######

class Animal:
    __hungry = "Yes" #private_variables
    __name = "No Name"
    __owner = "No owner"

    def __init__(self):
        pass

###Using getters and setters###

    def set_owner(self,newOwner):
        self.__owner = newOwner
        return

    def get_owner(self):
        return self.__owner


    def noise(self):
        print('err')
        return

def main():
    dog = Animal() #Creating an object
    dog.set_owner('Sue')
    print dog.get_owner()
    dog.noise()

if __name__ =='__main__':main()







