'''
1.	Write a program to implement Constructor with Variable Number of Arguments.
'''


class A:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print(f"Name={self.name}\nage={self.age}\ncity={self.city}")




a=A("Mangesh",60,"Pune")
a.display()




