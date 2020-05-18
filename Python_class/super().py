class A:
    def m1(self): 
        print("A Class Method")


class B(A):
    def m1(self):
        super().m1()
        print("B Class Method")
        
class C(B):
    def m1(self):
        super().m1()
        print("C Class Method")

class D(C):
    def m1(self):
        super().m1()
        print("D Class Method")

class E(D):
    def m1(self):
        super().m1()
        print("E Class Method")
        
e=E()
e.m1()

# How to call a perticular parent class Method
# syntax is :
#            Parentclassname.methodname(self)
#            e.g.  B.m1(self)