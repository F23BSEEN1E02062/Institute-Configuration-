class department:
    def __init__ (self,name,code,head):
        self. name = name
        self. code = code
        self. head = head
        self. courses = []
    def add_course (self,course) :
        self.courses. append(course)
        
    def remove_course (self,course):
        if course in self.courses:
            print(self.courses.remove(course))
        else:
            print (f'Error:Given {course} is not in {self.name} courses')    
    def display_courses (self,course):
        print (f'courses offered in {self.name} department')
        for course in self.courses:
            print(course) 
class course:
    def __init__ (self,name,code,credit_hours):
        self.name=name
        self.code=code
        self.credit_hours=credit_hours
    def __str__ (self):
        return f'{self.name}:course code {self.code} ({self.credit_hours} credit_hours)'                 
if __name__=="__main__":
       # Creating departments
    
    deprt1 = department('Software Engineering','SE','Dr Nadeem Akhtar')  
    deprt2 = department('Information technology','IT','Dr naouman')
    deprt3 = department ('Food Science','FS','Dr Faisal iqbal')
    
       # Adding course to departments
    deprt1. add_course(course('Object oriented Programing','SE106',"4"))
    deprt1. add_course(course('Data structures','SE107','3'))
    
    deprt2. add_course(course('ICT','IT108','3'))
    deprt2. add_course(course('TBW','IT109','3'))
    
    deprt3. add_course(course('Applied Physics','FS110','3'))
    deprt3. add_course(course('Calculus','FS111','3'))
    deprt3. add_course(course('Biotechnology','FS112','4'))
       #Display Courses
    deprt1 .display_courses(course)    
    deprt2.display_courses(course)  
    deprt3.display_courses(course)