
#1) From child class by using super we cant call parent
# class instance variables.We should use self only

#2) From child class by using super method we can call
#   parent class static variables


class P:
    a=10
    def __init__(self):
        self.b=20
        
        
class C(P):
    def m1(self):
        print(super().a)
        print(self.b)
c=C()
c.m1()
    


