class Class:
    def __init__(self,id:str, courses:list['Course'] = []) -> None:
        self._id = id
        self._courses = courses
    
    def addCourse(self, course: 'Course') -> None:
        self._courses.append(course)

class Course:
    def __init__(self, id:str, studants:list['Studant'] = []) -> None:
        self._id = id
        self._studants = studants

    def addStudant(self, studant: 'Studant') -> None:
        self._studants.append(studant)
    

class Studant:
    def __init__(self, id:str, name:str, age:int) -> None:
        self.id = id
        self.name = name
        self.age = age
