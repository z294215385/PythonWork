import random

number_of_streaks = 0
for experiment_number in range(10000):
    list = []
    count = 1
    for i in range(0, 100):
        list.append(random.randint(0, 1))
    for number in range(0, 99):
        if count >= 6:
            number_of_streaks += 1
            break
        if list[number] == list[number + 1]:
            count += 1
        else:
            count = 1

print('Chance of streak: %s%%' % (number_of_streaks / 100))
