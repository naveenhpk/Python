#operator over loading
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    
    def __add__(self,other):
        self.other=self.rollno+other.rollno