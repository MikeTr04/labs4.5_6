"""MAIN GAME MODULE"""


# pylint: disable=R0903
# pylint: disable=W0105
# pylint: disable=W0613
class Lesson:
    """Lesson class"""
    def __init__(self, name="Lecture", description="Lecture description"):
        """A lesson can have name, lecture, and available materials.
        By default, name is 'Lecture', description is 'Lecture description',
        and materials are []. The lesson can be initialized with or without
        name and description."""
        self.__name = name
        self.__description = description
        self.__material = []

    """Getter, setter, and property name for __name."""
    def __set_name(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name

    name = property(__get_name, __set_name)

    """Getter, setter, and property description for __description."""
    def __set_description(self, description):
        self.__description = description

    def __get_description(self):
        return self.__description

    description = property(__get_description, __set_description)

    def add_material(self, material):
        """Add a material to the materials list."""
        if isinstance(material, Material):
            self.__material.append(material)

    def get_material(self):
        """Returns the materials."""
        return self.__material


class Material:
    """Represents a Task, Test, Exam, or Study."""
    def __init__(self, name: str, description: str):
        """A material has a name and description.
        Can be initialized by name and description."""
        self.__name = name
        self.__description = description

    """Getter, setter, and property name for __name."""
    def __set_name(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name

    name = property(__get_name, __set_name)

    """Getter, setter, and property description for __description."""
    def __set_description(self, description):
        self.__description = description

    def __get_description(self):
        return self.__description

    description = property(__get_description, __set_description)


class Task(Material):
    """Task class."""
    def __init__(self, name: str, knowledge, description: str):
        """A task uses the Material __init__ function and also includes the
        knowledge attribute. Knowledge represents the knowledge that the
        student needs to have to solve this task."""
        super().__init__(name, description)
        self.__knowledge = knowledge

    """Getter, setter, and property knowledge for __knowledge."""
    def __set_knowledge(self, knowledge):
        self.__knowledge = knowledge

    def __get_knowledge(self):
        return self.__knowledge

    knowledge = property(__get_knowledge, __set_knowledge)


class Test(Task):
    """Test class."""
    def __init__(self, name: str, knowledge, description: str, practice: list):
        """A test uses the Task __init__ function and also includes the
        practice attribute. Practice represents the practical knowledge
        that the student needs to have to solve this test."""
        super().__init__(name, knowledge, description)
        self.__practice = practice

    """Getter, setter, and property practice for __practice."""
    def __set_practice(self, practice):
        self.__practice = practice

    def __get_practice(self):
        return self.__practice

    practice = property(__get_practice, __set_practice)

    def passed(self, know, practice, req=True):
        """Checks if the student has the knowledge and practice
        to solve the test, as well as if the requirement is satisfied."""
        for i in self.knowledge:
            if i not in know:
                return False
        for i in self.practice:
            if i not in practice:
                return False
        return True


class Exam(Test):
    """Exam class. Uses the Test __init__ function."""
    def passed(self, know, practice, req=True):
        """Checks if the student has the knowledge and practice
        to solve the test, as well as if the requirement is satisfied."""
        if not req:
            print("Test not passed! You cannot take the exam!")
            return False
        for i in self.knowledge:
            if i not in know:
                return False
        for i in self.practice:
            if i not in practice:
                return False
        return True


class Study(Material):
    """Study class."""
    def __init__(self, name: str, description: str, knowledge: list):
        """Study uses the Material __init__ function and also includes the
        knowledge attribute. Knowledge represents the knowledge that the
        student will learn after doing this study."""
        super().__init__(name, description)
        self.knowledge = knowledge
