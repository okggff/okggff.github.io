import random
import math
import time
import sys

def loading_animation():
    chars = "/-\\|"
    for _ in range(10):
        for char in chars:
            sys.stdout.write(f"\rThinking really hard... {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    for _ in range(10):
        for char in chars:
            sys.stdout.write(f"\rFinding brain patterns... {char}")
            sys.stdout.flush()
            time.sleep(0.05)
    for _ in range(8):
        for char in chars:
            sys.stdout.write(f"\rDoing the most complex math to find ur brain activity... {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r  Loading Complete!                                                                                                       \n")


def generate_random_number():
    return random.randint(1, 100)

def calculate_square_root(number):
    return math.sqrt(number)

while True:
    get_input = input("Enter a random number between 1 and 100: ")

    loading_animation()

    time.sleep(0.2)

    print(f"Ur thinking of number {get_input}")

    time.sleep(0.2)



    if get_input != "98" or get_input != "87" or get_input != "76":
        print("you're gay...")
    else:
        print("you're not gay!")

    time.sleep(10)
    for i in range(60):
        print("   ")

