# Name: Han Xinpeng
# Assignment One
# ddl is 22/9/2026 23:59pm
#
# ELEC7023 Workshop - Edge computing device programming for AI projects
# Assignment 1: Python Basics
#
# How to run:
#   python3 "assignment 1_Han Xinpeng.py"      (Jetson Nano / Linux)
#   python "assignment 1_Han Xinpeng.py"       (Windows)
# Then type 1 / 2 / 3 to run a task, 0 to quit.

# Task C needs the turtle window, so import it only when it is used.
# (If turtle is imported at the top, it may fail on a machine without a display.)


# ============================================================
# Task A: Simple Calculator
# Prompt for first number, second number and operator,
# then display the math result.
# ============================================================
def task_a_calculator():
    print("\n--- Task A: Simple Calculator ---")
    print("Simple Calculator")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Result: cannot divide by zero")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid operation")


# ============================================================
# Task B: QA Bot
# Interactive bot that matches user queries with if / elif / else.
# Keywords supported (>= 5): hello, python, jetson, ai, name, bye
# ============================================================
def task_b_qa_bot():
    print("\n--- Task B: QA Bot ---")
    print("Question Answering Bot")
    print("(keywords: hello / python / jetson / ai / name / bye)")

    while True:
        question = input("Ask me something: ")
        question = question.lower().strip()   # make matching easier

        if question == "hello":
            print("Bot: Hello! Nice to meet you.")
        elif question == "python":
            print("Bot: Python is a language.")
        elif question == "jetson":
            print("Bot: Jetson Nano is an AI computer.")
        elif question == "ai":
            print("Bot: AI means Artificial Intelligence.")
        elif question == "name":
            print("Bot: My name is Python Bot.")
        elif question == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")


# ============================================================
# Task C (bonus): Turtle Drawing
# Rainbow star burst: a for loop draws 90 stars, the colour is
# taken from the colour wheel and the size grows step by step,
# so both colour and length change dynamically.
# ============================================================
def task_c_turtle():
    print("\n--- Task C (bonus): Turtle Drawing ---")
    import colorsys
    from turtle import Turtle, Screen

    screen = Screen()
    screen.bgcolor("black")
    screen.title("Assignment 1 - Turtle Drawing")

    pen = Turtle()
    pen.speed(0)
    pen.hideturtle()

    total = 90
    for i in range(total):
        # colour changes dynamically: walk around the colour wheel
        r, g, b = colorsys.hsv_to_rgb(i / total, 1.0, 1.0)
        pen.color(r, g, b)
        pen.pensize(1)

        # length changes dynamically: the stars grow one by one
        length = 30 + i * 4
        for _ in range(5):          # 5 points = 1 star
            pen.forward(length)
            pen.right(144)          # 144 degrees makes a star point
        pen.right(6)                # rotate a little before the next star

    print("Drawn %d stars. Close the turtle window to continue." % total)
    screen.mainloop()


# ============================================================
# Menu: one single file, choose which task to run
# ============================================================
def main():
    while True:
        print("\n===== Assignment 1: Python Basics =====")
        print("1. Simple Calculator")
        print("2. QA Bot")
        print("3. Turtle Drawing (bonus)")
        print("0. Quit")
        choice = input("Choose a task (0-3): ").strip()

        if choice == "1":
            task_a_calculator()
        elif choice == "2":
            task_b_qa_bot()
        elif choice == "3":
            task_c_turtle()
        elif choice == "0":
            print("Bye.")
            break
        else:
            print("Invalid choice, please enter 0-3.")


if __name__ == "__main__":
    main()
