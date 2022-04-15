"""Main module"""


# Imports from the game module
from game import Lesson
from game import Task
from game import Test
from game import Exam
from game import Study

# Sets for knowledge of topics and the practical knowledge.
know = set()
practice = set()

# Create the studies, tasks, test, and exam
study1 = Study("Series Study",
               "A study on series.",
               "Series")
study2 = Study("Functional series Study",
               "A study on functional series.",
               "Functional series")
task1 = Task("Series Task",
             "Series",
             "A task on series")
task2 = Task("Functional Series Task",
             "Functional series",
             "A task on functional series")
test = Test("Series Test",
            ["Series", "Functional series"],
            "A test on series and functional series",
            ["Series", "Functional series"])
study4 = Study("Multiple Integrals Study",
               "A study on multiple integrals.",
               "Multiple integrals")
task4 = Task("Multiple Integrals Task",
             "Multiple integrals",
             "A task on multiple integrals.")
exam = Exam("Calculus exam",
            ["Series", "Functional series", "Multiple integrals"],
            "The final exam on calculus.",
            ["Series", "Functional series", "Multiple integrals"])

# Create lessons list
lessons = [Lesson(i) for i in range(1, 6)]

# First lesson
lessons[0].name = "Series"
lessons[0].description = "Series lesson!"
lessons[0].add_material(study1)
lessons[0].add_material(task1)

# Second Lesson
lessons[1].name = "Functional Series"
lessons[1].description = "Functional series lesson!"
lessons[1].add_material(study2)
lessons[1].add_material(task2)

# Third lesson
lessons[2].name = "Series test lesson"
lessons[2].description = "Series Test Time!!! Get Ready!!!!"
lessons[2].add_material(test)

# Fourth lesson
lessons[3].name = "Multiple Integrals Lesson"
lessons[3].description = "A lesson on multiple integrals"
lessons[3].add_material(study4)
lessons[3].add_material(task4)

# Fifth lesson
lessons[4].name = "Exam time"
lessons[4].description = "The time has come for the exam. Good luck!"
lessons[4].add_material(exam)

# Is test passed
TEST_PASSED = False
# How many exam tries left
TRIES = 2
# Current lesson
CUR = 1
# Is exam passed
EXAM_PASSED = False

# The program runs until the exam is not passed or
# the following cycle is not broken.
while EXAM_PASSED is False:
    print("\n")
    # Print the current lecture and the available materials
    print(f"You are on lecture #{CUR} {lessons[CUR-1].name}:\n"
          f"{lessons[CUR-1].description}\n"
          f"Materials in this lesson:\n")
    materials = lessons[CUR-1].get_material()
    for i, mat in enumerate(materials):
        print(f"{i+1}: {mat.name}")

    # Print the available commands
    print("\nCommands available:")
    print("Drop Out")
    print("Back")
    print("Forward")
    print("Knowledge")
    print("Or select a material from the list by typing its number")
    command = input("> ")
    # Drop Out - end the game
    if command == "Drop Out":
        print("Bye Bye!")
        break
    # Back - go to the previous lecture
    # if the index of current lecture is not 1
    if command == "Back":
        if CUR > 1:
            CUR -= 1
        else:
            print("Cannot go back.")
    # Forward - go to the next lecture if
    # the index of current lecture is not 5
    elif command == "Forward":
        if CUR < 5:
            CUR += 1
        else:
            print("Cannot go forward.")
    # Knowledge - print information about the current knowledge
    # and practical knowledge.
    elif command == "Knowledge":
        print(f"You know "
              f"{know if len(know) else 'no topics in mathematics'}.")
        print(f"You have practical knowledge in "
              f"{practice if len(practice) else 'no topics in mathematics'}.")
    # If the command is a number and in range of the available materials,
    # chooses the corresponding material.
    elif command.isnumeric() and int(command) in range(1, len(materials) + 1):
        material = materials[int(command)-1]
        print(material.description)
        # Processing for exam material
        if isinstance(material, Exam):
            if material.passed(know, practice, TEST_PASSED):
                print("You successfully passed the course!!🎉🎉🎉🎉🎉"
                      " You can have your deserved chill!")
                EXAM_PASSED = True
            else:
                TRIES -= 1
                if TRIES:
                    print("Oh no! You did not pass the exam. "
                          "Luckily, you can try again. "
                          "Come back when you are ready.")
                else:
                    print("You did not pass the course "
                          "and you will be expelled!")
                    break
        # Processing for test material
        elif isinstance(material, Test):
            if material.passed(know, practice):
                TEST_PASSED = True
                print("Great job! You successfully passed the test!"
                      " Continue learning to pass the course!")
            else:
                print("You are not ready for the test! "
                      "Go back and learn everything!")
        # Processing for task material
        elif isinstance(material, Task):
            if material.knowledge in know:
                practice.add(material.knowledge)
                print(f"Congratulations! "
                      f"You learned practical {material.knowledge}")
            else:
                print(f"You do not know {material.knowledge} "
                      f"to complete this task.")
        # Processing for study material
        elif isinstance(material, Study):
            know.add(material.knowledge)
            print(f"Congratulations! You learned knowledge "
                  f"{material.knowledge}")
    # Error message - no such command is available
    else:
        print("There is no such command available")
