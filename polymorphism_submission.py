

#Parent Class

class Pet:
    breed = ""
    care = ""

    def information(self):
        msg = "\nBreed: ()\nCare: ()".format(self.breed, self.care)
        return msg

#child class
class Dog(Pet):
    breed = "Golden Retriever"
    care = "Needs outside"
    #added attributes outside parent
    leash = True
    clean = "Needs regular bathing"
    
    #using information to overite the parent class demonstrating polymorphism
    def information(self):
        msg = "\nDogs are very friendly and loyal to people!"
        return msg

#another child class
class Cat(Pet):
    breed = "Russian Blue"
    care = "Litter Box"
    leash = False
    clean = "Self cleaning, may need additional bathing"
    #additional attributes on top of Dog attributes
    clawing = "needs claw toys"
    hairballs = "May produce hairballs"
    
    #using another functiont to represent polymorphism
    def information(self):
        msg = "\nCats let you know when you can do things for them!"
        return msg
    





#Intstantiating Dog and Cat to call on the information from the overwritten parent class.
if __name__ == "__main__":
    dog1 = Dog()
    cat1 = Cat()
    print(dog1.information())
    print(cat1.information())
 
