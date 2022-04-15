# labs4.5_6

## lab5

Lab 5 is created by changing the game file and adding implementations
of different classes. There were minor changes to the main.py file,
but they almost did not impact the flow of the game.

## lab6

Lab 6 is about completing the Calculus course in a university.

The player (student) needs to pass the exam to complete the course.
In this game there are the following classes:

Lesson

Material -> Study
         -> Task -> Test -> Exam

A lesson is a class that has a name, description and materials that
are available. It is initialized by optional name and optional
description. The materials can be added or accessed using 
respectively the methods add_material and get_material.

Material is a class that is initialized by a name and description.

Task extends the Material and also includes the string knowledge attribute
that represents the knowledge that the student needs to have to
successfully solve this task.

Study extends the Material and also includes the string knowledge attribute
that represents the knowldge that the student will have after
completing the study.

Test extends Task and also includes the practice attribute that represents
the practical knowledge that the student will need to have to pass the test.
In main.py, test has lists of strings of knowledge and practice.
Includes the function passed which checks the knowledge and practical 
knowledge with the requirements. Returns True if all requirements are
satisfied, otherwise False.

Exam extends Test. Also includes the checking of additional requirement
that is an attribute to the function passed.

In the game, there are 5 lessons. First two each have a study and a task.
Third has a test that requires to pass all the previous studies and tasks.
Fourth lesson has a study and a task. Last lesson is an exam.
Exam requires the test to be passed, and also all the previous studies and tasks.
If the exam is failed, the player has another try. If he fails again,
the respective message is displayed and the game ends. Otherwise,
the player completes the course.

The player has the following commands on his turn:
Back - to go to the previous lesson if it is possible
Forward - to go to the next lesson if it is possible
Drop Out - end the game
Knowledge - display the current knowledge of the player
Number - select a material from the current lesson if the number is in bounds
of the materials list.
In any other case, returns the message that the command is not supported.

The log.txt file can help understand the flow of the game. Also, a look at
the game.py and main.py files can help understand the classes structure and
how the game works.
