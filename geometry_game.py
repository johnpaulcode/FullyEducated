import math
import random

QUESTIONS = [
    'area of square',
    'perimeter of square',
    'area of rectangle',
    'perimeter of rectangle',
    'area of circle',
    'circumference of circle',
]


def ask_square_area():
    side = random.randint(1, 10)
    answer = side * side
    user = float(input(f"What is the area of a square with side length {side}? "))
    return abs(user - answer) < 0.01


def ask_square_perimeter():
    side = random.randint(1, 10)
    answer = 4 * side
    user = float(input(f"What is the perimeter of a square with side length {side}? "))
    return abs(user - answer) < 0.01


def ask_rectangle_area():
    width = random.randint(1, 10)
    height = random.randint(1, 10)
    answer = width * height
    user = float(input(f"What is the area of a rectangle {width}x{height}? "))
    return abs(user - answer) < 0.01


def ask_rectangle_perimeter():
    width = random.randint(1, 10)
    height = random.randint(1, 10)
    answer = 2 * (width + height)
    user = float(input(f"What is the perimeter of a rectangle {width}x{height}? "))
    return abs(user - answer) < 0.01


def ask_circle_area():
    radius = random.randint(1, 10)
    answer = math.pi * radius ** 2
    user = float(input(f"What is the area of a circle with radius {radius}? (use 3.14 for pi) "))
    return abs(user - answer) < 0.1


def ask_circle_circumference():
    radius = random.randint(1, 10)
    answer = 2 * math.pi * radius
    user = float(input(f"What is the circumference of a circle with radius {radius}? (use 3.14 for pi) "))
    return abs(user - answer) < 0.1


QUESTION_FUNCS = {
    'area of square': ask_square_area,
    'perimeter of square': ask_square_perimeter,
    'area of rectangle': ask_rectangle_area,
    'perimeter of rectangle': ask_rectangle_perimeter,
    'area of circle': ask_circle_area,
    'circumference of circle': ask_circle_circumference,
}


def play(num_questions=5):
    correct = 0
    for _ in range(num_questions):
        q = random.choice(QUESTIONS)
        if QUESTION_FUNCS[q]():
            print("Correct!\n")
            correct += 1
        else:
            print("Incorrect\n")
    print(f"You got {correct} out of {num_questions} correct.")


if __name__ == '__main__':
    play()
