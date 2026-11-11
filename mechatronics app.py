# Mechatronics Quiz Questions

questions = [

    "What does PLC stand for?",

    "Which component stores electrical energy?",

    "What is the unit of electrical resistance?",

    "Which device converts electrical energy into mechanical energy?",

    "What does CNC stand for?"

]

# Multiple choice options

options = [

    ["A. Programmable Logic Controller", "B. Personal Logic Control", "C. Program Line Computer", "D. Power Logic Controller"],

    ["A. Resistor", "B. Capacitor", "C. Diode", "D. Switch"],

    ["A. Volt", "B. Ampere", "C. Ohm", "D. Watt"],

    ["A. Generator", "B. Electric Motor", "C. Transformer", "D. Battery"],

    ["A. Computer Numerical Control", "B. Central Network Control", "C. Computer Number Connection", "D. Control Numerical Circuit"]

]

# Correct answers

answers = ["A", "B", "C", "B", "A"]

# Start the quiz

score = 0

print("\nWelcome to the Mechatronics Quiz!")

# Ask each question

for i in range(len(questions)):

    print("\nQuestion", i + 1)

    print(questions[i])

    # Display multiple choice options

    for option in options[i]:

        print(option)

    # Get user's answer

    user_answer = input("Choose A, B, C or D: ").upper().strip()

    # Check the answer

    if user_answer == answers[i]:

        print("Correct!")

        score += 1

    elif user_answer in ["A", "B", "C", "D"]:

        print("Wrong answer!")

    else:

        print("Invalid option!")

# Display final score

print("\nQuiz completed!")

print("Your score is:", score, "out of", len(questions))