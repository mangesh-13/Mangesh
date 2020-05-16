#without existing outer class object there is no chance of
#existing of inner class object
#So if you want to call inner class object method we need
# to create outer class object and using that object we can 
#create inner class object. Then using that object reference
# we can call inner class object methods.

#  Examples of inner class
#e.g Braine without person is not possible
# e.g engine without car is not possible




class Outer:
    def __init__(self):
        print("Outer class object creation")
    
    class Inner:
        def __init__(self):
            print("inner class object creation")
        
        def m1(self):
            print("Inner class method")
            
            
            
o=Outer()
i=o.Inner()
i.m1()