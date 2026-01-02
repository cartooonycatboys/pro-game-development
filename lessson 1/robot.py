class Robot:
    def __init__(self,name,use):
        self.name=name
        self.use=use
    def bark(self):
        print("hello I am",self.name,"my use is",self.use)

robot1=Robot("Rob","cleaning")
robot1.bark()

robot2=Robot("Bob","cooking")
robot2.bark()

robot3=Robot("Tob","errands")
robot3.bark()