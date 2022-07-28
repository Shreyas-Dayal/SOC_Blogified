class People:
    def __init__(self,name,age,gender,dob) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.dob = dob

    def intro(self):
        print(f"Hi!, My name is {self.name}. I am {self.age} years old.")

    
class Teacher(People):
    def sub(self,sub):
        self.sub = sub
    
    def subject(self):    
        print(f"Hello, My name is {self.name} and I teach {self.sub}")

class Student(People):
    def std(self,grade,roll_number):
        self.grade = grade
        self.roll_number = roll_number

    def grade(self):
        print(f"Hi!, My name is {self.name} and I study in {self.grade} grade.")
    def roll_no(self):
        print(f"{self.name}'s roll number is {self.roll_number}.")


teacher1 = Teacher("Sam",32,'Male',(1,1,1990))
teacher1.sub("Science")

teacher2 = Teacher('Blake',30,'Female',(1,2,1992))
teacher2.sub("Maths")

teacher3 = Teacher('Rachel',28,'Female',(1,4,1994))
teacher3.sub("English")

student1 = Student('Ross',16,'Male',(30,5,2012))
student1.std(10,32)

student2 = Student('Micheal',16,'Male',(28,4,2012))
student2.std(10,20)


teacher1.intro()
teacher1.subject()

student1.intro()
student1.roll_no()