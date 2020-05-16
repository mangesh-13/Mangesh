# Person(outer class)
#     name 
#     DOB   (inner class)
#         dd
#         mm
#         yyyy


class Person:
    def __init__(self):
        self.name="Mangesh"
        self.dob=self.DOB()
    
    def display(self):
        print("Name:",self.name)
        self.dob.display()
        
        
    class DOB:
        def __init__(self):
            self.dd=15
            self.mm=8
            self.yyyy=1947
       
        def display(self):
            print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))
            
p=Person()
p.display()