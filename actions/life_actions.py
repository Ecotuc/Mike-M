import random
import time

goals =['Graduate', 'Trips', 'Cars', 'Home', 'Buisiness']
achievements = []

def get_goals():
    return goals

def done(goal):
    print('{} completed, next goal'.format(goal))
    del goals[0]
    achievements.append(goal)

def success(goal):
    return bool(random.getrandbits(1))

def imAlive():
    goalss = get_goals()
    return len(goalss) > 0

def keepOn(goal):
    print('Kepp on until {} is done'.format(goal))
    time.sleep(3)

def die():
    print('\n\n\nLife achievements:\n')
    print(achievements)
    print("\n\n\n")
    print("-----------------------------------------------------------------")
    print("| I don't have dreams I have goals. Now it's onto the next one. |")
    print("-----------------------------------------------------------------")
    print("\n\n\n")