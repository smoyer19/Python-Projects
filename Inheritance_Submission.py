


#Setting Parent class for my name First and Last
class MyName:
    FirstName = "Shea"
    LastName = "Moyer"

# setting MyConacact as Child class 1
class MyContact(MyName):
    email = "smoyer19@gmail.com"
    phone = 6512630130

# setting Bio as Child class 2
class Bio(MyName):
    BloodType = "A"
    RH = "+"
    
    def __init__(Self, FirstName, LastName):
        Self.FirstName
        Self.LastName



print(MyName.FirstName)
print(MyName.LastName)


