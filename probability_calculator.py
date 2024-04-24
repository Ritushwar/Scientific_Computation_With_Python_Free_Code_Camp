import copy
import random

class Hat:
    def __init__(self,**balls):
        self.contents = []
        for key, value in balls.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self,number):
        if number > len(self.contents):
            return self.contents
        draws_balls = []
        for _ in range(number):
            choice = random.randrange(len(self.contents))
            draws_balls.append(self.contents.pop(choice))

        return draws_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_no_of_balls = []
    for key in expected_balls:
        expected_no_of_balls.append(expected_balls[key])
    success = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)

        no_of_balls = []

        for key in expected_balls:
            no_of_balls.append(balls.count(key))
        expected = True
        for count, expected_count in zip(no_of_balls,expected_no_of_balls):
            if count < expected_count:
                expected = False
                break
        if expected:
            success += 1
    return success/num_experiments