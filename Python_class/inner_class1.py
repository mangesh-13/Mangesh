
# inner class
# Person:
#     name
#     dob=DOB()
    
#     DOB:
#         dd
#         mm
#         yyyy




class Person:
    def __init__(self,name,dd,mm,yyyy):
        self.name=name
        self.dob=self.DOB(dd,mm,yyyy)
        
    def display(self):
        print('Name:',self.name)
        self.dob.display()
        
    class DOB:
        def __init__(self,dd,mm,yyyy):
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
    
        def display(self):
            print("DOB={}/{}/{}".format(self.dd,self.mm,self.yyyy))
        
        
p=Person("Vinayak",13,4,1947)
p.display()
p1=Person("Aniket",13,12,1988)
p1.display()
            
            
