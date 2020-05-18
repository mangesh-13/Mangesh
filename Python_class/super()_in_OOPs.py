# super() keyword
#Advantages od super()
#1) code reusabiliy
#2) Use to call parent class constructor and methods

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #100 properties
    
    def display(self):
        print("Name=",self.name)
        print("age=",self.age)
        
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    
    def display(self):
        super().display()
        print("rollno=",self.rollno)
        print("marks=",self.marks)
        

class Teacher(Person):
    def __init__(self,name,age,salary,subject):
        super().__init__(name,age)
        self.salary=salary
        self.subject=subject
   
    def display(self):
        super().display()
        print("rollno=",self.salary)
        print("marks=",self.subject)
    
    

s=Student("Mangesh",50,105,92)
s.display()
t=Teacher("Amar",62,10000,"Python")
t.display()