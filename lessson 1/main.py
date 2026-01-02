class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("hi i am ",self.name,"and my color is",self.color)

dog1=Dog("max","yellow")
dog1.bark()
dog2=Dog(" bruno","black")
dog2.bark()
