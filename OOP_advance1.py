#!/bin/python/

__metaclass__ = type #Allow py 2.7 to user Py 3.0 objects
#####OOP Concepts#######

class Animal:
    
    __name = "No Name"
    __owner = "No owner"
    
    ##CONSTRUCTOR accepting infinite tuples in the form of key-value pairs
    def __init__(self,**kvargs):
        self._attributes = kvargs
    
    ###### USER of the class needs to set up these unlinited arguments
    ###### THIS ONE FUNCTION CAN SUSTITUTE ALL OF THE ACCESSOR FUNCTIONS PREVIOUSLY USED ######
    def set_attributes(self,key,value):
        self._attributes[key] = value
        return
        
    ###### TO RETURN ALL OF THESE ATTRIBUTES WE NEED TO USE JUST 1 GETTER FUNCTION ########
    def get_attributes(self,key):
        return self._attributes.get(key,None)
    
    def noise(self):
        print('err')
        return

    def move(self):
        print('Move forward Animal')
        return

    def eat(self):
        print('Crunch crunch')
        return

######INHERITANCE#########
class Dog(Animal):
    
    ####CONSTRUCTOR####
    def __init__(self,**kvargs):
        super(Dog, self).__init__() #super gets all the parent classes methods and variables
                                    #Need to add a line on top to get this feature in Py 2.7
        self._attributes=kvargs

#####Overriding a method#######
    def noise(self):
        print ("Woof, Woof")
        Animal.noise(self) #To display the parent noise as well
        return

##########ANOTHER INHERITED CLASS TO SHOW POLYMORPHISM###########
class cat(Animal):

    def __init__(self,**kvargs):
        super(cat,self).__init__()
        self._attributes=kvargs

    def noise(self):
        print("Meow Meow")
        return

    def noise2(self):
        print ("Purr")
        return

#####  POLYMORPHISM METHOD. This method would show how polymorphism exhibits two seperate functinalities
##depending on the classes
def playWithAnimals(Animal):
    Animal.noise()
    Animal.eat()
    Animal.move()
    Animal.set_attributes('clean','Yes')
    print(Animal.get_attributes('clean'))
    print (Animal.get_attributes('__name'))
    print (Animal.get_attributes('__owner'))
    print('\n')


def main():
    jake = Dog(__name='Jake',__owner='Paul')
    sophie = cat(__name='Sophie',__owner='Sue')
    playWithAnimals(sophie)
    playWithAnimals(jake)

if __name__ =='__main__':main()







