import random

class FruitQuiz:

    # Create a constructor
    def __init__(self):
        # Create a dictionary of fruits as keys and color as value
        self.fruits = {
            'apple': 'red',
            'orange': 'orange',
            'watermelon': 'green',
            'banana': 'yellow'
        }

    # Function for the quiz, here a fruit will be chosen randomly
    def quiz(self):
        while True:

            fruit, color = random.choice(list(self.fruits.items()))

        print("What is the color of {}".format(fruit))
        user_answer = input()

        if(user_answer.lower() == color):
            print("corroct answer")
        else:
            print("wrong answer")

        option = int(input("enetr 0,of you want to play againother wise enter 1 :"))
        if(option):
        break
print("welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()
