

'''
class P:
    def __init__(self):
        print("Parent constructor")
    
    def m1(self):
        print("Parent instance method")
    
    @classmethod
    def m2(cls):
        print("Parent class method")
    
    @staticmethod
    def m3():
        print("Parent static method")
        
        
class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        
c=C()
'''

class P:
    def __init__(self):
        print("Parent constructor")
    
    def m1(self):
        print("Parent instance method")
    
    @classmethod
    def m2(cls):
        print("Parent class method")
    
    @staticmethod
    def m3():
        print("Parent static method")
        
        
class C(P):
    def method1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        
c=C()
c.method1()                
        
        
        


