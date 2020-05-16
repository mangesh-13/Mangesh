# Three levels of inner classes

# Person
#    Head
#     talk
#     Brain
#      think


class Person:
    def __init__(self):
        self.name="Mangesh"
        self.head=self.Head()
   
    def display(self):
        print('Name=',self.name)
        self.head.talk()
        self.head.brain.think()
        
    class Head:
        def __init__(self):
         self.brain=self.Brain() 
        
        def talk(self):
            print("Talking")
            
        class Brain:
            def think(self):
                print("Thinking")
                
                
p=Person()
p.display()