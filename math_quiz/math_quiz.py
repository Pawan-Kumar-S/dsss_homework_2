import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer within the specified range [min_value, max_value].
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Randomly selects an arithmetic operator: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def arithmetic_operation(number1, number2, operator):
    """
    Performs an arithmetic operation based on the given operator and returns the problem and answer.
    """
    problem = f"{number1} {operator} {number2}"

    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2

    return problem, result

def math_quiz():
    """
    Conducts a math quiz game, prompting the user to solve random arithmetic problems.
    """
    score = 0
    questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You'll be presented with arithmetic problems, and your task is to provide the correct answers.")

    for _ in range(questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = arithmetic_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            user_answer = 0

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{questions}")

if __name__ == "__main__":
    math_quiz()
